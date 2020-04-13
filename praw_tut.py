import praw

reddit = praw.Reddit(client_id = "WB1eE8IEp98v4w", client_secret = "P5ot1jBJFueprjlPNhlMDkO2sws", username = "ashley_likes_cereal", password = "ashleylikescereal" , user_agent = "ashley")

subreddit = reddit.subreddit("all")

hot = subreddit.hot(limit = 1)

for submission in hot:
    print(submission.title)
