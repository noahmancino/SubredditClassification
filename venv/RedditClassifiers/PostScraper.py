'''
Scrapes last 1000 post titles from specified subreddits. The script will then a file each subreddit, with the name of
file being the name of the subreddit, consisting of post titles seperated by newlines.

Usage:
python PostScraper.py subredditname1 subredditname2 ...

Note:
Requires that an an ini file with valid praw credentials named 'credentials.ini' is in the same directory as the script
'''

import praw
import time
import sys
import configparser

config = configparser.ConfigParser()
config.read('credentials.ini')
config = config['DEFAULT']

to_scrape = sys.argv[1:]

reddit = praw.Reddit(
    user_agent=config['user_agent'],
    client_id=config['client_id'],
    client_secret=config['client_secret'],
    username=config['username'],
    password=config['password']
)
for subreddit in to_scrape:
    recent_posts = reddit.subreddit(subreddit).new(limit=1000)
    recent_posts = [recent_post.title for recent_post in recent_posts]
    with open(subreddit, 'w') as train_file:
        for post in recent_posts:
            train_file.write(post + '\n')

    # sleeping for API rate limit reasons
    time.sleep(120)