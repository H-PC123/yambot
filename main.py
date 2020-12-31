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

    if message.content.startswith("What's ligma?"):
        await message.channel.send('Ligma balls')

    if message.content.startswith("join vc"):
        try:
            author_vc = message.author.voice.channel
            await message.channel.send("Coming on!")
            await author_vc.connect()
        except AttributeError:
            await message.channel.send("Join a channel first!")
    else:
        return

    if message.content.startswith("get out bot"):
        await message.channel.send("ok")
        author_vc = message.author.voice.channel
        await author_vc.disconnect()




client.run("NzkzMTQ2MzM2MDU5OTgxODI1.X-oBFg.0x3_8-GaFdpdiINSIpJSX6WYgrE")
