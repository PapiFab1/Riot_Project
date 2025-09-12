import pandas as pd
import requests as rq
import json
from dotenv import load_dotenv
import os

#loading .env
load_dotenv()

#for now a simple function that gets the player name and tag to make it more user friendly (will need to make this work for website) URLS ONLY WORK FOR NA
def account_info():
    game_name = input("Enter your account name: ")
    tag_name = input("Enter your tag: ")
    return game_name,tag_name
    
#grabs puuid from riot
def playerID_API():
    api_key = os.getenv("riot_api_key")
    base_player_id_url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/"
    url = f"{base_player_id_url}{game_name}/{tag}/?api_key={api_key}"
    

    response = rq.get(url)
    player_id = response.json()
    

    puuid = player_id["puuid"]
    return puuid

#return match ids for last 5 matches
def match_ID_API(playerID):
    api_key = os.getenv("riot_api_key")
    base_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/"
    url = f"{base_url}{playerID}/ids?start=0&count=20&api_key={api_key}"

    response = rq.get(url)
    match_id = response.json()
    return match_id[:5]

   
#only does one match at a time for now. Will need to update to iterate through 5 matches
def player_stats_API(match_ID, player_ID):
    api_key = os.getenv("riot_api_key")
    base_url = "https://americas.api.riotgames.com/lol/match/v5/matches/"
    url = f"{base_url}{match_ID}/?api_key={api_key}"

    response = rq.get(url)
    #turn response into a dictionary so it can be used
    data = response.json()
    participants = data["metadata"]["participants"]
    player_index = participants.index(player_ID)
    print(data["info"]["participants"][player_index]["summonerName"])
    print(" ")
    
    c = data["info"]["participants"][player_index]["championName"]
    k = data["info"]["participants"][player_index]["kills"]
    d = data["info"]["participants"][player_index]["deaths"]
    a = data["info"]["participants"][player_index]["assists"]

    print(f"Champion: {c}")
    print(f"Kills: {k}")
    print(f"Deaths: {d}")
    print(f"Assists: {a}\n")


game_name, tag = account_info()
playerID = playerID_API()
match_ID = match_ID_API(playerID)

for i in match_ID:
    player_stats_API(i,playerID)


    
    



