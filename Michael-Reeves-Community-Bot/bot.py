import discord
from discord.ext import commands
import random
import pyfiglet

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("nut")

@client.command()
async def phase1_gen(ctx, *, num):
    print("DEBUG:: PHASE 1 TRIGGERED BOIZ")
    file = open("phasegenshit/sortedphase1.txt", "r")
    data = file.read().split(" ")
    temp_str = ""
    for i in range(int(num)):
        temp_str += random.choice(data) + " "
    file.close()
    await ctx.send(temp_str[:2000])

@client.command()
async def phase2_gen(ctx, *, num):
    print("DEBUG:: PHASE 2 TRIGGERED BOIZ")
    file = open("phasegenshit/sortedphase2.txt", "r")
    data = file.read().split(" ")
    temp_str = ""
    for i in range(int(num)):
        temp_str += random.choice(data) + " "
    file.close()
    await ctx.send(temp_str[:2000])

@client.command()
async def ascii(ctx, *, txt):
    print("DEBUG:: ASCII TRIGGERED BOIZ")
    await ctx.send("```" + pyfiglet.figlet_format(txt) + "```")
    print(pyfiglet.figlet_format(txt))

@client.command()
async def video_idea(ctx):
    print("DEBUG:: VIDEO IDEA TRIGGERED BOIZ")
    file = open("phasegenshit/videoideas.txt", "r")
    data = file.read().split("\n")
    temp_str = random.choice(data)
    await ctx.send(temp_str[:2000])
    file.close()
    

client.run("NzE3MDQyODUwNDc0MjI5Nzkw.XuJ0vQ.4bxSrTU3kR6PLn3bxAFUhrfJZwU")
