import discord
import message_handling
from discord.ext import commands


class Bot(commands.Bot):
    client = discord.Client()

    def __init__(self, command_prefix):
        super().__init__(command_prefix=command_prefix)

    
    async def on_ready():
        print(f"We have logged in as {self.user}")

    async def on_message(message):
        if message.author == client.user:
            return
        else:
            message_handling.handleMessage(message)
