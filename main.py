import requests
from variables import API_KEY, URL
from helper_functions.last_match_content import last_match_content


def main():
    match_content = last_match_content(URL, API_KEY)
    final_result = [None, None, None, None, None, None, None, None]
    for participant in match_content["info"]["participants"]:
        name = participant["riotIdGameName"]
        placement = participant["placement"]
        final_result[placement - 1] = name

    for i in range(len(final_result)):
        print(f"#{i + 1} {final_result[i]}")

main()
