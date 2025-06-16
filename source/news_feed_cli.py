"""
News Digest CLI App
--------------------
This Python script fetches the latest news headlines using the GNews API.
Users can specify a country code, and the app retrieves and displays top articles,
including title, description, source, and URL.

Technologies used:
- requests: for API communication
- json: for handling API response data
"""
import requests

API_KEY = "your_gnews_api_key"
BASE_URL = "https://gnews.io/api/v4/top-headlines"

def get_top_headlines(country="gb", max_articles=5):
    params = {
        "token": "API_KEY",
        "lang": "en",
        "country": country,
        "max": max_articles
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if 'articles' not in data:
        print("Error:", data)
        return []

    return data['articles']

def print_headlines(articles):
    print("\n📰 Top Headlines:\n")
    for idx, article in enumerate(articles, 1):
        print(f"{idx}. {article['title']}")
        print(f"   {article['description']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   URL   : {article['url']}")
        print()

if __name__ == "__main__":
    country = input("Enter 2-letter country code (default GB): ") or "gb"
    articles = get_top_headlines(country)
    print_headlines(articles)
