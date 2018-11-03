import discord
from discord.ext import commands

TOKEN = 'NTA4MTQyNTcxNDUzNjc3NTY4.Dr-tOw.gyvQANZjl0ujzpmA1CPz0n9XZOA'
client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('Rappy Rap Rap')


@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))
    await client.process_commands(message)


@client.command()
async def GrantMacdonald():
    await client.say('https://www.youtube.com/watch?v=2k0SmqbBIpQ')


@client.command()
async def ShowmeSomeTravisScott():
    await client.say('Heres some Travis Scott: https://www.youtube.com/watch?v=6ONRf7h3Mdk')


@client.command()
async def AstroWorldSickoMode():
    await client.say('SICKO MODE, By Travis Scott: https://www.youtube.com/watch?v=d-JBBNg8YKs')

@client.command()
async def AstroWorldStarGazing():
    await client.say('Star Gazing, By Travis Scott: https://www.youtube.com/watch?v=2a8PgqWrc_4')

client.run(TOKEN)
