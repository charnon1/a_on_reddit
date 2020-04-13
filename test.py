import praw

reddit = praw.Reddit(client_id = "WB1eE8IEp98v4w", client_secret = "P5ot1jBJFueprjlPNhlMDkO2sws", username = "ashley_likes_cereal", password = "ashleylikescereal" , user_agent = "ashley")

subreddit_list = [ "aww","all", "gifs", "interestingasfuck", "wtf", "funny", "pics", "mildlyinteresting", "lmGoingToHellForThis", "me_irl"]

top_titles = []

# for sub in subreddit_list:
#     subreddit = reddit.subreddit(sub)
#     hot_subreddit = subreddit.hot(limit=1)
#     for post in hot_subreddit:
#         top_titles.append(post.title)
#
# print(len(top_titles))


subreddit = reddit.subreddit("pics")
hot_subreddit = subreddit.hot(limit=2)
for post in hot_subreddit:
    if not subreddit.is_self:
        print(subreddit.url)
