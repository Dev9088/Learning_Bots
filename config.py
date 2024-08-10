import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = 23205730
API_HASH = "ab6988be4e4f0461cc7d52635769405c"
BOT_TOKEN = "7431806618:AAFIUpJ1B4ewS09tgNMklbXtEXW0wgj_cHE"
MONGO_DB_URI = ""
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))
LOGGER_ID = -1002112549809
OWNER_ID = 6055819019

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnonymousX1025/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/NETFLIXHUBULTRA")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/NETFLIXHUBCHATS")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = "BQFiF2sAoqm54JOJY2Euw13-XOafxSNPUKjrw8wHx_JcEvolEROr9wtODRKzA-s0mTYRExsujlEFF14I-LZaUY7-kSgYeQrbLD4OQR9KppBV-ww57d5dskJ5v_N8TYCMCTtWYZRU2yGF2L6yG7xHx1ZMdjoartGSeRbjTCX4CarSbb1-xdPL4me919anYB4jmtoKtffl-Cqo1BfjF-NftpX_jSS9gZ3efksUcObezJJB62_5-AeujmrzzxF68F_6pKa-tjxbquWrLw40JXgDVppRb5cedidRGCKGuaGpE0yljalL-oFNbtp9lbtO9LvhfjALjMiPxBfGQt3PzefJXONZbn9BEwAAAAFo9HcLAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/748d933b7010000ed5e10.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/748d933b7010000ed5e10.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/748d933b7010000ed5e10.jpg"
STATS_IMG_URL = "https://graph.org/file/748d933b7010000ed5e10.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/748d933b7010000ed5e10.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/748d933b7010000ed5e10.jpg"
STREAM_IMG_URL = "https://graph.org/file/748d933b7010000ed5e10.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/748d933b7010000ed5e10.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/748d933b7010000ed5e10.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/748d933b7010000ed5e10.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/748d933b7010000ed5e10.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/748d933b7010000ed5e10.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
