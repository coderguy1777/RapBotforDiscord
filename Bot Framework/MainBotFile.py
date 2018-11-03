import discord
from discord.ext import commands

TOKEN = 'NTA4MTQyNTcxNDUzNjc3NTY4.Dr682A.iJQMFHG4VJoStrrXL8finOz7Xig'
client = commands.Bot(command_prefix= '?searchfor')

@client.event
async def on_ready():
    print('Rappy Rap Rap')
    
client.run(TOKEN)
