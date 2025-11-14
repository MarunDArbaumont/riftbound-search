import requests
from helper_functions.match_ids import match_ids

# retrive the content of the last match
def last_match_content (url, api_key):
    last_match_id = match_ids(url, api_key)
    last_match_content_url = url + f"tft/match/v1/matches/{last_match_id}?api_key={api_key}"
    response = requests.get(last_match_content_url)
    content = response.json()
    return content
