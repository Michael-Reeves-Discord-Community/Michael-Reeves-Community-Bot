import discord 
from discord.ext import commands
 
class Socials(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.tweet = "tweets don't work yet. darn. michael's last tweet was something about turtles hahhahhaa"
	
	@commands.command()
	async def twitter(self, ctx):
		await ctx.send(self.tweet)
