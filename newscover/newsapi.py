import requests
#import json
import datetime


def check_timeframe(news_list, lookback_days):
    """ 
    Check if the news articles are within the timeframe.    
    Args:
        news_list (list): A list of news articles represented as dictionaries.
        lookback_days (int): The number of days to look back for news articles.
    Returns:
        bool: True if all news articles are within the timeframe, False otherwise.
    """ 
    # Calculate the dates
    today = datetime.date.today()
    lookback_date = today - datetime.timedelta(days=lookback_days)
    # Check if the dates are valid
    for article in news_list:
        article_date = datetime.datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ").date()
        if article_date < lookback_date:
            return False
    return True

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
    
    # Calculate the dates
    today = datetime.date.today()
    lookback_date = today - datetime.timedelta(days=lookback_days)
    # Convert the dates to strings
    today_str = today.strftime("%Y-%m-%d")
    lookback_date_str = lookback_date.strftime("%Y-%m-%d")
    # Fetch the news
    url = f"https://newsapi.org/v2/everything?q={news_keywords}&from={lookback_date_str}&to={today_str}&sortBy=popularity&apiKey={api_key}"
    response = requests.get(url)
    # Check if the timeframe is valid
    if not check_timeframe(response.json().get('articles', []), lookback_days):
        print("Please enter a valid timeframe")
        return []
    # Check if the response is valid
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
