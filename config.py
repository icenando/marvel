#! python3


import os
from flask import Flask
import time
import hashlib

app = Flask(__name__)

TIMESTAMP = str(time.time()).replace(".",'')
API_PRIVATE = os.environ["API_PRIVATE"]
API_PUBLIC = os.environ["API_PUBLIC"]

# Marvel's API server-side requests hash format requirement: 
# digested md5 hash of "timestamp + private key + public key")
HASH = hashlib.md5((TIMESTAMP+API_PRIVATE+API_PUBLIC).encode()).hexdigest()

MARVEL_URL = f"https://gateway.marvel.com:443/v1/public/stories?ts={TIMESTAMP}&apikey={API_PUBLIC}&hash={HASH}"
# print(MARVEL_URL)