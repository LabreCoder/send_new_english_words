import requests

def get_random_word():
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    '''
    if response.status_code != 200 and response.status_code != 500:
        return sys.exit(1)
    
    elif response.status_code == 500:
        return sys.exit(1)
    else: 
        return response.json()[0]
    '''
    return response.json()[0]

