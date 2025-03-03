import instaloader
import pandas as pd
import os

def scrape_instagram():
    os.makedirs("data", exist_ok=True)

    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, "nike")

    posts_data = []
    for post in profile.get_posts():
        posts_data.append({
            "Date": post.date,
            "Likes": post.likes,
            "Comments": post.comments,
            "Caption": post.caption[:100]
        })

    df = pd.DataFrame(posts_data)
    df.to_csv("data/nike_instagram_csv", index=False)
    print("Nike Instagram data saved")

if __name__== "__main__":
    scrape_instagram()