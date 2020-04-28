import discord
import requests
import os
import random
from discord.ext import commands, tasks

class commands(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def s(self, ctx, *,arg):
		for filename in os.listdir(f'./assets/{ctx.guild.id}'):
			splited = filename.split('.')
			if arg == f'{splited[:-1][0]}':
				await ctx.channel.purge(limit=1)
				await ctx.send(f'{ctx.author.mention}',file=discord.File(f'assets/{ctx.guild.id}/{filename}'))
				break

	@commands.command(name='add-img')
	async def add_img(self,ctx,name,link='0'):
		if not os.path.exists(f'./assets/{ctx.guild.id}'):
			os.mkdir(f'./assets/{ctx.guild.id}')
		if link == '0' and len(ctx.message.attachments) == 0:
			await ctx.send(f'{ctx.author.mention}, you forgot the image')
		else:
			if link == '0':
				link = ctx.message.attachments[0].url
			link_array = link.split('.')
			ex = f'.{link_array[len(link_array)-1]}'
			try:
				r = requests.get(link)
				with open(f'assets/{ctx.guild.id}/{name}{ex}', 'wb') as outfile:
					outfile.write(r.content)
				await ctx.send(f'{ctx.author.mention} added the {name} command successfully')
			except:
				await ctx.send(f'Error: url img not found')

	@commands.command()
	async def info(self, ctx):
		names = []
		for filename in os.listdir(f'./assets/{ctx.guild.id}'):
			splited = filename.split('.')
			names.append('.'.join(splited[:-1]))
		embed = discord.Embed(
			title = f'THE DIFFERENT IMAGES',
			description = '\n'.join(names),
			color = discord.Color(random.randint(0, 0xffffff))
		)
		await ctx.send(embed=embed)
		


def setup(client):
	client.add_cog(commands(client))