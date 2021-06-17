#! python3
# app.py: main app to fetch and parse info from the Marvel API (http://developer.marvel.com/docs)
# and output desired data to be rendered by templates html pages.

import requests
from config import MARVEL_URL, generate_hash, app, API_PUBLIC
from pprint import pprint
from flask import render_template



def get_url_info(url: str) -> dict:
    result = requests.get(url)
    result.raise_for_status()
    result = (result.json())
    return result


def char_img(hero_id: str) -> str:
    timestamp, hash = generate_hash()
    char_url = f"http://gateway.marvel.com/v1/public/characters/{hero_id}?ts={timestamp}&apikey={API_PUBLIC}&hash={hash}"
    char_info = get_url_info(char_url)['data']['results'][0]['thumbnail']
    img_url = '/'.join([char_info['path'], "standard_xlarge"]) + '.' + char_info['extension']
    return img_url


def get_characters(story: dict) -> dict:
    chars_dict = {}
    for hero in story['characters']['items']:
        chars_dict[hero['name']] = char_img(hero['resourceURI'].split('/')[-1])
    
    return chars_dict


@app.route('/', methods = ['GET'])
def home() -> None:
    #The Marvel attribution text
    all_data = get_url_info(MARVEL_URL)
    attribution = all_data['attributionText']
    story = all_data['data']['results'][1]
    
    #The story's description
    description = story['description']
    
    #A list of names and pictures 
    # of the characters that features in the story
    characters = get_characters(story)

    #Characters pictures
    return render_template(
        'home.html', 
        description=description, 
        characters=characters, 
        attribution=attribution
    )



if __name__ == "__main__":
    app.run()
    # home()