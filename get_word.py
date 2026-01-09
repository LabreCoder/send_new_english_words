import requests

def get_random_word():
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()[0]

