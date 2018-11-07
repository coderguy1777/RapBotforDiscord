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
async def Astroworld():
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
    await client.say('5% TINT, By Travis Scott: https://www.youtube.com/watch?v=6SLD1ZQZ_4Y')
    await client.say('COFFEE BEAN, By Travis Scott: https://www.youtube.com/watch?v=Z6d3BofQqN0')
    await client.say('BUTTERFLY EFFECT, By Travis Scott: https://www.youtube.com/watch?v=k2pwvr8p4vM')
    await client.say('SKELETONS, By Travis Scott: https://www.youtube.com/watch?v=tAyYYKcySXA')


@client.command(pass_context=True)
async def join(ctx):
    author = ctx.message.author
    channel = author.voice_channel
    vc = await client.join_voice_channel(channel)

@client.event
async def play_yt(link):
    player = await client.voice_client_in(client.get_server(serverID)).create_ytdl_player(link)
    player.volume = 0.05
    player.start()
    return player

    if message.content.startswith('!yt'):
        link = message.content.strip('!yt ')
        player = await play_yt(link)
    
@client.command()
async def CANTSAY():
    await client.say('https://www.youtube.com/watch?v=gpnQhbOMQDA')


@client.command()
async def AstroThunder():
    await client.say('https://www.youtube.com/watch?v=Pa67b28h0vY')


@client.command()
async def AlexaPlayDespacito():
    await client.say('https://www.youtube.com/watch?v=kJQP7kiw5Fk')


@client.command()
async def RamRanch():
    await client.say('https://www.youtube.com/watch?v=7NYvnxu7NW0')


@client.command()
async def LofiGrantMacdonald():
    await client.say('https://www.youtube.com/watch?v=qrIEkgARtJI')


@client.command()
async def SKELETONS():
    await client.say('https://www.youtube.com/watch?v=tAyYYKcySXA')


@client.command()
async def COFFEEBEAN():
    await client.say('https://www.youtube.com/watch?v=Z6d3BofQqN0')


@client.command()
async def ALEXAPLAYDESPACITO():
     await client.say('STOP, BEING SO SAD!')


@client.command()
async def FIVEPERCENTTINT():
    await client.say('https://www.youtube.com/watch?v=6SLD1ZQZ_4Y')


@client.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await client.say(':boot: Cya, {}. Ya Loser!'.format(user.name))
    await client.kicks(user)


client.run(TOKEN)
