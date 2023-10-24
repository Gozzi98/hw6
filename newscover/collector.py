import json
import os
import argparse
from newscover.newsapi import fetch_latest_news



def collect_news(api_key, input_file, output_dir, lookback_days=10):
    # Read keyword sets from the input JSON file
    with open(input_file, "r") as input:
        keyword_sets = json.load(input)

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through each keyword set and fetch news
    for name, keywords in keyword_sets.items():
        keywords_str = ",".join(keywords)
        news_data = fetch_latest_news(api_key, keywords_str, lookback_days)

        if news_data:
            output_file = os.path.join(output_dir, f"{name}.json")
            with open(output_file, "w") as output:
                json.dump(news_data, output)

def main():
    parser = argparse.ArgumentParser(description="News Article Collector")
    parser.add_argument("-k", "--api_key", required=True, help="NewsAPI API Key")
    parser.add_argument("-b", "--days_to_lookback", type=int, default=10, help="Number of days to look back for news")
    parser.add_argument("-i", "--input_file", required=True, help="Input JSON file with keyword sets")
    parser.add_argument("-o", "--output_dir", required=True, help="Output directory for JSON files")

    args = parser.parse_args()
    
    collect_news(args.api_key, args.input_file, args.output_dir, args.days_to_lookback)

if __name__ == "__main__":
    main()