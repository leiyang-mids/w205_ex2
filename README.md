# MIDS W205 Exercise 2

### Lei Yang - 2015/12/12

#### Deployment steps:
0. assume streamparse and tweepy are installed and properly configured.
1. under **/setup**, create Postgres database and table:
<pre><code># python create_db.py</code></pre>
2. under **/EX2Tweetwordcount**, start streaming:
<pre><code># sparse run </code></pre>

#### Checking results (under **/serving_scripts**):
- check all words count:
<pre><code># python finalresults.py </code></pre>
- check a specific word:
<pre><code># python finalresults.py google </code></pre>
- check histogram with specified range:
<pre><code># python histogram.py 6000 7000 </code></pre>
