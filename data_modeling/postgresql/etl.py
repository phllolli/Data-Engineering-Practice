import os, glob, psycopg2, sql_queries
import pandas as pd
import numpy as np

def process_song_file(cur, filepath):
    
    df = pd.read_json(filepath, lines = True)
    df = df.reindex(sorted(df.columns), axis=1).replace({np.nan, None})
    
    for value in df.values:
  
        artist_id, artist_latitude, artist_location, artist_longitude, artist_name, duration, num_songs, song_id, title, year = value

        data_artist = [artist_id, artist_name, artist_location, artist_latitude, artist_longitude]
        data_song = [song_id, title, artist_id, year, duration]
        
        cur.execute(sql_queries.insert_record.artist, data_artist)
        cur.execute(sql_queries.insert_record.song, data_song)

def process_log_file(cur, filepath):
    
    df = pd.read_json(filepath, lines = True)
    
    df = df[df['page'] == 'NextSong']
    
    ts = pd.to_datetime(df['ts'], unit = 'ms')
        
    data_time = []
    for row in ts:
        data_time.append([row, row.hour, row.day, row.week, row.month, row.year, row.day_name()])
    col_labels = ('start_time', 'hour', 'day', 'week', 'month','year','weekday')
    df_time = pd.DataFrame.from_records(data_time, columns=col_labels)

    for i, row in df_time.iterrows():
        cur.execute(sql_queries.insert_record.time, list(row))
    
    df_user = df[['userId', 'firstName', 'lastName', 'gender', 'level']]
    
    for i, row in df_user.iterrows():
        cur.execute(sql_queries.insert_record.user, list(row))
        
    for i, row in df.iterrows():

        cur.execute(sql_queries.select.song, (row.song, row.artist, row.length))
        result = cur.fetchone()

        if result:
            songid, artistid = result
        else:
            songid, artistid = None, None

        data_songplay = (i, pd.to_datetime(row.ts, unit='ms'), int(row.userId), row.level, songid, artistid, row.sessionId, row.location, row.userAgent)

        cur.execute(sql_queries.insert_record.songplay, data_songplay)

def process_data(cur, conn, filepath, func):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))

    return all_files   

def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=mydb user=postgres password={}".format(open('password.txt','r').read())
        )
    cur = conn.cursor()
    process_data(cur, conn, 'C:/Users/Admin/Documents/GitHub/SQLtest/data_modeling/postgresql/data/song_data', process_song_file)
    process_data(cur, conn, 'C:/Users/Admin/Documents/GitHub/SQLtest/data_modeling/postgresql/data/log_data', process_log_file)
    
    conn.close()
    
if __name__ == '__main__':
    main()