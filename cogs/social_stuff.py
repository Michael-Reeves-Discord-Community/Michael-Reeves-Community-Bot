import discord 
from discord.ext import commands
 
class Socials(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.tweet = open("")
	
	@commands.command()
	async def twitter(self, ctx):
		await ctx.send(self.tweet)
