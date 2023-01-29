import discord
from bot import Bot

myBot = Bot(command_prefix='.')

bot_token = "NzkzMTQ2MzM2MDU5OTgxODI1.X-oBFg.bjQ9MfreAucktpKFD27Cbsrvc04"
#TODO: use secret config
#TODO: handle token passing from program call

myBot.run(bot_token)
