from tweepy import Cursor
from TweeterAPI1 import get_twitter_client
import json

if __name__ == "__main__":
    client = get_twitter_client()

    with open('home_timeline1.jsonl','w') as f:
        for page in Cursor(client.home_timeline,count=200).pages(4):
            for status in page:
                f.write(json.dumps(status._json)+"\n")