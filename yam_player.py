import os
from discord.ext import commands


class YamPlayer(commands.Cog):
    playlist = []

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("Pong.")

    @commands.command()
    async def play(self, ctx: commands.Context):
        # TODO: parse link or file from message, download, add to playlist, play
        #self.playlist.append(ctx)
        return NotImplementedError



    async def store_mp3(self, download_link: str, library: os.path) -> None:
        return NotImplementedError