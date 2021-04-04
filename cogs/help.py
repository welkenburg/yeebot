import discord
import os
import random
from discord.ext import commands, tasks

class help(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(help='Shows this message')
	async def help(self,ctx,cog=None):
		cogs = self.client.cogs.keys() if cog == None else [cog]
		for each in cogs:
			embed = discord.Embed(title=f"Help {each}",color = discord.Color(random.randint(0, 0xffffff))) if each != 'help' else discord.Embed(title=f"Help",color = discord.Color(random.randint(0, 0xffffff)))
			for command in self.client.get_cog(each).get_commands():
				command_value = f'{self.client.command_prefix}{command.name}'
				for para in command.params:
					if '=' in str(command.params[para]):
						command_value += f' [{para}]'
					elif not para in ["self","ctx"]:
						 command_value += f' <{para}>'
				embed.add_field(name=f"`{command_value}`",value=f"{command.help}",inline=False)
			await ctx.send(embed=embed)



def setup(client):
	client.add_cog(help(client))
