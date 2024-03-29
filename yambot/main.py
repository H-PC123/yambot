# TODO: restructure to standard
import sys
import os
import json
import logging
from yambot.yam_bot import YamBot

COMMAND_PREFIX = "."
LOGLEVEL = os.environ.get('LOGLEVEL')
LOGLEVEL = LOGLEVEL if LOGLEVEL else 'INFO'
os.makedirs(os.path.dirname('./logs/*'), exist_ok=True)
logging.basicConfig(filename='./logs/yam.log',
                    filemode='w+',
                    encoding='utf-8',
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=getattr(logging, LOGLEVEL))


def start_yam(args, command_prefix=COMMAND_PREFIX):
    # should yamBot handle with default intents or should we pass something here to the init call?
    my_yam = YamBot(command_prefix=command_prefix)

    if args:
        # Get token from args if passed
        bot_token = args[0]
    else:
        # Get token from <secrets.json> config file if nothing in args
        with open("../configs/secrets.json", "r") as f:
            secrets = json.load(f)
            bot_token = secrets["bot_token"]

    my_yam.run(bot_token)


if __name__ == "__main__":
    # TODO: use arg parser, we're probably going to need config files and arg overides
    start_yam(sys.argv[1:], COMMAND_PREFIX)
