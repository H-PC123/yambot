import discord
import re


async def handle_non_command(message: discord.Message) -> None:
    if message.content == "hello":
        # test string reply
        await message.reply("hiya back!")
    else:
        # TODO: implement an "is annoying" or bot channel/quiet mode variable to control if should actually reply to any yt link
        video = re.finditer(
            r"(?:https?:\/\/)?(?:www\.)?youtu\.?be(?:\.com)?\/?.*(?:watch|embed)?(?:.*v=|v\/|\/)([\w\-_]+)\&?",
            message.content)
        if video:
            # message has a yt video link, ask if user wants to play
            await message.reply(f"nice yt link ;)"
                                f"\n{next(video)[0]}"
                                f"\nLemme know if you want to play it!", suppress_embeds=True)

# TODO: actually handle messages
