from __future__ import absolute_import, print_function, unicode_literals

import re
from streamparse.bolt import Bolt

################################################################################
# Function to check if the string contains only ascii chars
################################################################################
def ascii_string(s):
  return all(ord(c) < 128 for c in s)

class ParseTweet(Bolt):

    def process(self, tup):
        tweet = tup.values[0]  # extract the tweet

        # words of no interests - will not count
        # we also don't count words with 1 or 2 characters
        no_count = 'for you the are this have not but that your get from and just they who can what about out any when now all was don\'t i\'m how she could with'.split()

        # get rid numbers
        tweet = re.sub(r'\w*\d\w*', '', tweet).strip()

        # Split the tweet into words and convert all to lower case
        words = tweet.lower().split()

        # Filter out the hash tags, RT, @ and urls
        valid_words = []
        for word in words:

            # Filter the hash tags
            if word.startswith("#"): continue

            # Filter the user mentions
            if word.startswith("@"): continue

            # Filter out retweet tags
            if word.startswith("rt"): continue

            # Filter out the urls
            if word.startswith("http"): continue

            # Strip leading and lagging punctuations
            aword = word.strip("\"?><,'.:;!-~[]()&%$*/\\")

            # Filter out words of no interests
            if aword in no_count: continue

            # now check if the word contains only ascii
            if len(aword) > 2 and ascii_string(word):
                valid_words.append([aword])

        if not valid_words: return

        # Emit all the words
        self.emit_many(valid_words)

        # tuple acknowledgement is handled automatically
