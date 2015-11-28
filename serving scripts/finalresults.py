import sys

arg = sys.argv
arg.pop(0)

if len(arg) > 1:
    sys.exit('accept at most 1 variable.')

no_count = 'for you the are this have not but that your get from and just they who can what about out any when now all was don\'t i\'m how she could with it\'s you\'re can\'t'.split()
if len(arg) == 1 and (len(arg[0]) < 3 or arg[0] in no_count):
    print 'words below, or with 1 or 2 characters are not counted, please try another one, like \'happy\''
    print no_count
    sys.exit()

import psycopg2
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

if len(arg) == 1:
    cur.execute('select count from tweetwordcount where word = %s', (arg[0].lower(),))
    #print 'run: ' + cur.query
    rtn = cur.fetchone()
    print 'Total number of occurrences of "%s": %s' %(arg[0].lower(), '0' if not rtn else str(rtn[0]))

if len(arg) == 0:
    cur.execute('select * from Tweetwordcount order by word')
    words = cur.fetchall()
    for word in words:
        print '(%s, %s)' %(word[0], word[1])

cur.close()
conn.close()
