import discord
from discord.ext import commands

TOKEN = 'NTA5NDM5MzM4Njk5MDMwNTI4.DsN03w.KBzZWf1le4HdOtYDGioX0GIlrjQ'

client = commands.Bot(command_prefix='%')


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Cinema 4D'))
    print('Cinema 4D, Duh.')


@client.command()
async def test():
    await client.say('Hello Animator!')

client.run(TOKEN)