import discord 
from discord.ext import commands 

class Memes(commands.Bot):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def gimme_meme(self, ctx):
		ctx.send("you are a meme")
		#TODO: api.reddit.com/r/subreddit/random returns post

