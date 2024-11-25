import re
import os
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables
load_dotenv()

# Basic configurations
API_ID = os.getenv("28928028")
API_HASH = os.getenv("b097202e877124392f4851d215fa8f3a")
BOT_TOKEN = os.getenv("7339158179:AAEaxVd1pTxymc_Yeb0X2WzVFS8x4sbcvDw")
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "Username_Of_Tuhin")
BOT_USERNAME = os.getenv("BOT_USERNAME", "UtopiaMaxBot")
BOT_NAME = os.getenv("Utopia")
ASSUSERNAME = os.getenv("ASSUSERNAME")

# Database configurations
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://GOKU:MISSBHOPALI@goku.pzzsl8d.mongodb.net/?retryWrites=true&w=majority")

# Limits and durations
DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 17000))
SONG_DOWNLOAD_DURATION = int(os.getenv("SONG_DOWNLOAD_DURATION", 9999999))
SONG_DOWNLOAD_DURATION_LIMIT = int(os.getenv("SONG_DOWNLOAD_DURATION_LIMIT", 9999999))

# Owner and logging
LOGGER_ID = int(os.getenv("-1002324830715"))
OWNER_ID = int(os.getenv("7038202445"))

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

# Validation for URLs
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL URL is invalid. It must start with https://")

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Your SUPPORT_CHAT URL is invalid. It must start with https://")

# Spotify credentials
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# File size limits
TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

# Auto-assistant settings
AUTO_LEAVING_ASSISTANT = os.getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(os.getenv("ASSISTANT_LEAVE_TIME", 9000))

# Other configurations
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))
STRING_SESSIONS = [
    os.getenv(f"STRING_SESSION{i}", "BQGWS8YAsfGFbmabwHKE_DvNcV1mO3AyTJLJnZ3eT3W2ArmQTnQ9ocjWjSuLgRieW5mJps0oIGDcB6YL-KhkB6U9KXuGnV6h7mc6q9IrZR7_9VRtQ9ODUttUe4kpJH8Si3OAXH73ZvqXhUy_YYeDGd_8jtp7tfaHwGb0--iXTg67iluMshTK4qjp7X4Jru_apbTgBItb8hWeXhkWH8BDV_kqnpU2O2eb-LBkfrasGFbrVvFP_15jGbTskzK6PnegefmIwhTBq_QgAjxxD6LIqBiQLq2UI_IcYpsehl_189HMAgiWmvCC8wPkE3UaPfD3IRTPvFw2Zb8CEziR6FI_gspoaviVTgAAAAG-IuuuAA") for i in range(1, 8)
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
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
