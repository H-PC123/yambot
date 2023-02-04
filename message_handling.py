import discord
import re


async def handle_non_command(message: discord.Message) -> None:
    '''
    message handling method
    :param message: message to deal with
    :return:
    '''
    if message.content == "hello":
        #test string reply
        await message.reply("hiya back!")
    else:
        # TODO: implement an "is annoying" variable to control if should actually reply to any yt link
        video = re.finditer(
            r"(http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/))([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?",
            message.content)
        if video:
            # message has a yt video link, ask if user wants to play
            await message.reply(f"nice yt link ;)\n{next(video)[0]}\nLemme know if you want to play it!", suppress_embeds=True)

# TODO: actually handle messages
