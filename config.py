import os
import re
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

# Configuration Variables
API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "X_STARBOY_KT")
BOT_USERNAME = os.getenv("BOT_USERNAME", "UtopiaMaxBot")
BOT_NAME = os.getenv("BOT_NAME", "Utopia")
ASSUSERNAME = os.getenv("ASSUSERNAME")
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "Your_Default_MongoDB_URI")

# Limits and durations
DURATION_LIMIT_MIN = get_env_int("DURATION_LIMIT", 17000)
SONG_DOWNLOAD_DURATION = get_env_int("SONG_DOWNLOAD_DURATION", 9999999)
SONG_DOWNLOAD_DURATION_LIMIT = get_env_int("SONG_DOWNLOAD_DURATION_LIMIT", 9999999)

# Group IDs for logging
try:
    LOG_GROUP_ID = get_env_int("LOG_GROUP_ID", -1002359323024)
    if not str(LOG_GROUP_ID).startswith("-100"):
        raise ValueError("LOG_GROUP_ID must start with '-100'.")
except ValueError as e:
    raise SystemExit(f"[ERROR] - {e}")

try:
    LOGGER_ID = get_env_int("LOGGER_ID", -1002359323024)
    if not str(LOGGER_ID).startswith("-100"):
        raise ValueError("LOGGER_ID must start with '-100'.")
except ValueError as e:
    raise SystemExit(f"[ERROR] - {e}")

try:
    OWNER_ID = get_env_int("OWNER_ID", 7318101682)
except ValueError:
    raise SystemExit("[ERROR] - OWNER_ID must be a valid integer.")

# Heroku configurations
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

# Git repository settings
UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/VIPBOLTE/GOKUMUSIC.git")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

# Support links
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/Kayto_Official")
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/Anime_Chat_Group_Community")

# Spotify credentials
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "Your_Default_Spotify_Client_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "Your_Default_Spotify_Client_Secret")

# File size limits
TG_AUDIO_FILESIZE_LIMIT = get_env_int("TG_AUDIO_FILESIZE_LIMIT", 5242880000)
TG_VIDEO_FILESIZE_LIMIT = get_env_int("TG_VIDEO_FILESIZE_LIMIT", 5242880000)

# Image URLs
START_IMG_URL = os.getenv(
    "START_IMG_URL", "https://graph.org/file/364a09ddd47378efaecfb-2d3ae182ccf44e9087.jpg"
)
PING_IMG_URL = os.getenv(
    "PING_IMG_URL", "https://graph.org/file/35ef624f376e22a0fa1d7-1ea63e464ea9f36fab.jpg"
)

# Helper functions
def validate_url(url, var_name):
    """Validates that a given URL starts with http or https."""
    if url and not re.match(r"^https?://", url):
        raise SystemExit(f"[ERROR] - {var_name} must be a valid URL starting with http or https.")

validate_url(START_IMG_URL, "START_IMG_URL")
validate_url(PING_IMG_URL, "PING_IMG_URL")

def time_to_seconds(time_str: str) -> int:
    """Converts time in 'hh:mm:ss' format to seconds."""
    try:
        return sum(int(x) * 60**i for i, x in enumerate(reversed(time_str.split(":"))))
    except ValueError:
        raise SystemExit("[ERROR] - Time format must be 'hh:mm:ss'.")

# Derived configurations
DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# Pyrogram Client initialization
app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Test access to log groups
def test_group_access(client, group_id, group_type):
    """Test bot's access to the given group (LOG_GROUP_ID or LOGGER_ID)."""
    try:
        client.send_message(group_id, f"{group_type} access test successful!")
        logger.info(f"{group_type} is accessible.")
    except Exception as e:
        logger.error(f"[ERROR] - Unable to access {group_type}: {e}")
        raise SystemExit(f"[ERROR] - Check {group_type} or bot permissions.")

# Retry logic for FloodWait
def send_message_with_retry(client, chat_id, text):
    """Send a message with retry logic in case of FloodWait."""
    try:
        client.send_message(chat_id, text)
    except FloodWait as e:
        logger.warning(f"Flood wait encountered. Sleeping for {e.x} seconds.")
        time.sleep(e.x)
        send_message_with_retry(client, chat_id, text)

# Bot commands
@app.on_message(filters.command("start"))
def start(client, message):
    """Respond to the /start command."""
    message.reply_text("Bot is now running!")
    send_message_with_retry(client, LOG_GROUP_ID, "Bot started successfully!")

# Run the bot
if __name__ == "__main__":
    with app:
        # Test group access before starting
        test_group_access(app, LOG_GROUP_ID, "LOG_GROUP_ID")
        test_group_access(app, LOGGER_ID, "LOGGER_ID")
        logger.info("Starting the bot...")
        app.run()
