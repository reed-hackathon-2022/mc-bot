import logging

from parser import parse
from tweeter import tweet_connections


def launch_bot():
    contents = parse()
    tweet_connections(contents)


if __name__ == "__main__":
    logging.basicConfig(
        filename="twitter.log", level=logging.DEBUG
    )
    launch_bot()
