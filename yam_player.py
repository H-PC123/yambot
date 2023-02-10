import os
import logging

import discord
import urllib3
import threading
from discord.ext import commands


class YamPlayer(commands.Cog):
    playlist = []
    # TODO: Need to add Rlock to playlist and make sure methods that add to the playlist use the lock
    playable_extensions = ["mp3"]
    media_folder = os.path.join(os.getcwd(), "Downloads")
    pool_manager = urllib3.PoolManager()

    def __init__(self, media_folder=os.path.join(os.getcwd(), "Downloads"), chunk_size=2048):
        super().__init__()
        self.media_folder = media_folder
        self.chunk_size = chunk_size
        logging.info(f"Media will be downloaded to: {media_folder}")

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("Pong.")

    @commands.command()
    async def play(self, ctx: commands.Context):
        if ctx.message.attachments:
            playable_attachments = [x for x in ctx.message.attachments if self.check_file(x.url)]
            logging.info(f"Message has the following playable files attached: {playable_attachments}")
            for att in playable_attachments:
                await self.store_attachment(att)
                # TODO: Add item to playlist, then hit play
        elif self.check_link(ctx.message):
            # TODO: parse link or file from message, download, add to playlist, play
            logging.info(f"Message contains link potentially containing playable content: {ctx.message.content}")

        # self.playlist.append(ctx)
        return NotImplementedError

    def check_file(self, link: str) -> bool:
        # TODO: should check somehow for security
        if link.split('.')[-1] in self.playable_extensions:
            return True
        logging.info(f"File hosted at {link} was not playable")
        return False

    async def check_link(self, message: discord.Message) -> bool:
        # TODO: add check for link(s) and if is playable content
        return False

    async def store_attachment(self, att: "Message attachment", destination: str = media_folder) -> bool:
        # Downloads music into self.media_folder
        # TODO: if file is being played or on the queue, they need to be locked so they aren't overwritten
        logging.debug(f"Attempting download of {att}")
        # TODO: wait on the request, maybe use threads when this method is called or a wait here
        try:
            with open(os.path.join(destination, att.filename), "wb+") as dest, \
                    self.pool_manager.request("GET", att.url, preload_content=False) as req:
                while True:
                    data = req.read(self.chunk_size)
                    if not data:
                        break
                    dest.write(data)
            logging.info(f"File: {att.filename} downloaded from: {att.url}")
            return True
        except:
            # for handling specific errors (that I cant think of yet)
            logging.debug(f"File: {att.filename} could not be downloaded: {att.url}")
            return False
