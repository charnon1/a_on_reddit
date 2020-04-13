import praw
import requests
import os

reddit = praw.Reddit(client_id = "WB1eE8IEp98v4w", client_secret = "P5ot1jBJFueprjlPNhlMDkO2sws", username = "ashley_likes_cereal", password = "ashleylikescereal" , user_agent = "ashley")
#
# subreddit_list = [ "aww","all", "gifs", "interestingasfuck", "wtf", "funny", "pics", "mildlyinteresting", "lmGoingToHellForThis", "me_irl"]
#
# top_titles = []
#
subreddit = reddit.subreddit("r/gifs")
hot_subreddit = subreddit.hot(limit=5)
for post in hot_subreddit:
    if post.stickied != True and post.is_self == False:
        print(post.url)
        print(post.title)
