import requests
import json
import datetime



def fetch_latest_news(api_key, news_keywords, lookback_days=10):
    """
    Fetch the latest news articles from NewsAPI based on keywords and lookback period.

    Args:
        api_key (str): Your NewsAPI API key.
        news_keywords (str): A string of keywords separated by commas.
        lookback_days (int): The number of days to look back for news articles (default is 10).

    Returns:
        list: A list of news articles represented as dictionaries.
    """
    # Check if the news_keywords is a alphabetic character
    if not news_keywords.isalpha():
        print("Please enter a valid keyword")
        return []
    # Calculate the date 'lookback_days' ago from the current date
    today = datetime.date.today()
    lookback_date = today - datetime.timedelta(days=lookback_days)

    # Format dates in ISO 8601 format (YYYY-MM-DD)
    today_str = today.strftime("%Y-%m-%d")
    lookback_date_str = lookback_date.strftime("%Y-%m-%d")

    # Make the request to NewsAPI
    url = f"https://newsapi.org/v2/everything?q={news_keywords}&from={lookback_date_str}&to={today_str}&sortBy=popularity&apiKey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        response_json = response.json()
        articles = response_json.get('articles', [])
        return articles
    else:
        print(f"Failed to fetch news. Status code: {response.status_code}")
        return []


if __name__ == "__main__":
    api_key = "1290da09ca1d4acea2d3388a89fe12b1"
    keywords = "rebbe"
    news_list = fetch_latest_news(api_key, keywords, lookback_days=10)
    print(news_list)
    for article in news_list:
        print(article['title'])
        print(article['url'])
        print()
