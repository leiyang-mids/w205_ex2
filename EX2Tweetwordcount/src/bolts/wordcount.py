from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        #self.redis = StrictRedis()
        # get postgres connection
        self.conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        self.cur = self.conn.cursor()
        # let's sync our counter with the DB, in case there are any records
        self.log('syncing with database ...')
        self.cur.execute('SELECT * FROM Tweetwordcount')
        records = self.cur.fetchall()
        for rec in records:
            self.counts[rec[0]] = int(rec[1])
        self.conn.commit()
        self.log('completed syncing with %d words' %self.cur.rowcount)

    def process(self, tup):
        word = tup.values[0]

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount
        # Table name: Tweetwordcount
        # you need to create both the database and the table in advance.
        if self.counts[word] == 1:
            self.cur.execute("INSERT INTO Tweetwordcount (word, count) VALUES (%s, 1)", (word,))
        else:
            self.cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (self.counts[word], word))
        self.conn.commit()

        # Log the count every 10 counts - just to see the topology running
        if self.counts[word]%100 == 0:
            self.log('%s: %d' %(word, self.counts[word]))
