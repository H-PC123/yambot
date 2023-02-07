import discord

import message_handling
from discord.ext import commands


class YamBot(commands.Bot):
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    def __init__(self, command_prefix: str):
        super().__init__(command_prefix=command_prefix, intents=self.intents)

    @client.event
    async def on_ready(self) -> None:
        print(f"We have logged in as {self.user}")

    @client.event
    async def on_message(self, message: discord.Message) -> None:
        if message.author == self.user:
            return
        else:
            await self.process_commands(message)
            # TODO: needs to separate between commands and non commands
            await message_handling.handle_non_command(message)
# TODO: implement VC usage
