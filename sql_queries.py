class create_table:
    songplay = ("""
        CREATE TABLE IF NOT EXISTS songplays
        (songplay_id int PRIMARY KEY, 
        start_time date , 
        user_id int NOT NULL, 
        level text, 
        song_id text, 
        artist_id text, 
        session_id int, 
        location text, 
        user_agent text)
    """)

    user = ("""
        CREATE TABLE IF NOT EXISTS users
        (user_id int PRIMARY KEY, 
        first_name text NOT NULL, 
        last_name text NOT NULL, 
        gender text, 
        level text)
    """)

    song = ("""
        CREATE TABLE IF NOT EXISTS songs
        (song_id text PRIMARY KEY, 
        title text NOT NULL, 
        artist_id text NOT NULL, 
        year int, 
        duration float NOT NULL)
    """)

    artist = ("""
        CREATE TABLE IF NOT EXISTS artists
        (artist_id text PRIMARY KEY,
        name text NOT NULL, 
        location text, 
        lattitude float, 
        longitude float)
    """)

    time = ("""
        CREATE TABLE IF NOT EXISTS time
        (start_time date PRIMARY KEY,
        hour int, 
        day int, 
        week int, 
        month int, 
        year int, 
        weekday text)
    """)
    
    all = [user, artist, song, time, songplay]
    
class drop_table:
    songplay = "DROP TABLE IF EXISTS songplays"
    user = "DROP TABLE IF EXISTS users"
    song = "DROP TABLE IF EXISTS songs"
    artist = "DROP TABLE IF EXISTS artists"
    time = "DROP TABLE IF EXISTS time"
    all = [songplay, user, song, artist, time]
    
class insert_record:
    songplay = ("""
                INSERT INTO songplays
                (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (songplay_id) DO NOTHING;
                """)
    
    user = ("""
            INSERT INTO users
            (user_id, first_name, last_name, gender, level)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (user_id) DO NOTHING;
            """)
    
    song = ("""
            INSERT INTO songs
            (song_id, title, artist_id, year, duration)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (song_id) DO NOTHING;
            """)
    
    artist = ("""
            INSERT INTO artists
            (artist_id, name, location, latitude, longitude)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (artist_id) DO NOTHING;
            """)
    
    time_table_insert = ("""
        INSERT INTO time
        (start_time, hour, day, week, month, year, weekday)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (start_time) DO NOTHING;
                        """)

class select:
    song = ("""
        SELECT song_id, artists.artist_id
        FROM songs JOIN artists ON songs.artist_id = artists.artist_id
        WHERE songs.title = %s
        AND artists.name = %s
        AND songs.duration = %s        
            """)