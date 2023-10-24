import unittest
from newscover.newsapi import fetch_latest_news, check_timeframe

class TestNewsAPI(unittest.TestCase):
    def test_no_news_keyword(self):
        api_key = "1290da09ca1d4acea2d3388a89fe12b1"
        keywords = ""
        news_list = fetch_latest_news(api_key, keywords, lookback_days=10)
        self.assertEqual(len(news_list), 0)
    
    def test_outside_timeframe(self):
        api_key = "1290da09ca1d4acea2d3388a89fe12b1"
        keywords = "rebbe"
        new_list = check_timeframe(fetch_latest_news(api_key, keywords, lookback_days=10), 10)
        self.assertEqual(new_list, True)
        
    def test_non_alphabetic_keyword(self):
        api_key = "1290da09ca1d4acea2d3388a89fe12b1"
        non_alphabetic_keywords = "catch22"  
        news_list = fetch_latest_news(api_key, non_alphabetic_keywords, lookback_days=10)
        self.assertEqual(len(news_list), 0) 


if __name__ == "__main__":
    unittest.main()
