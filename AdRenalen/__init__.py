from AdRenalen.core.bot import Omar
from AdRenalen.core.dir import dirr
from AdRenalen.core.git import git
from AdRenalen.core.userbot import Userbot
from AdRenalen.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Omar()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
