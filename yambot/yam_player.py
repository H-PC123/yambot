import os
import logging
import string

import discord
import urllib3
import mutagen
import random
import threading
import concurrent.futures
from discord.ext import commands


class YamPlayer(commands.Cog):
    playlist = []
    # TODO: Need to add Rlock to playlist and make sure methods that add to the playlist use the lock
    playable_extensions = ["mp3"]
    media_folder = os.path.join(os.getcwd(), "../Downloads")
    pool_manager = urllib3.PoolManager(maxsize=3)

    dest_lock = threading.RLock()

    # Will lock a song from being overwritten in the playlist by only releasing after song is played

    def __init__(self, media_folder=os.path.join(os.getcwd(), "../Downloads"), chunk_size=2048, filename_size=32):
        super().__init__()
        self.media_folder = media_folder
        self.chunk_size = chunk_size
        self.filename_size = filename_size
        logging.info(f"Media will be downloaded to: {media_folder}")

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("Pong.")

    @commands.command()
    async def play(self, ctx: commands.Context):
        if ctx.message.attachments:
            playable_attachments = [x for x in ctx.message.attachments if await self.check_file_extension(x.url)]
            logging.info(f"Message has the following playable files attached: {playable_attachments}")
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                saved_files = [executor.submit(self.store_attachment, x).result() for x in playable_attachments]
                #executor.map(self.store_attachment, playable_attachments)
            logging.debug(f"Files saved: {saved_files}")

            song_titles = [x.filename for x in playable_attachments]
            for song, title in zip(saved_files, song_titles):
                self.playlist.append((song, title))
            logging.debug(f"playlist: {self.playlist}")

                # TODO: Actually play the songs
        elif self.check_link(ctx.message):
            # TODO: parse link or file from message, download, add to playlist, play
            logging.info(f"Message contains link potentially containing playable content: {ctx.message.content}")

        # self.playlist.append(ctx)
        return NotImplementedError

    async def check_file(self, file: "path to file") -> bool:
        # TODO uses mutagen to check if the file is actuallty playable using the metadata
        return True

    async def check_file_extension(self, link: str) -> bool:
        if link.split('.')[-1] in self.playable_extensions:
            return True
        logging.info(f"File hosted at {link} was not playable")
        return False

    async def check_link(self, message: discord.Message) -> bool:
        # TODO: add check for link(s) and if is playable content
        raise NotImplementedError

    def store_attachment(self, att: "discord attachment") -> str:
        # Downloads music into self.media_folder
        try:
            rand_filename = self.get_rand_filename() + os.path.splitext(att.filename)[-1]
            logging.debug(f"{rand_filename} : {att.filename}")
            with self.dest_lock, \
                    open(os.path.join(self.media_folder, rand_filename), "wb+") as dest, \
                    self.pool_manager.request("GET", att.url, preload_content=False) as req:
                logging.debug(f"Attempting download of {att}")
                while True:
                    data = req.read(self.chunk_size)
                    if not data:
                        break
                    dest.write(data)
                logging.info(f"Attachment {att.filename} downloaded from: {att.url}")
            return rand_filename
        except urllib3.exceptions.HTTPError as e:
            # for handling specific errors (that I cant think of yet)
            logging.debug(f"File: {att.filename} could not be downloaded: {att.url} due to {e}")
            return None
        logging.debug("failed")

    def get_rand_filename(self) -> str:
        rand_name = "".join(random.choice(string.ascii_letters + string.digits) for i in range(self.filename_size))
        return rand_name

    def get_songname(self, file: "song file name") -> str:
        song_path = os.path.join(self.media_folder, file)
        return mutagen.File(song_path)["title"]
