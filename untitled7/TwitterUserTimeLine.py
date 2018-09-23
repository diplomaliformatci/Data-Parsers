import sys
import json
from tweepy import Cursor
from TweeterAPI1 import get_twitter_client

if __name__ == "__main__":
    #user  = sys.argv[1]
    user = 'ayyusss'
    client = get_twitter_client()
    fname = "user_timeline_{}.json".format(user)

    with open(fname, 'w') as f:
        for page in Cursor(client.user_timeline , screen_name = user, count = 20).pages(20):
            for status in page:
                f.write(json.dumps(status._json)+"\n")
