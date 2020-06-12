import discord 
from discord.ext import commands
import random, pyfiglet, time

class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def phase1_gen(self, ctx, *, num = 1):
		# print("DEBUG:: PHASE 1 TRIGGERED BOIZ")
		file = open("cogs/res/phase1.txt", "r")
		data = file.read().split(" ")
		temp_str = ""
		for i in range(int(num)):
			temp_str += random.choice(data) + " "
		file.close()
		await ctx.send(temp_str[:2000])

	@commands.command()
	async def phase2_gen(self, ctx, *, num = 1):
		# print("DEBUG:: PHASE 2 TRIGGERED BOIZ")
		file = open("cogs/res/phase2.txt", "r")
		data = file.read().split(" ")
		temp_str = ""
		for i in range(int(num)):
			temp_str += random.choice(data) + " "
		file.close()
		await ctx.send(temp_str[:2000])

	@commands.command()
	async def ascii(self, ctx, *, txt = "Specify words please"):
		# print("DEBUG:: ASCII TRIGGERED BOIZ")
		if len(txt) < 50:
			await ctx.send(("```" + pyfiglet.figlet_format(txt))[:1996] + "```")
		else:
			await ctx.send("Message too long. Please use long_ascii")
		# print(pyfiglet.figlet_format(txt))

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
	async def long_ascii(self, ctx, *, txt = "Specify words please"):
		txt_ls = txt.split(" ")
		next_ls = []
		count = 0
		while txt_ls:
			if len(txt_ls) > 6: # if there's available list items
				it = (txt_ls[0], txt_ls[1], txt_ls[2], txt_ls[3], txt_ls[4], txt_ls[5]) #iterates through 6...1 words and sees whether they are combinable to fit 2k char limit
				if len(txt_ls[0] + txt_ls[1] + txt_ls[2] + txt_ls[3] + txt_ls[4] + txt_ls[5]) < 33: # 6 word cap: 33 char
					next_ls.append(txt_ls[0] + "  " + txt_ls[1] + "  " + txt_ls[2] + "  " + txt_ls[3] + "  " + txt_ls[4] + "  " + txt_ls[5])
					txt_ls.pop(5)
					txt_ls.pop(4)
					txt_ls.pop(3)
					txt_ls.pop(2)
					txt_ls.pop(1)
					txt_ls.pop(0)
				elif len(txt_ls[0] + txt_ls[1] + txt_ls[2] + txt_ls[3] + txt_ls[4]) < 35: # 5 word cap: 35 char
					next_ls.append(txt_ls[0] + "  " + txt_ls[1] + "  " + txt_ls[2] + "  " + txt_ls[3] + "  " + txt_ls[4])
					txt_ls.pop(4)
					txt_ls.pop(3)
					txt_ls.pop(2)
					txt_ls.pop(1)
					txt_ls.pop(0)
				elif len(txt_ls[0] + txt_ls[1] + txt_ls[2] + txt_ls[3]) < 37: # 4 word cap: 37 char
					next_ls.append(txt_ls[0] + "  " + txt_ls[1] + "  " + txt_ls[2] + "  " + txt_ls[3])
					txt_ls.pop(3)
					txt_ls.pop(2)
					txt_ls.pop(1)
					txt_ls.pop(0)
				elif len(txt_ls[0] + txt_ls[1] + txt_ls[2]) < 39: # 3 word cap: 39 char
					next_ls.append(txt_ls[0] + "  " + txt_ls[1] + "  " + txt_ls[2])
					txt_ls.pop(2)
					txt_ls.pop(1)
					txt_ls.pop(0)
				elif len(it[0] + it[1]) < 41: # 2 word cap: 41 char
					next_ls.append(it[0] + "  " + it[1])
					txt_ls.pop(1)
					txt_ls.pop(0)
				else: # returns single words 41 chars or longer
					next_ls.append(it[0])
					txt_ls.pop(0)
			else: # final six words
				fin_str = ""
				for item in txt_ls: # combines remaining items into string
					fin_str += item + " "
				if len(fin_str) < 50: # if all words are fittable into one box
					next_ls.append(fin_str)
					txt_ls = []
				elif len(fin_str) < 80: # checks for intermediary breakpoint
					ind = fin_str.find(" ", 20)
					if ind != -1: # if intermediary space is available in the first third 
						ind2 = fin_str.find(" ", ind) # program tries to find another space
						if ind2 != -1: # if both seperators are clear, then split into three blocks
							next_ls.append(fin_str[:ind])
							next_ls.append(fin_str[ind:ind2])
							next_ls.append(fin_str[ind2:])
							txt_ls = []
						else:
							if ind > 30: # if first seperator is sufficient to fit 2k char, program passes
								next_ls.append(fin_str[:ind])
								next_ls.append(fin_str[ind:])
							else: # if all else fails, put one word into each box to fit char limits
								for i in txt_ls:
									next_ls.append(i)
									txt_ls = []
					else:
						for i in txt_ls:
							next_ls.append(i)
							txt_ls = []	
				else:
					for i in txt_ls:
						next_ls.append(i)
					txt_ls = []
		for item in next_ls:
			to_send = ("```" + pyfiglet.figlet_format(item))[:1996] + "```"
			await ctx.send(to_send)
			time.sleep(0.8)
