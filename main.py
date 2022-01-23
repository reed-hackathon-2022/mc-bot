from parser import parse
from tweeter import tweet_connections


def launch_bot():
    contents = parse()
    tweet_connections(contents)


if __name__ == "__main__":
    launch_bot()