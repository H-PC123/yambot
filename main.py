import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$What's ligma?"):
        await message.channel.send('Ligma balls')


client.run("NzkzMTQ2MzM2MDU5OTgxODI1.X-oBFg.0x3_8-GaFdpdiINSIpJSX6WYgrE")
