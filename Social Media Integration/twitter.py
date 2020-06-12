import tweepy as tpy #the library that interfaces with the Twitter API

import os


class TwitterBot():
	def __init__(self, akey, asecret, apikey, apisecret, targetUser):
		self.akey = akey
		self.asecret = asecret
		self.apikey = apikey
		self.apisecret = apisecret
		self.api = self.auth()
		self.latestTweet = self.getLatestTweet(targetUser)
		self.saveLatestTweet(self.latestTweet)

	def auth(self):
		try:
			auth = tpy.OauthHandler(self.apikey, self.apisecret)
			auth.set_access_token(self.akey, self.asecret)
			return tpy.API(auth) 
		except TweepError:
			raise ("Check your credentials dumbass. Imagine being such a poo poo") 

	def getLatestTweet(self, user):
		tweet = self.api.user_timeline(id = user, count = 1)[0]
		return tweet.text

	def saveLatestTweet(self, tweet):
		try: os.remove("latesttweet.txt")
		except: pass 
		
		latest_tweet = open("lattesttweet.txt", "w")
		latest_tweet.write(tweet)
		latest_tweet.close()

if __name__ == "__main__":
	tweety = TwitterBot(0, 0, 0, 0, 0)
