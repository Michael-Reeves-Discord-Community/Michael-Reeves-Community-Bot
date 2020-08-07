import discord
from discord.ext import commands
import random
import pyfiglet
import time
import requests
import json
import os

from cogs.utils.gendata import *
from pyfiglet import Figlet, FigletFont, FontNotFound
from cogs.utils import crack


def render_text(text, delims=None, *, escape=True, shorten_by=8, page_length=2000):
    if delims is None:
        delims = ["\n"]
    in_text = text
    if escape:
        num_mentions = text.count("@here") + text.count("@everyone")
        shorten_by += num_mentions
    page_length -= shorten_by
    while len(in_text) > page_length:
        closest_delim = max([in_text.rfind(d, 0, page_length) for d in delims])
        closest_delim = closest_delim if closest_delim != -1 else page_length
        to_send = in_text[:closest_delim]
        yield to_send
        in_text = in_text[closest_delim:]
    yield in_text


async def render_ascii(ctx, text, language="", font=None, org_txt=None):
    if font:
        ascii_font = f"\n[ Font :: {font} ]"
    else:
        ascii_font = ""
    if org_txt:
        org_text_box = f"[ Text :: {org_txt} ]"
    else:
        org_text_box = ""
    ret = f"```{language}\n{text}```"
    await ctx.send(ret)


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.phase1, self.phase2, self.videoideas = get_phase_1(), get_phase_2(), get_video_ideas()

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def phase1_gen(self, ctx, *, num=1):
        temp_str = ""
        for i in range(min(int(num), 100)):
            temp_str += random.choice(self.phase1) + " "
        await ctx.send(temp_str[:2000])

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def phase2_gen(self, ctx, *, num=1):
        temp_str = ""
        for i in range(min(int(num), 100)):
            temp_str += random.choice(self.phase2) + " "
        await ctx.send(temp_str[:2000])

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def video_idea(self, ctx, *, num=1):
        for i in range(min(10, num)):
            temp_str = random.choice(self.videoideas)
            await ctx.send(temp_str[:2000])
            time.sleep(1)

    @commands.command(aliases=["ascii_2"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def randascii(self, ctx, *, text: commands.clean_content):
        if len(text) > 30:
            return await ctx.send(
                f"**{ctx.author.name},** unfortunately to prevent spam, "
                f"the limit is **30** characters.\nSo you can only you use this part of the "
                f"sentence you tried: `{text[:30]}`"
            )
        random_font = crack.insta_crack(
            stuff=True, things=FigletFont.getFonts())
        font = Figlet(font=random_font)
        out = font.renderText(text)
        for txt in render_text(out, shorten_by=30):
            async with ctx.channel.typing():
                await render_ascii(ctx, text=txt, font=random_font, org_txt=text)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def asciifont(self, ctx, text, font):
        if len(text) > 30:
            return await ctx.send(
                f"**{ctx.author.name},** unfortunately to prevent spam, "
                "the limit is **30** characters.\nSo you can only you use this part of "
                f"the sentence  {text[:30]}"
            )
        try:
            chosen_font = Figlet(font=font)
        except FontNotFound:
            return await ctx.send(
                f"**{ctx.author}**, \nFont :: **{font}** not found, "
            )
        out = chosen_font.renderText(text)
        for txt in render_text(out, shorten_by=30):
            async with ctx.channel.typing():
                await render_ascii(ctx, text=txt, font=font, org_txt=text)

    @commands.command(aliases=["big"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bigtext(self, ctx, *, text):
        if len(text) > 36:
            return await ctx.send(
                f"**{ctx.author.name},** unfortunately to prevent spam, "
                "the limit is **36** characters.\nSo you can only you use this part of "
                f"the sentence  {text[:36]}"
            )
        font = Figlet(font='big')
        out = font.renderText(text)
        for txt in render_text(out, shorten_by=30):
            async with ctx.channel.typing():
                await render_ascii(ctx, text=txt, language="fix", org_txt=text)

    @commands.command(aliases=["ascii_1"])
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def ascii(self, ctx, *, txt="Specify words please"):
        infostr = f"Text from {ctx.author} Message"
        txt_ls = txt.split(" ")
        next_ls = []
        count = 0
        while 1:
            if not txt_ls:
                break
            count = 0
            temp_chars = txt_ls[0]
            while 1:
                count += 1
                if count <= len(txt_ls):
                    if count < len(txt_ls) and len(temp_chars + "   " + txt_ls[count]) <= 70:
                        temp_chars += "   " + txt_ls[count]
                    else:
                        for i in range(count):
                            txt_ls.pop(0)
                        next_ls.append(temp_chars)
                        break
                else:
                    txt_ls.pop(0)
                    next_ls.append(temp_chars)
                    break
        for i in range(0, len(next_ls)):
            to_send = ("```" + pyfiglet.figlet_format(next_ls[i]))[:1940] + f"\n{infostr} {i + 1} of {len(next_ls)}```"
            await ctx.send(to_send)
            time.sleep(1.2)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def nerdtalk(self, ctx, *, cmd="not_language bruh"):
        language = cmd[:cmd.find(" ")].lower()
        text = cmd[(cmd.find(" ") + 1):]

        if language == "c#" or language == "cs":
            out_str = "using System;\n\nnamespace csharp\n{\n\tclass Nut\n\t{\n\t\tstatic void Main(string[] args)\n\t\t{\n\t\t\tConsole.WriteLine(\"" + \
                      text + "\");\n\t\t}\n\t}\n}"
        elif language == "java":
            out_str = "package java.nut;\n\npublic class Nut {\n\tpublic static void main(string[] args) {\n\t\tSystem.out.println(\"" + \
                      text + "\");\n\t}\n}"
        elif language == "python" or language == "py" or language == "r":
            out_str = "print(" + text + ")\n"
        elif language == "c++":
            out_str = "#include <iostream>\n\nint main()\n{\n\tstd::cout<<\"" + \
                      text + "\";\n\treturn 0;\n}"
        elif language == "c":
            out_str = "#include <stdio.h>\nint main() {\n\tprintf(\"" + \
                      text + "\");\n\treturn 0;\n}"
        elif language == "not_language":
            out_str = "usage: [prefix]nerdtalk [language] [message]"
        else:
            out_str = "your hecking language hasn't been implemented yet because the devs are too lazy. here's the text: " + text
        await ctx.send("```" + language + "\n" + out_str + "\n```")

    @commands.command()
    @commands.cooldown(1, 7, commands.BucketType.user)
    async def f(self, ctx):
        await ctx.send("Somebody has sent a ***___MASSIVE F IN THE CHAT___***.")
        await ctx.send("```" + pyfiglet.figlet_format("f") + "```")
        await ctx.send(":regional_indicator_f:")

    @commands.command(aliases=["rona", "cases", "covid"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def corona(self, ctx):
        await ctx.send(
            "lmao corona cases rn be goin: " + str(requests.request("GET", "https://api.thevirustracker.com/free-api?global=stats", headers={}, data={}).json()["results"][0]["total_cases"]))
