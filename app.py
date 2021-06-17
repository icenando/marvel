#! python3
# app.py: main app to fetch and parse info from the Marvel API (http://developer.marvel.com/docs)
# and output desired data to be rendered by templates html pages.

import requests
from config import MARVEL_URL
from pprint import pprint

from flask import Flask, render_template

app = Flask(__name__)


def get_story() -> dict:
    result = requests.get(MARVEL_URL)
    result.raise_for_status()
    result = (result.json())
    return [
        result['attributionText'], 
        result['data']['results'][1]
    ]


def get_characters(story: dict) -> dict:
    characters_dict = {}
    
    for hero in story['characters']['items']:
        characters_dict[hero['name']] = hero['resourceURI']
    
    return characters_dict


@app.route('/', methods = ['GET'])
def home() -> None:
    #The Marvel attribution text
    attribution, story = get_story()
    
    #The story's description
    description = story['description']
    
    #A list of names and pictures 
    # of the characters that features in the story
    characters = get_characters(story)


    return render_template('home.html', description=description, characters=characters, attribution=attribution)



if __name__ == "__main__":
    app.run()