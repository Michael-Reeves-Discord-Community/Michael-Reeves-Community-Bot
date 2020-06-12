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
	async def ascii(self, ctx, *, txt):
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
	async def long_ascii(self, ctx, *, txt):
		txt_ls = txt.split(" ")
		next_ls = []
		count = 0
		while txt_ls:
			if len(txt_ls) > 6:
				it = (txt_ls[0], txt_ls[1], txt_ls[2], txt_ls[3], txt_ls[4], txt_ls[5])
				if len(txt_ls[0] + txt_ls[1] + txt_ls[2] + txt_ls[3] + txt_ls[4] + txt_ls[5]) < 33:
					next_ls.append(txt_ls[0] + "  " + txt_ls[1] + "  " + txt_ls[2] + "  " + txt_ls[3] + "  " + txt_ls[4] + "  " + txt_ls[5])
					txt_ls.pop(5)
					txt_ls.pop(4)
					txt_ls.pop(3)
					txt_ls.pop(2)
					txt_ls.pop(1)
					txt_ls.pop(0)
				elif len(txt_ls[0] + txt_ls[1] + txt_ls[2] + txt_ls[3] + txt_ls[4]) < 35:
					next_ls.append(txt_ls[0] + "  " + txt_ls[1] + "  " + txt_ls[2] + "  " + txt_ls[3] + "  " + txt_ls[4])
					txt_ls.pop(4)
					txt_ls.pop(3)
					txt_ls.pop(2)
					txt_ls.pop(1)
					txt_ls.pop(0)
				elif len(txt_ls[0] + txt_ls[1] + txt_ls[2] + txt_ls[3]) < 37:
					next_ls.append(txt_ls[0] + "  " + txt_ls[1] + "  " + txt_ls[2] + "  " + txt_ls[3])
					txt_ls.pop(3)
					txt_ls.pop(2)
					txt_ls.pop(1)
					txt_ls.pop(0)
				elif len(txt_ls[0] + txt_ls[1] + txt_ls[2]) < 39:
					next_ls.append(txt_ls[0] + "  " + txt_ls[1] + "  " + txt_ls[2])
					txt_ls.pop(2)
					txt_ls.pop(1)
					txt_ls.pop(0)
				elif len(it[0] + it[1]) < 41:
					next_ls.append(it[0] + "  " + it[1])
					txt_ls.pop(1)
					txt_ls.pop(0)
				else:
					next_ls.append(it[0])
					txt_ls.pop(0)
			else:
				fin_str = ""
				for item in txt_ls:
					fin_str += item + " "
				if len(fin_str) < 40:
					next_ls.append(fin_str)
					txt_ls = []
				elif len(fin_str) < 80:
					ind = fin_str.find(" ", 20)
					if ind != -1:
						ind2 = fin_str.find(" ", ind)
						if ind2 != -1:
							next_ls.append(fin_str[:ind])
							next_ls.append(fin_str[ind:ind2])
							next_ls.append(fin_str[ind2:])
							txt_ls = []
						else:
							if ind > 30:
								next_ls.append(fin_str[:ind])
								next_ls.append(fin_str[ind:])
							else:
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
		lenlen_list = []
		for item in next_ls:
			to_send = ("```" + pyfiglet.figlet_format(item))[:1996] + "```"
			lenlen_list.append(len(to_send))
			await ctx.send(to_send)
			time.sleep(0.5)
		print(lenlen_list)
