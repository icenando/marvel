#! python3
# Config variables for app.py.

import os
import time
import hashlib


CHARACTER_ID = "1009362" #iceman
COMIC_ID = "13881"

TIMESTAMP = str(time.time()).replace(".",'')
API_PRIVATE = os.environ["API_PRIVATE"]
API_PUBLIC = os.environ["API_PUBLIC"]

# Marvel's API server-side requests hash format requirement: digested md5 hash of "timestamp + private key + public key")
HASH = hashlib.md5((TIMESTAMP+API_PRIVATE+API_PUBLIC).encode()).hexdigest()

MARVEL_URL = f"https://gateway.marvel.com:443/v1/public/comics/{COMIC_ID}/stories?ts={TIMESTAMP}&apikey={API_PUBLIC}&hash={HASH}"