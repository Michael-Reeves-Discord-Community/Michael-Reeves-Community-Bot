import discord
from discord.ext import commands 
import os 
from cogs.fun import Fun

print("i am ehre")
bot = commands.Bot(command_prefix="nut_")

@bot.event
async def on_ready():
	print("time 2 nut")


print("here lmao")

# for filename in os.listdir('./cogs'):
# 	if filename.endswith('.py'):
# 		print("\n", filename[:-3], "\n")
# 		try:
# 			bot.load_extension(f'cogs.{filename[:-3]}')
# 		except discord.ext.commands.errors.NoEntryPointError: pass
# using cogs rather than extensions

bot.add_cog(Fun(bot))

bot.run("NzE3MDQyODUwNDc0MjI5Nzkw.XuKRYg.WTYLO8jLorgxkYHcNYTT2yigTWA")



