import tweepy as tpy #the library that interfaces with the Twitter API
import os
import time


class TwitterBot():
    def __init__(self, akey, asecret, apikey, apisecret):
        self.akey = akey
        self.asecret = asecret
        self.apikey = apikey
        self.apisecret = apisecret
        self.api = self.auth()
        # self.user = targetUser
        # self.latestTweet = self.getLatestTweet(targetUser)
        # self.saveLatestTweet(self.latestTweet)

    def auth(self):
        auth = tpy.OAuthHandler(self.apikey, self.apisecret)
        auth.set_access_token(self.akey, self.asecret)
        return tpy.API(auth)

    def getLatestTweet(self, user):
        tweet = self.api.user_timeline(id = user, count = 1)[0]
        return tweet.text

    def saveLatestTweet(self, tweet):
        try: os.remove("latest/latesttweet.txt")
        except: pass

        latest_tweet = open("latest/latesttweet.txt", "w")
        latest_tweet.write(tweet)
        latest_tweet.close()

    def waitInBetween(self, time):
        time.sleep(time)

if __name__ == "__main__":
    tweety = TwitterBot("", "", "", "", "michaelreeves")
