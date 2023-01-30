# TODO: restructure to standard
import sys
import json
from bot import YamBot


def start_yam(args):
    # should yamBot handle with default intents or should we pass something here to the init call?
    my_yam = YamBot(command_prefix='.')

    if args:
        # Get token from args
        bot_token = args[0]
    else:
        # Get token from secret.json if nothing in args
        with open("secrets.json", "r") as f:
            secrets = json.load(f)
            print(secrets)
            bot_token = secrets["bot_token"]

    my_yam.run(bot_token)


if __name__ == "__main__":
    start_yam(sys.argv[1:])
