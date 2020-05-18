import discord as ds
import os
TOKEN = os.environ.get('B_T')
client = ds.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.content.startswith('hello') or message.content.startswith('hi') or message.content.startswith('привет') or message.content.startswith('дарова') or message.content.startswith('Hello') or message.content.startswith('Hi') or message.content.startswith('Привет') or message.content.startswith('Дарова'):
     await message.channel.send('Привет, раб системы')

client.run(TOKEN)
