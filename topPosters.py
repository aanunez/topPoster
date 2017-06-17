#!/usr/bin/env python3

from praw import Reddit
from argparse import ArgumentParser
from collections import deque

try:
    from credentials import *
except ImportError:
    print("Please setup the credentails file.\n" + \
        "Consult the Readme for more information.")
    raise SystemExit

def connect():
    reddit = Reddit(client_id=CLIENT_ID, client_secret=SECRET, password=PASSWORD,
                    user_agent=AGENT, username=USER)
    reddit.read_only = True
    return reddit

def top_poster(reddit, sub, top, depth):

    subreddit = reddit.subreddit(sub)
    hot = subreddit.hot()

def parse_args():
    parser = ArgumentParser(description=
        "")
    parser.add_argument('sub', nargs='?', help=
        "Subreddit's name")
    parser.add_argument('depth',nargs='?',default=500, help=
        "")
    parser.add_argument('top',nargs='?',default=100, help=
        "")
    opts = parser.parse_args()
    return ( opts.user, int(opts.depth), int(opts.top) )

def main():
    opts = parse_args()
    users = top_posters( connect(), opt.sub, opts.top, opts.depth )
    print(users)

if __name__ == "__main__":
    main()




