'''reddit class'''

import praw
from .analyzer import Analyzer
from .models import Article


class Reddit:
    '''client for reddit api'''
    def __init__(self):
        self.client = self.login()
        self.analyzer = Analyzer()
        self.image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Reddit.svg/1024px-Reddit.svg.png"

    def login(self):
        '''login to reddit client'''
        with open('linklys/keys.txt') as file:
            keys = file.readlines()
        return praw.Reddit(
            client_id=keys[0].strip(),
            client_secret=keys[1].strip(),
            user_agent=keys[2].strip()
        )

    def get_subreddits(self):
        '''create list of subreddit objects from file of subreddits'''
        with open('linklys/subreddits.txt') as file:
            subreddits = file.readlines()
        subreddits = [
            self.client.subreddit(subreddit.strip()) for subreddit in subreddits
        ]
        return subreddits

    def get_posts(self, subreddit):
        '''get all posts from subreddit object'''
        dirty = [post for post in subreddit.hot(limit=20)]
        clean = [
            Article(
                post.url,
                self.image_url,
                post.title,
                "",
                str(post.author),
                post.created,
                self.analyzer.sentiment(post.title),
                post.subreddit,
                "reddit.com"
            ) for post in dirty
        ]
        return clean
