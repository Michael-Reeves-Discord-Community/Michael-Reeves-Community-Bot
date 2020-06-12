import discord
from discord.ext import commands 
import os 
from cogs.fun import Fun
from cogs.social_stuff import Socials

bot = commands.Bot(command_prefix="nut_")

@bot.event
async def on_ready():
	print("time 2 nut")

bot.add_cog(Fun(bot))
bot.add_cog(Socials(bot))

bot.run("dab")
