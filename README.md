# MIDS W205 Exercise 2

### Lei Yang - 2015/12/12

#### System Requirements:
1. Python libraries streamparse, tweepy, and psycopg2 are installed and properly configured.
2. Postgres is running with postgres user.

#### Deployment steps:
0. as w205, checkout repo:
<pre><code>$ git clone git@github.com:leiyang-mids/w205_ex2.git </code></pre>
1. as w205, under **/setup**, create Postgres database and table:
<pre><code>$ python create_db.py</code></pre>
2. bash screen should show:
<pre><code>
[w205@ip-172-31-6-39 setup]$ python create_db.py
creating tcount database in postgres ...
database tcount is successfully created!
creating tweetwordcount table in tcount ...
table tweetwordcount is successfully created!
postgres setup completed, you are good to go, happy streaming :)
</code></pre>
3. as w205, under **/EX2Tweetwordcount**, start streaming:
<pre><code>$ sparse run </code></pre>
 - note: to avoid log flood, we only log count every 100 counts for each word, it could be several seconds before you see the first count shows up
 - e.g. 37262 [Thread-41] INFO  backtype.storm.task.ShellBolt - ShellLog pid:4265, name:count-bolt weather: 100
4. to stop streaming, press <code>Ctrl+C</code> at any time.

#### Checking results (under **/serving_scripts**):
- check all words count:
<pre><code>$ python finalresults.py </code><pre>
- check a specific word:
<pre><code>$ python finalresults.py weather </code><pre>
- check histogram with specified range:
<pre><code>$ python histogram.py 600 1000 </code><pre>
- perform customized query on Postgres:
<pre><code>
$ [w205@ip-172-31-6-39 ~]$ psql -U postgres
psql (8.4.20)
Type "help" for help.
postgres=# \\c tcount
psql (8.4.20)
You are now connected to database "tcount".
tcount=# select * from tweetwordcount order by count desc limit 20
tcount-# ;
  word   | count
---------+-------
 like    |   700
 one     |   610
 love    |   524
 will    |   443
 amp     |   430
 know    |   421
 want    |   390
 weather |   370
 see     |   360
 time    |   340
 people  |   331
 good    |   330
 make    |   310
 new     |   309
 thank   |   308
 day     |   282
 much    |   282
 need    |   277
 back    |   274
 really  |   270
(20 rows)
</code><pre>
