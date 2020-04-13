import praw
import requests
import os

reddit = praw.Reddit(client_id = "WB1eE8IEp98v4w", client_secret = "P5ot1jBJFueprjlPNhlMDkO2sws", username = "ashley_likes_cereal", password = "ashleylikescereal" , user_agent = "ashley")

#posting a text
# title = "Testing a post"
# url = "https://praw.readthedocs.io"
# reddit.subreddit("adevtest").submit(title, url)

#posting an image
# title = 'My favorite picture'
# image = "./dolphin.jpg"
# reddit.subreddit('adevtest').submit_image(title, image)

#download image given a URL
# img_data = requests.get("https://www.nzherald.co.nz/resizer/q0yZRWen-s1_w7yO3WceXlW2tvs=/620x349/smart/filters:quality(70)/arc-anglerfish-syd-prod-nzme.s3.amazonaws.com/public/LYVOOBXGZFCQDHFQ2HZFPTDYVU.jpg").content
# with open('image_name.jpg', 'wb') as handler:
#     handler.write(img_data)

def download_image(url):
    img_data = requests.get(url).content
    with open('image.jpg', 'wb') as handler:
        handler.write(img_data)

def post_image(title):
    image = "./image.jpg"
    reddit.subreddit('adevtest').submit_image(title, image)

def delete_image(image_name):
    os.remove(image_name)

subreddit_list = [ "aww", "interestingasfuck", "funny", "pics", "mildlyinteresting", "me_irl"]

for sub in subreddit_list:
    subreddit = reddit.subreddit(sub)
    hot_subreddit = subreddit.hot(limit=5)
    for post in hot_subreddit:
        #not stickied and has an image
        if post.stickied != True and post.url != None:
            print(sub)
            print(post.url)
            print(post.title)
            download_image(post.url)
            post_image(post.title)
            delete_image("image.jpg")
            break
