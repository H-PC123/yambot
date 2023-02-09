import os
import logging
import urllib3
from discord.ext import commands


class YamPlayer(commands.Cog):
    playlist = []
    playable_extensions = ["mp3"]
    media_folder = os.path.join(os.getcwd(), "Downloads")

    def __init__(self, media_folder=os.path.join(os.getcwd(), "Downloads")):
        super().__init__()
        self.media_folder = media_folder
        logging.info(f"Media will be downloaded to: {media_folder}")

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("Pong.")

    @commands.command()
    async def play(self, ctx: commands.Context):
        # TODO: parse link or file from message, download, add to playlist, play
        if ctx.message.attachments:
            playable_attachments = [x for x in ctx.message.attachments if self.check_file(x.url)]
            logging.info(f"Message has the following playables attached: {playable_attachments}")
            http = urllib3.PoolManager()
            for att in playable_attachments:
                logging.debug(f"Attempting download of {att}")
                with open(os.path.join(self.media_folder, att.filename), "wb+") as dest, \
                        http.request("GET", att.url, preload_content=False) as req:
                    dest.write(req.read())
                # TODO: wait on the request
                logging.info(f"File: {att.filename} downloaded from: {att.url}")
        elif self.check_link(ctx.message.content):
            logging.info(f"Message contains link potentially containing playable content: {ctx.message.content}")

        # self.playlist.append(ctx)
        return NotImplementedError

    async def check_file(self, link: str) -> bool:
        # TODO: need better check
        if link.endswith(self.playable_extensions[0]):
            return True
        logging.info(f"File hosted at {link} was not playable")
        return False

    async def check_link(self, ctx: commands.Context) -> bool:
        # TODO: add check for link(s) and is playable content
        return False

    async def store_mp3(self, download_link: str, library: os.path) -> None:
        # Downloads music into a media folder
        return NotImplementedError
