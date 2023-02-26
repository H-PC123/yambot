import unittest
import time
import json
import concurrent.futures

from yambot.yam_bot import YamBot
from yambot import *

import discord
from discord.ext import commands



class YamBotTestClass(unittest.IsolatedAsyncioTestCase):
    bot_thread_executor = concurrent.futures.ThreadPoolExecutor()
    test_intents = discord.Intents.default()
    test_intents.message_content = True
    test_yam = YamBot(command_prefix=".")
    test_bot = commands.Bot(command_prefix="!", intents=test_intents)
    #test_bot.change_presence(activity=discord.Game(name="Testing"))

    @classmethod
    def setUpClass(cls) -> None:
        print(f"running setUpClass")
        with open("../configs/secrets.json", "r") as f:
            secrets = json.load(f)
            yam_token = secrets["bot_token"]
            test_token = secrets["test_token"]
        # Launches yambot instance and an instance of a default bot on threads
        # Default bot is used for sending test messages
        cls.bot_thread_executor.submit(cls.test_yam.run, yam_token)
        cls.bot_thread_executor.submit(cls.test_bot.run, test_token)
        while not (cls.test_yam.is_ready() and cls.test_bot.is_ready()):
            time.sleep(2)
        print(f"bots are ready")

    @classmethod
    def tearDownClass(cls) -> None:
        print(f"running tearDownClass")
        #cls.bot_thread_executor.shutdownNow()

    async def asyncSetUp(self) -> None:
        print(f"running setUp")
        await self.test_yam.wait_until_ready()
        await self.test_bot.wait_until_ready()
        print(f"bots are ready")

    def run_bot(self):
        print(f"commiting sudoku")
        await self.test_yam.close()
        await self.test_bot.close()
        print(f"good night")

    def test_send_message_test(self):
        time.sleep(2)
        self.assertTrue(True)

    def test_my_test(self):
        self.assertEqual('foo'.upper(), 'FOO', "what the hell did you do?")


if __name__ == '__main__':
    test_classes = [YamBotTestClass]
    suites = []
    test_loader = unittest.TestLoader()

    for test_class in test_classes:
        suite = test_loader.loadTestsFromTestCase(test_class)
        suites.append(suite)

    master_suite = unittest.TestSuite(suites)
    unittest.TextTestRunner().run(master_suite)
