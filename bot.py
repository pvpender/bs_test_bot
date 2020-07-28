import discord as ds
import os
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
async def on_typing(message):
    await message.channel.send(f"Чё пишешь, {client.user.id} ")

client.run(TOKEN)
