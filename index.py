import discord
from discord.ext import commands 
import os 


bot = commands.Bot(command_prefix="nut")

@bot.event
async def on_ready():
    print("time 2 nut")




for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

bot.run("nice try buddy ur not getting the token ha ")



