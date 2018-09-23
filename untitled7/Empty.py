from TweeterAPI1 import get_twitter_client
import json
client = get_twitter_client()
profile = client.get_user(screen_name='mkcgrbz')
print(json.dumps(profile._json,indent=4))