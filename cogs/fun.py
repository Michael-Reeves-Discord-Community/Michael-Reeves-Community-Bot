import discord 
from discord.ext import commands
import random, pyfiglet, time

class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def phase1_gen(self, ctx, *, num):
		# print("DEBUG:: PHASE 1 TRIGGERED BOIZ")
		file = open("cogs/res/phase1.txt", "r")
		data = file.read().split(" ")
		temp_str = ""
		for i in range(int(num)):
			temp_str += random.choice(data) + " "
		file.close()
		await ctx.send(temp_str[:2000])

	@commands.command()
	async def phase2_gen(self, ctx, *, num):
		# print("DEBUG:: PHASE 2 TRIGGERED BOIZ")
		file = open("cogs/res/phase2.txt", "r")
		data = file.read().split(" ")
		temp_str = ""
		for i in range(int(num)):
			temp_str += random.choice(data) + " "
		file.close()
		await ctx.send(temp_str[:2000])

    	@commands.command()
	async def video_idea(self, ctx, *, num = 1):
		# print("DEBUG:: VIDEO IDEA TRIGGERED BOIZ")
		file = open("cogs/res/thinktank.txt", "r")
		data = file.read().split("\n")
		for i in range(0, min(10, num)):
			temp_str = random.choice(data)
			await ctx.send(temp_str[:2000])
			time.sleep(1)
		file.close()

