import re
import os
import time
import logging
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from a .env file
load_dotenv()

# Helper function to fetch and validate integer environment variables
def get_env_int(var_name, default_value):
    """
    Fetch an environment variable as an integer. If the value is invalid,
    return the default or raise an error.
    """
    value = os.getenv(var_name, default_value)
    try:
        return int(value)
    except (ValueError, TypeError):
        raise SystemExit(
            f"[ERROR] - The environment variable '{var_name}' must be a valid integer. Current value: {value}"
        )


# Basic configurations
API_ID = os.getenv("API_ID", "27744639")
API_HASH = os.getenv("API_HASH", "a5e9da62bcd7cc761de2490c52c89ccf")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8125428412:AAFRUBKz5Nt0mx9qaBrlTWwTBlX-Aop6vT4")
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "ituuc")
BOT_USERNAME = os.getenv("BOT_USERNAME", "sung_gamebot")
BOT_NAME = os.getenv("BOT_NAME", "Moonligt")
ASSUSERNAME = os.getenv("ASSUSERNAME")

# Database configurations
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://waifuuu0786:sungjinwoo@cluster0.uctgneu.mongodb.net/?retryWrites=true&w=majority")

# Limits and durations
DURATION_LIMIT_MIN = get_env_int("DURATION_LIMIT", 17000)
SONG_DOWNLOAD_DURATION = get_env_int("SONG_DOWNLOAD_DURATION", 9999999)
SONG_DOWNLOAD_DURATION_LIMIT = get_env_int("SONG_DOWNLOAD_DURATION_LIMIT", 9999999)

# Owner and logging
# Chat id of a group for logging bot's activities
LOGGER_ID = os.getenv("LOGGER_ID", "-1002272021040")
OWNER_ID = get_env_int("OWNER_ID", "7775259302")

# Heroku configurations
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

# Git repository settings
UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/itz-rehan-786/UtopiaMax.git")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

# Support links
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/ur_hell_paradise")
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/ur_hell_paradise")

# Validate support URLs
if SUPPORT_CHANNEL and not re.match(r"^https://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL URL must start with https://")

if SUPPORT_CHAT and not re.match(r"^https://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - SUPPORT_CHAT URL must start with https://")

# Spotify credentials
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "Your_Default_Spotify_Client_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "Your_Default_Spotify_Client_Secret")

# File size limits
TG_AUDIO_FILESIZE_LIMIT = get_env_int("TG_AUDIO_FILESIZE_LIMIT", 5242880000)
TG_VIDEO_FILESIZE_LIMIT = get_env_int("TG_VIDEO_FILESIZE_LIMIT", 5242880000)

# Auto-assistant settings
AUTO_LEAVING_ASSISTANT = os.getenv("AUTO_LEAVING_ASSISTANT", "True").lower() == "true"
AUTO_LEAVE_ASSISTANT_TIME = get_env_int("ASSISTANT_LEAVE_TIME", 9000)

# Playlist settings
PLAYLIST_FETCH_LIMIT = get_env_int("PLAYLIST_FETCH_LIMIT", 25)

# Image URLs
START_IMG_URL = os.getenv(
    "START_IMG_URL", "https://graph.org/file/364a09ddd47378efaecfb-2d3ae182ccf44e9087.jpg"
)
PING_IMG_URL = os.getenv(
    "PING_IMG_URL", "https://graph.org/file/35ef624f376e22a0fa1d7-1ea63e464ea9f36fab.jpg"
)
PLAYLIST_IMG_URL = os.getenv(
    "PLAYLIST_IMG_URL", "https://envs.sh/K-2.jpg"
) 
TELEGRAM_AUDIO_URL = os.getenv(
    "TELEGRAM_AUDIO_URL", "https://envs.sh/K-2.jpg"
) 
TELEGRAM_VIDEO_URL = os.getenv(
    "TELEGRAM_VIDEO_URL", "https://envs.sh/K-2.jpg"
) 
STREAM_IMG_URL = os.getenv(
    "STREAM_IMG_URL", "https://envs.sh/K-2.jpg"
) 
SOUNCLOUD_IMG_URL = os.getenv(
    "SOUNCLOUD_IMG_URL", "https://envs.sh/K-2.jpg"
) 
YOUTUBE_IMG_URL = os.getenv(
    "YOUTUBE_IMG_URL", "https://envs.sh/K-2.jpg"
) 
SPOTIFY_ARTIST_IMG_URL = os.getenv(
    "SPOTIFY_ARTIST_IMG_URL", "https://envs.sh/K-2.jpg",
) 
SPOTIFY_ALBUM_IMG_URL = os.getenv(
    "SPOTIFY_ALBUM_IMG_URL", "https://envs.sh/K-2.jpg"
) 
SPOTIFY_PLAYLIST_IMG_URL = os.getenv(
    "SPOTIFY_PLAYLIST_IMG_URL", "https://envs.sh/K-2.jpg"
) 

# YouTube thumbnail URL format
YOUTUBE_IMG_URL = "https://img.youtube.com/vi/{video_id}/hqdefault.jpg"

# Session strings
STRING1 = os.getenv("STRING_SESSION", "BQGnWX8Alb5W7EP_IZ4Udn5BNtlQECliuAioGKRehPTpn_266dyFzdRGPAUNNdzUs7gT3Q9aqrHAgBo04QpinLUk-0e3FTKuf4AZx1-c_2Yf-GN9oMnf22LloRhUL63GfExpQtT0oanRHWK2Qxqoi2TowvRPVYS1oKQIJzO-ZtN8tTL7_pvIT3d5BUmqjNkS_GFQ3XoIIM6Q5RsObrguGx0ov8axm5PNso9yACQx0AhgnniTkm5ReWFLJrJtvNq82YHCJkAjX-5ovIL7MF2nC8UoVf0Gn0sZQ3eRO9NOkOIjFmXHg-O8MecteNhsRMubPsMKOibGtovMHxiLsCeOy_EzkDfmswAAAAHRgjE-AA")
STRING2 = os.getenv("STRING_SESSION2", "BQGnWX8Alb5W7EP_IZ4Udn5BNtlQECliuAioGKRehPTpn_266dyFzdRGPAUNNdzUs7gT3Q9aqrHAgBo04QpinLUk-0e3FTKuf4AZx1-c_2Yf-GN9oMnf22LloRhUL63GfExpQtT0oanRHWK2Qxqoi2TowvRPVYS1oKQIJzO-ZtN8tTL7_pvIT3d5BUmqjNkS_GFQ3XoIIM6Q5RsObrguGx0ov8axm5PNso9yACQx0AhgnniTkm5ReWFLJrJtvNq82YHCJkAjX-5ovIL7MF2nC8UoVf0Gn0sZQ3eRO9NOkOIjFmXHg-O8MecteNhsRMubPsMKOibGtovMHxiLsCeOy_EzkDfmswAAAAHRgjE-AA")
STRING3 = os.getenv("STRING_SESSION3", "BQGnWX8Alb5W7EP_IZ4Udn5BNtlQECliuAioGKRehPTpn_266dyFzdRGPAUNNdzUs7gT3Q9aqrHAgBo04QpinLUk-0e3FTKuf4AZx1-c_2Yf-GN9oMnf22LloRhUL63GfExpQtT0oanRHWK2Qxqoi2TowvRPVYS1oKQIJzO-ZtN8tTL7_pvIT3d5BUmqjNkS_GFQ3XoIIM6Q5RsObrguGx0ov8axm5PNso9yACQx0AhgnniTkm5ReWFLJrJtvNq82YHCJkAjX-5ovIL7MF2nC8UoVf0Gn0sZQ3eRO9NOkOIjFmXHg-O8MecteNhsRMubPsMKOibGtovMHxiLsCeOy_EzkDfmswAAAAHRgjE-AA")
STRING4 = os.getenv("STRING_SESSION4", "BQGnWX8Alb5W7EP_IZ4Udn5BNtlQECliuAioGKRehPTpn_266dyFzdRGPAUNNdzUs7gT3Q9aqrHAgBo04QpinLUk-0e3FTKuf4AZx1-c_2Yf-GN9oMnf22LloRhUL63GfExpQtT0oanRHWK2Qxqoi2TowvRPVYS1oKQIJzO-ZtN8tTL7_pvIT3d5BUmqjNkS_GFQ3XoIIM6Q5RsObrguGx0ov8axm5PNso9yACQx0AhgnniTkm5ReWFLJrJtvNq82YHCJkAjX-5ovIL7MF2nC8UoVf0Gn0sZQ3eRO9NOkOIjFmXHg-O8MecteNhsRMubPsMKOibGtovMHxiLsCeOy_EzkDfmswAAAAHRgjE-AA") 
STRING5 = os.getenv("STRING_SESSION5", "BQGnWX8Alb5W7EP_IZ4Udn5BNtlQECliuAioGKRehPTpn_266dyFzdRGPAUNNdzUs7gT3Q9aqrHAgBo04QpinLUk-0e3FTKuf4AZx1-c_2Yf-GN9oMnf22LloRhUL63GfExpQtT0oanRHWK2Qxqoi2TowvRPVYS1oKQIJzO-ZtN8tTL7_pvIT3d5BUmqjNkS_GFQ3XoIIM6Q5RsObrguGx0ov8axm5PNso9yACQx0AhgnniTkm5ReWFLJrJtvNq82YHCJkAjX-5ovIL7MF2nC8UoVf0Gn0sZQ3eRO9NOkOIjFmXHg-O8MecteNhsRMubPsMKOibGtovMHxiLsCeOy_EzkDfmswAAAAHRgjE-AA")

# Helper functions
def time_to_seconds(time: str) -> int:
    """Converts time in 'hh:mm:ss' format to seconds."""
    try:
        return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))
    except ValueError:
        raise SystemExit("[ERROR] - Time format must be 'hh:mm:ss'.")

# Derived configurations
DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# Filters and caches
BANNED_USERS = filters.user()  # Ensure filters is properly imported
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Create a Pyrogram Client
app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Bot is now running!")

# Retry logic for API rate limits (FloodWait)
def send_message_with_retry(client, chat_id, text):
    try:
        client.send_message(chat_id, text)
    except FloodWait as e:
        logger.warning(f"Flood wait encountered. Sleeping for {e.x} seconds.")
        time.sleep(e.x)  # Wait for the specified duration
        send_message_with_retry(client, chat_id, text)  # Retry after the wait

# Run the bot
if __name__ == "__main__":
    app.run() # enhance it
