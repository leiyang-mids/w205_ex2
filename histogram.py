import sys

arg = sys.argv
arg.pop(0)

if len(arg) != 2:
    sys.exit('only take two parameters as input')

try:
    k1 = int(arg[0])
    k2 = int(arg[0])
except ValueError:
    sys.exit('invalid input - only accept integer')

if k1 > k2:
    sys.exit('invalid interval!')

import psycopg2
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
cur.execute('select word, count from tweetwordcount where count >= %s and count <= %s', (k1, k2))
records = cur.fetchall()
for word in records:
    print '    %s: %d' %(word[0], word[1])
