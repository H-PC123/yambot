import asyncio


async def handle_message(message):
    if message.content == "hello":
        await asyncio.sleep(3)
        await message.channel.send("hiya back!")
    else:
        await message.channel.send('please help me!')

# TODO: actually handle messages
