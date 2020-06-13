import discord
from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        commands = open("cogs/commandlist.txt", "r")
        self.commands = commands.read().split("&&&")
        commands.close()

    @commands.command()
    async def help(self, ctx, page=0):
        if page >= 1 and page <= 3:
            await ctx.send("```\n" + self.commands[page - 1] + "\n```")
        else:
            await ctx.send("```\nHelp page:\n\nDo [prefix]help [page] for more info.\n\nPage 1: phase1_gen, phase2_gen, video_idea, nerdtalk, f\nPage 2: ascii, randascii, asciifont, bigtext\nPage 3: twitter, youtube, meme, help\n```")
