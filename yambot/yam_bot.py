import discord
import logging

from yambot import message_handling
from yambot.yam_player import YamPlayer

from discord.ext import commands


class YamBot(commands.Bot):
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    def __init__(self, command_prefix: str):
        super().__init__(command_prefix=command_prefix, intents=self.intents)

    async def import_cogs(self) -> None:
        await self.add_cog(YamPlayer())

    async def setup_hook(self) -> None:
        await self.import_cogs()
        logging.debug("Cogs imported")

    @client.event
    async def on_ready(self) -> None:
        logging.info(f"Logged in as {self.user}")
        print(f"Logged in as {self.user}")

    @client.event
    async def on_message(self, message: discord.Message) -> None:
        if message.author == self.user:
            return
        else:
            await self.process_commands(message)
            # TODO: needs to separate between commands and non commands
            await message_handling.handle_non_command(message)
# TODO: implement VC usage
