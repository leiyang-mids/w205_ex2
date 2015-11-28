import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# create tcount database
conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
# TODO: add cleanup step - drop first if exist
cur.execute('drop database tcount')
conn.commit()
# create anew
cur.execute("create database tcount")
conn.commit()
cur.close()
conn.close()
print 'database tcount is successfully created!'

# create table in Tcount
# connect to database and create table & column
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

#Create tweetwordcount table
cur = conn.cursor()
cur.execute('''CREATE TABLE Tweetwordcount
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);''')
conn.commit()
conn.close()
print 'table tweetwordcount is successfully created!'
