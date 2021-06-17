#! python3
# app.py: main app to fetch and parse info from the Marvel API (http://developer.marvel.com/docs)
# and output desired data to be rendered by templates html pages.

import requests
from config import MARVEL_URL
from pprint import pprint


def api_request() -> requests:
    result = requests.get(MARVEL_URL)
    result.raise_for_status()

    result = result.json()
    pprint(result)

if __name__ == "__main__":
    api_request()