# import discord

# TOKEN = 'NjE4NDIwNDU2MTYwMTAwMzcy.XW5cCA.Nf11JH6Hdi0iPrZ02nzJEm-PrF0'

# client = discord.Client()

# @client.event
# async def on_message(message):
#     # we do not want the bot to reply to itself
#     if message.author == client.user:
#         return

#     if message.content.startswith('!hello'):
#         msg = 'Hello {0.author.mention}'.format(message)
#         await client.send_message(message.channel, msg)

# @client.event
# async def on_ready():
#     print('Logged in as')
#     print(client.user.name)
#     print(client.user.id)
#     print('------')

# client.run(TOKEN)
import discord
# from discord import User
# from discord.ext.commands import Bot

from discord.ext import commands
client = discord.Client()
bot = commands.Bot(command_prefix='>')

@bot.command()
async def test(ctx):
    await ctx.send('Deleting your account... {0}'.format(ctx.author))

@bot.command()
async def hello(ctx):
    await ctx.send('Hello {0}'.format(ctx.author))

@client.event
async def on_ready():
	try:
		# print bot information
		print(client.user.name)
		print(client.user.id)
		print('Discord.py Version: {}'.format(discord.__version__))
	
	except Exception as e:
		print(e)

bot.run('NjE4NDIwNDU2MTYwMTAwMzcy.XW6d7A.MT6LL4k2yLWw3cMiUqtd-YmC_ao')
# pybot = Bot(command_prefix = ">")

# @pybot.event
# async def on_read():
#     print("Client logged in")

# @pybot.command()
# async def hello(*args):
#     print(User.display_name)
#     return await pybot.say("Hello, world!")

# # @pybot.command()
# # async def truck(*args):
# #     await pybot.send_message(message.user,'Watchout for that truck!')
# @pybot.command(pass_context=True)
# async def truck(ctx):
#     await pybot.send_message(ctx.message.user, 'Watchout for that truck!')

# pybot.run('NjE4NDIwNDU2MTYwMTAwMzcy.XW5bLw.dlb9rtKpOCA5cwsKfwqQvuNFVtw')