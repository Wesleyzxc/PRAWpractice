import praw
import config
import re
import time
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
    
def response(original, translated):
    response_str = '''The original text: {0} is translated to: {1}
    '''
    print(response_str.format(original, translated))
    
    return response_str.format(original, translated) # replace placeholders
    
def inbox_translator(reddit):
    translator, RE_EMOJI = start_translator()
    
    for item in reddit.inbox.unread(limit=None):
        item.body = RE_EMOJI.sub(r'', item.body) # replaces emoji
        item.body = item.body.strip('u/just_a_data_bot') # removes mention
        print(item.body)
        if (item.body == ""):
            original = item.parent().body # Gets parent comment
            translated = translator.translate(original).text
            item.reply(response(original, translated))
            item.mark_read()
            time.sleep(3)
            
        else:        
            print(translator.detect(item.body)) # Shows detected language
            if (translator.detect(item.body).lang!='en'): # Checks for anything non-English
                original = item.body # Gets parent comment
                translated = translator.translate(original).text
                user = item.author
                item.reply(response(original, translated))
                item.mark_read()
                time.sleep(3)
        
