import discord
from discord.ext import commands
import os
from cogs.fun import Fun
from cogs.social_stuff import Socials
from cogs.memes import Memes
from cogs.misc import Misc
from dotenv import load_dotenv
from socialmedia.twitter import TwitterBot

# load environment variables from .env
load_dotenv()

bot = commands.Bot(command_prefix="nut_")
bot.remove_command("help")


@bot.event
async def on_ready():
    print("time 2 nut")
    await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name="a game rn", url="https://www.youtube.com/watch?v=DLzxrzFCyOs"))


@bot.event
async def on_command_error(ctx, error):
    if type(error) == discord.ext.commands.errors.CommandNotFound:
        await ctx.send("that is not a valid command gamer. try [prefix]help for a list")
    elif type(error) == discord.ext.commands.errors.CommandOnCooldown:
        await ctx.send(f"you are doing that too fast. you have {error.retry_after} seconds left. precise, huh")
    elif type(error) == discord.ext.commands.errors.CommandInvokeError:
        if type(error.original) == discord.errors.Forbidden:
            await ctx.send("you do not have permissions for this gamer.")
        else:
            await ctx.send(f"some thing wrong. here, deal with it: {error.original}")
    else:
        await ctx.send(error)


bot.add_cog(Fun(bot))
bot.add_cog(Socials(bot))
bot.add_cog(Memes(bot))
bot.add_cog(Misc(bot))

bot.run(os.environ['discord_key'])
