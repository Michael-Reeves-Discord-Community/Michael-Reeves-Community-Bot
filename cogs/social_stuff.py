import discord
from discord.ext import commands
import os

class Socials(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tweet = open("socialmedia/latest/latesttweet.txt", "r").read()
        self.ytvid = open("socialmedia/latest/latestytvid.txt", "r").read()

    @commands.command()
    async def twitter(self, ctx):
        await ctx.send(self.tweet)

    @commands.command()
    async def youtube(self, ctx):
        await ctx.send(self.ytvid)
