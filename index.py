import discord
import os
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '.',activity=discord.Game('.help'),help_command=None)

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
	# await client.change_presence(status=discord.Status.online,activity=discord.Game('.help'))
	print(f'The bot {client.user} is ready!')
	for guild in client.guilds:
		if not os.path.exists(f'./assets/{guild.id}'):
			os.mkdir(f'./assets/{guild.id}')
	
@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f"Error: MissingRequiredArgument")
	elif isinstance(error, commands.CommandNotFound):
		await ctx.send(f"Error: CommandNotFound")
	else:
		print(error)

client.run('NzAwMDUwMzY1MTY0NTUyMjMy.XqhsvQ.Xs6j5YdTAsO27ytek9KlWEGcSKg')