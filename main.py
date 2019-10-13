import praw
import config
import re
from googletrans import Translator

reddit = praw.Reddit(client_id=config.ID,
                     client_secret=config.SECRET,
                     user_agent=config.USER_AGENT,
					 username=config.USERNAME,
					 password=config.PASSWORD)
					 
subreddit = reddit.subreddit('learnjapanese')

titleID = []
for submission in subreddit.hot(limit=10):
	if not submission.stickied:
	   titleID.append(submission.id)


translator = Translator()
thread = reddit.submission(id=titleID[0])
thread.comments.replace_more(limit=None)
RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
for comments in thread.comments.list():
    comments.body = RE_EMOJI.sub(r'', comments.body)
    # print(translator.detect(comments.body))
    if (translator.detect(comments.body).lang!='en'): # Checks for anything non-English
        print(comments.body)
        print(translator.translate(comments.body).text)
    
    
    
if __name__ == "__main__":
    start()