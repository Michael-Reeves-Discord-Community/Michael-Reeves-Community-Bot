import discord
from discord.ext import commands
import os
from cogs.fun import Fun
from cogs.social_stuff import Socials
from cogs.memes import Memes
from dotenv import load_dotenv
from socialmedia.twitter import TwitterBot

# load environment variables from .env
load_dotenv()

bot = commands.Bot(command_prefix="nut_")

# ben was here
#lmao what is this codebase
# i too code python

@bot.event
async def on_ready():
    print("time 2 nut")

bot.add_cog(Fun(bot))
bot.add_cog(Socials(bot))
bot.add_cog(Memes(bot))

bot.run(os.environ['discord_key'])

