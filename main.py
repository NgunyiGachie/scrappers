import os
from scrapers.instagram_scraper import scrape_instagram
from scrapers.twitter_scraper import scrape_twitter
from scrapers.youtube_scraper import scrape_youtube

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)

    print("Starting data scraping....")
    scrape_instagram()
    scrape_twitter()
    scrape_youtube()
    print("All data scraped and saved successfully")