import praw
import config

reddit = praw.Reddit(client_id=config.ID,
                     client_secret=config.SECRET,
                     user_agent=config.USER_AGENT,
					 username=config.USERNAME,
					 password=config.PASSWORD)
					 
subreddit = reddit.subreddit('singapore')

for submission in subreddit.hot(limit=10):
	if not submission.stickied:
	   print(submission.title)