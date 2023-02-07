# TODO: restructure to standard
import sys
import os
import json
import logging
from bot import YamBot

COMMAND_PREFIX = "."
LOGLEVEL = os.environ.get('LOGLEVEL')
logging.basicConfig(filename='yam.log', encoding='utf-8', level=getattr(logging, LOGLEVEL))


def start_yam(args):
    # should yamBot handle with default intents or should we pass something here to the init call?
    my_yam = YamBot(command_prefix=COMMAND_PREFIX)

    if args:
        # Get token from args if passed
        bot_token = args[0]
    else:
        # Get token from secret.json if nothing in args
        with open("secrets.json", "r") as f:
            secrets = json.load(f)
            print(secrets)
            bot_token = secrets["bot_token"]

    my_yam.run(bot_token)
# TODO: Implement testing by getting another bot instance to send shit


if __name__ == "__main__":
    start_yam(sys.argv[1:])
