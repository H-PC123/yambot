# TODO: restructure to standard
import sys
import json
from bot import yamBot


def start_yam(args):
    # should yamBot handle with default intents or should we pass something here to the init call?
    myYam = yamBot(command_prefix='.')

    if args:
        bot_token = args[0]
    else:
        with open("secrets.json", "r") as f:
            secrets = json.load(f)
            print(secrets)
            bot_token = secrets["bot_token"]

    myYam.run(bot_token)


if __name__ == "__main__":
    start_yam(sys.argv[1:])
