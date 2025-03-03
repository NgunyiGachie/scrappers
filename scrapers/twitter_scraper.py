import snscrape.modules.twitter as sntwitter
import pandas as pd
import os

def scrape_twitter():
    os.makedirs("data", exist_ok=True)

    query = "Nike since:2024-01-01 until:2024-03-01"
    tweets = []

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        tweets.append([tweet.date, tweet.content, tweet.likecount, tweet.retweetCount])

    df = pd.DataFrame(tweets, columns=["Date", "Tweet", "Likes", "Retweets"])
    df.to_csv("data/nike_twitter.csv", index=False)
    print("Nike Twitter data saved")

if __name__ == "__main__":
    scrape_twitter()