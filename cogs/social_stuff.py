import discord
from discord.ext import commands
import os
import tweepy as tpy
import time
from dotenv import load_dotenv

load_dotenv()

class Twitter():
    def __init__(self, akey, asecret, apikey, apisecret):
        self.akey = akey
        self.asecret = asecret
        self.apikey = apikey
        self.apisecret = apisecret
        self.api = self.auth()

    def auth(self):
        auth = tpy.OAuthHandler(self.apikey, self.apisecret)
        auth.set_access_token(self.akey, self.asecret)
        return tpy.API(auth)

    def getLatestTweet(self, user = "michaelreeves"):
        tweet = self.api.user_timeline(id=user, count=1)[0]
        return tweet.text

class Youtube():
    pass

class Socials(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Twitter = Twitter(os.environ['tweet_access_key'], os.environ['tweet_access_secret'], os.environ['tweet_api_key'], os.environ['tweet_api_secret'])
        self.ytvid = open("socialmedia/latest/latestytvid.txt", "r").read()

    @commands.command(aliases=["tweet"])
    async def twitter(self, ctx):
        self.tweet = self.Twitter.getLatestTweet()
        await ctx.send(self.tweet)

    @commands.command(aliases=["video", "ytvid"])
    async def youtube(self, ctx):
        print("hi")
        await ctx.send(self.ytvid)
