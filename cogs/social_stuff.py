import discord 
from discord.ext import commands
 
class Socials(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.tweet = open("socialmedia/lastest/latesttweet.txt", "r").read()
	
	@commands.command()
	async def twitter(self, ctx):
		await ctx.send(self.tweet)
