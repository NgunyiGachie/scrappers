from googleapiclient.discovery import build
import pandas as pd
import os

API_KEY = "YOUR_YOUTUBE_API_KEY"

def scrape_youtube():
    os.makedirs("data", exist_ok=True)

    youtube = build("youtube", "v3", developerKey=API_KEY)

    request = youtube.search().list(
        q="Nike",
        part="snippet",
        maxResults=5
    )
    response = request.execute()

    videos_data = []
    for video in response["items"]:
        videos_data.append({
            "Title": video["snippet"]["title"],
            "channel": video["snippet"]["channelTitle"]
        })

    df = pd.DataFrame(videos_data)
    df.to_csv("data/nike_youtube.csv", index=False)
    print("Nike YouTube data saved")

if __name__ == "__main__":
    scrape_youtube()