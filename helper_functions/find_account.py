import requests

def find_account(url, api_key):
    account_name = input("Enter your account name: ")
    correct_account_name = account_name.replace(" ", "%20")
    account_tag = input("Enter your account tag (e.g. EUW): ")
    account_url = url + f"riot/account/v1/accounts/by-riot-id/{correct_account_name}/{account_tag}?api_key={api_key}"
    resp = requests.get(account_url)
    puuid = resp.json()["puuid"]
    print(puuid)
    return puuid
