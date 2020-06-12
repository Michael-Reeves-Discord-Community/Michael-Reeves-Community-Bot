import discord 
from discord.ext import commands
import random, pyfiglet, time
from pyfiglet import Figlet, FigletFonts, FontNotFound 


class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def phase1_gen(self, ctx, *, num = 1):
		file = open("cogs/res/phase1.txt", "r")
		data = file.read().split(" ")
		temp_str = ""
		for i in range(int(num)):
			temp_str += random.choice(data) + " "
		file.close()
		await ctx.send(temp_str[:2000])

	@commands.command()
	async def phase2_gen(self, ctx, *, num = 1):
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

	@commands.command()
	async def ascii(self, ctx, *, txt = "Specify words please"):
		txt_ls = txt.split(" ")
		next_ls = []
		count = 0
		while 1:
			if txt_ls == []:
				break
			count = 0
			temp_chars = txt_ls[0]
			while 1:
				count += 1
				if count <= len(txt_ls):
					if count < len(txt_ls) and len(temp_chars + " " + txt_ls[count]) <= 75:
						temp_chars += " " + txt_ls[count]
					else:
						for i in range(count):
							txt_ls.pop(0)
						next_ls.append(temp_chars)
						break
				else: #brb 
					txt_ls.pop(0) 
					next_ls.append(temp_chars)
					break
		for item in next_ls:
			to_send = ("```" + pyfiglet.figlet_format(item))[:1996] + "```"
			await ctx.send(to_send)
			time.sleep(0.8)
