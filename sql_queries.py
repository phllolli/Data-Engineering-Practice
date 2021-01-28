class create_table:
    songplay = ("""
        CREATE TABLE IF NOT EXISTS songplays
        (songplay_id int PRIMARY KEY, 
        start_time date REFERENCES time(start_time), 
        user_id int NOT NULL REFERENCES users(user_id), 
        level text, 
        song_id text REFERENCES songs(song_id), 
        artist_id text REFERENCES artists(artist_id), 
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
        artist_id text NOT NULL REFERENCES artists(artist_id), 
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