import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import shlex

TOKEN = 'NTEyMjcyNjg1ODUwNTU4NDY1.Ds4_vg.62blPpJTf-kEha3jZ2nhZeBfBBw'

client = commands.Bot(command_prefix='#')

chat_filter = ["ram", "ranch", "cH"]
bypass_list = []

@client.event
async def on_ready():
    print('Up and running')

@client.event
async def on_message(message):
    if 'nch' in message.content:
        print('Keyword found in message')
        await client.delete_message(message)
    if 'soh' in message.content:
        print('Keyword found in message')
        await client.delete_message(message)
    if 'ram' in message.content:
        print('Keyword found in message')
        await client.delete_message(message)
    if 'Ram' in message.content:
        print('Keyword found in message')
        await client.delete_message(message)
    if 'Nig' in message.content:
        print('Keyword found in message')
        await client.delete_message(message)
    if 'reeee' in message.content:
        print('Keyword found in message')
        await client.delete_message(message)
    if 'https://www.youtube.com/watch?v=3WQeTpnYN2c' in message.content:
        print('Keyword found')
        await client.delete_message(message)
    if 'https://www.youtube/watch?v=NFBxAvYlrs' in message.content:
        print('Keyword found')
        await client.delete_message(message)
    if 'NFB_xAvYlrs' in message.content:
        print('Keyword found')
        await client.delete_message(message)

client.run(TOKEN)
