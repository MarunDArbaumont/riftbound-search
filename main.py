import requests
from variables import API_KEY, URL
from helper_functions.last_match_content import last_match_content

match_content = last_match_content(URL, API_KEY)
for participant in match_content["info"]["participants"]:
    name = participant["riotIdGameName"]
    placement = participant["placement"]
    print(f"{name} placed {placement} in your last match.")
