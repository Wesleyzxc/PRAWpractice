import praw
import config
import re
from translate import submission_translator, inbox_translator
from googletrans import Translator

def start():
    reddit = praw.Reddit(client_id=config.ID,
                         client_secret=config.SECRET,
                         user_agent=config.USER_AGENT,
    					 username=config.USERNAME,
    					 password=config.PASSWORD)
    
    return reddit
					 



    

    
if __name__ == "__main__":
    reddit = start()
    #submission_translator(reddit, submissionNumber=0)
    inbox_translator(reddit)