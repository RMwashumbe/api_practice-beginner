import requests


def get_news(api_key):
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        for article in articles:
            print(article['title'])
        else:
            print("Failed to fetch news.")


api_key = 'your_api_key_here'
get_news(api_key)
