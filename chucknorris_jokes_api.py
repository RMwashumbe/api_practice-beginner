import requests

def get_joke():
    url = 'http://api.icndb.com/jokes/random'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        joke = data['value']['joke']
        print(joke)
    else:
        print("Failed to fetch joke.")

get_joke()