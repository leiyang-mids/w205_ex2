import sys

arg = sys.argv

if len(arg) > 1:
    print 'accept at most 1 variable.'
    return

no_count = 'for you the are this have not but that your get from and just they who can what about out any when now all was don\'t i\'m how she could with it\'s you\'re can\'t'.split()
if len(arg) == 1 and (len(arg[0]) < 3 or arg[0] in no_count):
    print 'words below, or with 1 or 2 characters are not counted, please try another one, like \'happy\''
    print no_count
    return

import psycopg2
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

if len(arg) == 1:
    cur.execute('select count from tweetwordcount where word = %s', (arg[0],))
    print 'run: ' + cur.query 
    rtn = cur.fetchone()
    print 'Total number of occurences of “%s”: %s' %(arg[0], '0' if not rtn else str(rtn[0]))

if len(arg) == 0:
    cur.execute('select * from Tweetwordcount order by word limit 15')
    words = cur.fetchall()
    for word in words:
        print '(%s, %s)' %(word[0], word[1])

cur.close()
conn.close()
