import psycopg2
import sql_queries
pswd = open('password.txt', 'r').read()

def create_db(dbname):
    conn = psycopg2.connect(
        database='postgres', user='postgres', password=pswd, host='127.0.0.1', port='5432'
    )
    conn.autocommit = True
    cur = conn.cursor()
    
    cur.execute('DROP DATABASE IF EXISTS {name}'.format(name = dbname))
    cur.execute('CREATE DATABASE {name}'.format(name = dbname))
    
    print("Database named {name} created successfully........".format(name = dbname))

    conn.close()
    
    conn = psycopg2.connect(
        database='mydb', user='postgres', password=pswd, host='127.0.0.1', port='5432'
    )
    
    cur = conn.cursor()
    
    return cur, conn

def create_tables(cur, conn):
    for query in sql_queries.create_table.all:
        cur.execute(query)
        conn.commit()
        
def drop_table(cur, conn):
    for query in sql_queries.drop_table.all:
        cur.execute(query)
        conn.commit()

def main():
    cur, conn = create_db('mydb')
    drop_table(cur, conn)
    create_tables(cur, conn)
    conn.close()

if __name__ == '__main__':
    main()