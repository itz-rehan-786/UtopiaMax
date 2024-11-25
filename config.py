import re
import os
from dotenv import load_dotenv
from pyrogram import filters  # Ensure this is properly imported

# Load environment variables
load_dotenv()

# Function to fetch and validate integer environment variables
def get_env_int(var_name, default_value):
    """Fetch environment variable as an integer or return the default."""
    value = os.getenv(var_name, default_value)
    try:
        return int(value)
    except (ValueError, TypeError):
        raise SystemExit(f"[ERROR] - The environment variable '{var_name}' must be a valid integer. Current value: {value}")

# Basic configurations
API_ID = os.getenv("API_ID", "Your_Default_API_ID")
API_HASH = os.getenv("API_HASH", "Your_Default_API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN", "Your_Default_BOT_TOKEN")
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
LOGGER_ID = get_env_int("LOGGER_ID", -1002252184024)
OWNER_ID = get_env_int("OWNER_ID", 7038202445)

# Debugging
print(f"LOGGER_ID: {LOGGER_ID}, OWNER_ID: {OWNER_ID}")

# Heroku configurations
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

# Git repository
UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/VIPBOLTE/GOKUMUSIC.git")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

# Support links
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/Kayto_Official")
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/Anime_Chat_Group_Community")

# Validate URLs
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL URL is invalid. It must start with https://")

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - SUPPORT_CHAT URL is invalid. It must start with https://")

# Spotify credentials
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "Your_Default_Spotify_Client_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "Your_Default_Spotify_Client_Secret")

# File size limits
TG_AUDIO_FILESIZE_LIMIT = get_env_int("TG_AUDIO_FILESIZE_LIMIT", 5242880000)
TG_VIDEO_FILESIZE_LIMIT = get_env_int("TG_VIDEO_FILESIZE_LIMIT", 5242880000)

# Auto-assistant settings
AUTO_LEAVING_ASSISTANT = os.getenv("AUTO_LEAVING_ASSISTANT", "True").lower() == "true"
AUTO_LEAVE_ASSISTANT_TIME = get_env_int("ASSISTANT_LEAVE_TIME", 9000)

# Other configurations
PLAYLIST_FETCH_LIMIT = get_env_int("PLAYLIST_FETCH_LIMIT", 25)
STRING_SESSIONS = [
    os.getenv(f"STRING_SESSION{i}", None) for i in range(1, 8)
]

# Image URLs
START_IMG_URL = os.getenv(
    "START_IMG_URL", "https://graph.org/file/364a09ddd47378efaecfb-2d3ae182ccf44e9087.jpg"
)
PING_IMG_URL = os.getenv(
    "PING_IMG_URL", "https://graph.org/file/35ef624f376e22a0fa1d7-1ea63e464ea9f36fab.jpg"
)

# Static Image URLs
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

# Helper functions
def time_to_seconds(time: str) -> int:
    """Converts time in 'hh:mm:ss' format to seconds."""
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# Filters and caches
BANNED_USERS = filters.user()  # Ensure filters is properly imported
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
