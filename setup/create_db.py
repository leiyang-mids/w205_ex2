import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# create tcount database
print 'creating tcount database in postgres ...'
conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
# cleanup step - drop first if exists
cur.execute('DROP DATABASE IF EXISTS tcount')
conn.commit()
# create anew
cur.execute("CREATE DATABASE tcount")
conn.commit()
cur.close()
conn.close()
print 'database tcount is successfully created in Postgres!'

# connect to tcount database and create table & column
print 'creating tweetwordcount table in tcount ...'
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
cur.execute('''CREATE TABLE Tweetwordcount
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);''')
conn.commit()
conn.close()
print 'table tweetwordcount is successfully created!'
print 'Postgres setup completed, you are good to go, happy streaming :)'
