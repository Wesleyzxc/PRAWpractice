import os
from dotenv import load_dotenv
load_dotenv()


ID = os.getenv("REDDIT_ID")
SECRET = os.getenv("REDDIT_SECRET")
USERNAME = os.getenv("REDDIT_USER")
PASSWORD = os.getenv("REDDIT_PASSWORD")

USER_AGENT = os.getenv("REDDIT_AGENT")