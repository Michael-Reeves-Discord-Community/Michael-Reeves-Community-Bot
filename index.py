import discord
from discord.ext import commands 
import os 
from cogs.fun import Fun

bot = commands.Bot(command_prefix="nut_")

@bot.event
async def on_ready():
	print("time 2 nut")

bot.add_cog(Fun(bot))

bot.run("NzE3MDQyODUwNDc0MQw9w4WgQxX.xZ8_153952483_ph5bfe1f55c3234JO")
