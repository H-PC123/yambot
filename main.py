import json
from bot import yamBot

myBot = yamBot(command_prefix='.')

with open("secrets.json", "r") as f:
    secrets = json.load(f)
    print(secrets)
    bot_token = secrets["bot_token"]

#TODO: handle token passing from program call

myBot.run(bot_token)
