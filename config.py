import re
import os
from dotenv import load_dotenv
from pyrogram import filters  # Ensure Pyrogram is properly installed

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
API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "Username_Of_Tuhin")
BOT_USERNAME = os.getenv("BOT_USERNAME", "UtopiaMaxBot")
BOT_NAME = os.getenv("BOT_NAME", "Utopia")
ASSUSERNAME = os.getenv("ASSUSERNAME")

# Database configurations
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "Your_Default_MongoDB_URI")

# Limits and durations
DURATION_LIMIT_MIN = get_env_int("DURATION_LIMIT", 17000)
SONG_DOWNLOAD_DURATION = get_env_int("SONG_DOWNLOAD_DURATION", 9999999)
SONG_DOWNLOAD_DURATION_LIMIT = get_env_int("SONG_DOWNLOAD_DURATION_LIMIT", 9999999)

# Owner and logging
LOGGER_ID = get_env_int("LOGGER_ID", -1002300280815)
OWNER_ID = get_env_int("OWNER_ID", 7038202445)

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

# Validate support URLs
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit(
        "[ERROR] - SUPPORT_CHANNEL URL is invalid. It must start with https://"
    )

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit(
        "[ERROR] - SUPPORT_CHAT URL is invalid. It must start with https://"
    )

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

# Static image URLs
STATIC_IMG_URLS = {
    "PLAYLIST": "https://envs.sh/K-2.jpg",
    "TELEGRAM_AUDIO": "https://envs.sh/K-2.jpg",
    "TELEGRAM_VIDEO": "https://envs.sh/K-2.jpg",
    "STREAM": "https://envs.sh/K-2.jpg",
    "SOUNDCLOUD": "https://envs.sh/K-2.jpg",
    "YOUTUBE": "https://envs.sh/K-2.jpg",
    "SPOTIFY_ARTIST": "https://envs.sh/K-2.jpg",
    "SPOTIFY_ALBUM": "https://envs.sh/K-2.jpg",
    "SPOTIFY_PLAYLIST": "https://envs.sh/K-2.jpg",
}

# YouTube thumbnail URL format
YOUTUBE_IMG_URL = "https://img.youtube.com/vi/{video_id}/hqdefault.jpg"

# Session strings
STRING1 = os.getenv("STRING_SESSION", None)
STRING2 = os.getenv("STRING_SESSION2", None)
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)

# Helper functions
def time_to_seconds(time: str) -> int:
    """Converts time in 'hh:mm:ss' format to seconds."""
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))


# Derived configurations
DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# Filters and caches
BANNED_USERS = filters.user()  # Ensure filters is properly imported
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
