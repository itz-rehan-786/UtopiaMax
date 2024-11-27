from GOKUMUSIC.core.bot import GOKU
from GOKUMUSIC.core.dir import dirr
from GOKUMUSIC.core.git import git
from GOKUMUSIC.core.userbot import Userbot
from GOKUMUSIC.music import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Aviax()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
