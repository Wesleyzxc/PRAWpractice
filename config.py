import os


CLIENT = {
    "ID": os.getenv("REDDIT_ID"),
    "SECRET": os.getenv("REDDIT_SECRET")
}

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

USER_AGENT = os.getenv("USER_AGENT")

# Read subreddit from environment variable; warn and default to /r/all if not set
SUBREDDIT = os.getenv("SUBREDDIT")
if SUBREDDIT is None:
    logging.warning("Environment variable `SUBREDDIT` is not set; defaulting to `all`")
    SUBREDDIT = "all"

COMMENT_LENGTH_LIMIT = 9900

    © 2019 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help

    Contact GitHub
    Pricing
    API
    Training
    Blog
    About

