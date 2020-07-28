import discord as ds
from discord.abc import User, GuildChannel, Messageable
from discord import user
import os
from datetime import datetime

TOKEN = os.environ.get('B_T')
client = ds.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.content.startswith('!hello'):
        await message.channel.send('Привет, раб системы')

@client.event
async def on_typing(Messageable, user, datetime):
    await Messageable.send(f"Net ne pishi {user.name}")

client.run(TOKEN)