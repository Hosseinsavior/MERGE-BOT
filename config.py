import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "0cef89ed2c8025c16d2b4d42a1b8d792")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5466053464:AAF9Ed9gYvT-jXozzvua015J4OQ7sp8KDLk")
    TELEGRAM_API = os.environ.get("TELEGRAM_API", 14699743)
    OWNER = os.environ.get("OWNER", 5059280908)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Savior_128")
    PASSWORD = os.environ.get("PASSWORD", " 123456")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Savior:136707@hossein.porr3rf.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "-1001788952875")  # Add channel id as -100 + Actual ID
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle"]
