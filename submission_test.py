import praw

reddit = praw.Reddit(client_id = "WB1eE8IEp98v4w", client_secret = "P5ot1jBJFueprjlPNhlMDkO2sws", username = "ashley_likes_cereal", password = "ashleylikescereal" , user_agent = "ashley")

title = "Testing a post"
url = "https://praw.readthedocs.io"
reddit.subreddit("adevtest").submit(title, url)
