import discord
import message_handling
from discord.ext import commands


class yamBot(commands.Bot):
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    def __init__(self, command_prefix):
        super().__init__(command_prefix=command_prefix, intents=self.intents)

    async def on_ready(self):
        print(f"We have logged in as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return
        else:
            message_handling.handleMessage(message)
