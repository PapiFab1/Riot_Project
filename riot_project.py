import pandas as pd
import requests as rq
from dotenv import load_dotenv
import os

#loading .env
load_dotenv()

#for now a simple function that gets the player name and tag to make it more user friendly (will need to make this work for website)
def account_info():
    game_name = input("Enter your account name: ")
    tag_name = input("Enter your tag: ")
    return game_name,tag_name
    

def playerID_API():
    api_key = (os.getenv("riot_api_key"))
    base_player_id_url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/"
    url = f"{base_player_id_url}{game_name}/{tag}/?api_key={api_key}"
    

    response = rq.get(url)
    player_id = response.json()
    print(player_id)


game_name, tag = account_info()
playerID_API()



