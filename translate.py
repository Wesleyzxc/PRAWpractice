import praw
import config
import re
from googletrans import Translator
from praw.models import Message

def start_translator():
    translator = Translator()
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    return translator, RE_EMOJI

def get_submissions(reddit, subreddit='learnjapanese', limit=10):
    subreddit = reddit.subreddit(subreddit)
    titleID = []
    for submission in subreddit.hot(limit=limit):
    	if not submission.stickied:
    	   titleID.append(submission.id)
    return titleID
    

def submission_translator(reddit, submissionNumber=0):    
    # Creates Translator instance and remove emojis
    translator, RE_EMOJI = start_translator()
    
    titleID = get_submissions(reddit) # Gets list of submissions (limit set to 10)
    thread = reddit.submission(id=titleID[submissionNumber])
    thread.comments.replace_more(limit=None)

    for comments in thread.comments.list():
        comments.body = RE_EMOJI.sub(r'', comments.body)
        print(translator.detect(comments.body))
        print(comments.body)
        if (translator.detect(comments.body).lang!='en'): # Checks for anything non-English
            print(comments.body)
            print(translator.translate(comments.body).text)
    
    
def inbox_translator(reddit):
    translator, RE_EMOJI = start_translator()
    
    for item in reddit.inbox.unread(limit=None):
        item.body = RE_EMOJI.sub(r'', item.body)
        print(translator.detect(item.body))
        if (translator.detect(item.body).lang!='en'): # Checks for anything non-English
            user = item.author
            item.reply("Hi, " + str(user) + ". Your original text: " + item.body + " is translated to: " + translator.translate(item.body).text)
            item.mark_read()
            print(translator.translate(item.body).text)
    
