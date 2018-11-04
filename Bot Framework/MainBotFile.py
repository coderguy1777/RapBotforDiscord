import discord
from discord.ext import commands

TOKEN = 'NTA4MTQyNTcxNDUzNjc3NTY4.Dr-tOw.gyvQANZjl0ujzpmA1CPz0n9XZOA'
client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Dope Rap Shit'))
    print('Rappy Rap Rap')


@client.command()
async def GrantMacdonald():
    await client.say('https://www.youtube.com/watch?v=2k0SmqbBIpQ')


@client.command()
async def AstroWorld():
    await client.say('SICKO MODE, By Travis Scott: https://www.youtube.com/watch?v=d-JBBNg8YKs')
    await client.say('Star Gazing, By Travis Scott: https://www.youtube.com/watch?v=2a8PgqWrc_4')
    await client.say('WAKE UP, By Travis Scott: https://www.youtube.com/watch?v=FAO8ZAUBx0c')
    await client.say('YOSEMITE, By Travis Scott: https://www.youtube.com/watch?v=ykMHDKB0-1o')
    await client.say('HOUSTONFORNICATION, By Travis Scott: https://www.youtube.com/watch?v=XzmnM2PLPfs')
    await client.say('NO BYSTANDERS, By Travis Scott: https://www.youtube.com/watch?v=OhXVLFpAAKY')
    await client.say('Stop Trying to be God, By Travis Scott: https://www.youtube.com/watch?v=YqvCptqhHfs')
    await client.say('CANT SAY, By Travis Scott: https://www.youtube.com/watch?v=gpnQhbOMQDA')
    await client.say('WHO? WHAT!, By Travis Scott: https://www.youtube.com/watch?v=gLkQA7iLNUk')
    await client.say('NC-17, By Travis Scott: https://www.youtube.com/watch?v=K2taklQnVzY')

@client.command()
async def AstroThunder():
    await client.say('AstroThunder, By Travis Scott: https://www.youtube.com/watch?v=Pa67b28h0vY')



client.run(TOKEN)
