import requests
from helper_functions.find_account import find_account

# retrive last match id
def match_ids(url, api_key):
    puuid = find_account(url, api_key)
    match_ids_url = url + f"tft/match/v1/matches/by-puuid/{puuid}/ids?start=0&count=1&api_key={api_key}"
    resp = requests.get(match_ids_url)
    match_id = resp.json()[0]
    return match_id
