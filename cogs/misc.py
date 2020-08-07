import discord
from discord.ext import commands
from discord.ext.commands import has_permissions


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        commands = open("cogs/commandlist.txt", "r")
        self.commands = commands.read().split("&&&")
        commands.close()

    @commands.command()
    async def help(self, ctx, page=0):
        if 1 <= page <= 3:
            await ctx.send("```\n" + self.commands[page - 1] + "\n```")
        else:
            await ctx.send("```\nHelp page:\n\nDo [prefix]help [page] for more info.\n\nPage 1: phase1_gen, phase2_gen, video_idea, nerdtalk, f\nPage 2: ascii, randascii, asciifont, "
                           "bigtext, nick, [admin] nick_someone_else\nPage 3: twitter, youtube, meme, corona, help\n```")

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def nick(self, ctx, *, nick=None):
        if nick is not None:
            await ctx.author.edit(nick=nick)
        else:
            await ctx.author.edit(nick=ctx.author.name)

    @commands.command()
    @has_permissions(administrator=True)
    async def nick_someone_else(self, ctx, member: discord.Member, nick):
        await member.edit(nick=nick)
