import tweepy

consumer_key = "JNh0r9tmrz2HPX4uLyasCiZxT";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "4RpiILSSTYqD8BdMdBT3gNaSNAN0LBUZcchDVFhfgBRmRsVaYC";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "196317396-54vgG05mWw9TjJGDEj9THuFkUM7EIcl4l1FtwhqL";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "wTN4fJBSAB2x9HRJPe8b6YEqZ6MkvjxZVHeNKC2TWwY7m";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
