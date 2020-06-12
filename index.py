import discord
from discord.ext import commands 
import os 
from cogs.fun import Fun

print("i am ehre")
bot = commands.Bot(command_prefix="nut_")

@bot.event
async def on_ready():
	print("time 2 nut")


print("here lmao")

bot.add_cog(Fun(bot))

bot.run("funni")



