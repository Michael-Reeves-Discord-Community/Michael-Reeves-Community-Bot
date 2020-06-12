import discord 
from discord.ext import commands
import random, pyfiglet, time
from pyfiglet import Figlet, fonts 
from cogs.utils.gendata import *
 #made it so u can import a json file and use it  ezer o nice
 
class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.phase1, self.phase2, self.videoideas = get_phase_1(), get_phase_2(), get_video_ideas()
	
	@commands.command()
	async def phase1_gen(self, ctx, *, num = 1):
		temp_str = ""
		for i in range(min(int(num), 100)):
			temp_str += random.choice(self.phase1) + " "
		await ctx.send(temp_str[:2000])

	@commands.command()
	async def phase2_gen(self, ctx, *, num = 1):
		temp_str = ""
		for i in range(min(int(num), 100)):
			temp_str += random.choice(self.phase2) + " "
		await ctx.send(temp_str[:2000])

	@commands.command()
	async def video_idea(self, ctx, *, num = 1):
		for i in range(min(10, num)):
			temp_str = random.choice(self.videoideas)
			await ctx.send(temp_str[:2000])
			time.sleep(1)

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
					if count < len(txt_ls) and len(temp_chars + "   " + txt_ls[count]) <= 75:
						temp_chars += "   " + txt_ls[count]
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
			try:
				to_send = ("```" + pyfiglet.figlet_format(item))[:1996] + "```"
				await ctx.send(to_send)
			except NotImplementedError:
				await ctx.send("Ascii module isn't working rn. deal with it please, thanks -devs")
			time.sleep(0.8)
