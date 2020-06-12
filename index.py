import discord
from discord.ext import commands 
import os 
from cogs.fun import Fun
from cogs.social_stuff import Socials
from cogs.memes import Memes

bot = commands.Bot(command_prefix="nut_")

@bot.event
async def on_ready():
	print("time 2 nut")

for module in (Fun(bot), Socials(bot), Memes(bot)):
	bot.add_cog(module)


bot.run("dab")
