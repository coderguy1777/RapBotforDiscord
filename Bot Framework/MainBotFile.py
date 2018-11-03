import discord
from discord.ext import commands

TOKEN = 'NTA4MTQyNTcxNDUzNjc3NTY4.Dr682A.iJQMFHG4VJoStrrXL8finOz7Xig'
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

client.run(TOKEN)
