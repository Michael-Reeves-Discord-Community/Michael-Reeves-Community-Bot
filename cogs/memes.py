import discord
import json
from discord.ext import commands
import aiohttp


class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['dmeme', 'memes'])
    @commands.cooldown(rate=5, per=5, type=commands.BucketType.user)
    async def meme(self, ctx, *, sub="michaelreeves"):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.reddit.com/r/{}/random".format(sub)) as r:
                    r = await r.json()
                    upvotes = r[0]["data"]["children"][0]["data"]["ups"]
                    reddit = r[0]["data"]["children"][0]["data"]["subreddit_name_prefixed"]
                    e = discord.Embed(title=f'**{r[0]["data"]["children"][0]["data"]["title"]}**',
                                    url=f'https://www.reddit.com{r[0]["data"]["children"][0]["data"]["permalink"]}')
                    e.set_image(url=r[0]["data"]["children"][0]["data"]["url"])
                    e.set_footer(
                        text=f"👍 {upvotes:,d} | From: {reddit} | {ctx.author}")
                    await ctx.send(embed=e)
        except KeyError:
            await ctx.send("your sub is rong. try that again dum")
