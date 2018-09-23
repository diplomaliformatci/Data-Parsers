import os
import json
import facebook
import requests

if __name__ == '__main__':
    token = 'EAACEdEose0cBAD6XpBrSh2PbppDy224r1kAQX0kXIbLvstWGDrxDnJlLQPVzVIVjIPlhLZCVRvQ2G7mGIeGLKZCSLMB2qwSpNfVDyvGmwazneIFtiZCMdqdYuY6ECDjVVuiLfkID9aXdjBPx7othHoQ6YvY31iUf0rRdZA3ADAZDZD'
    graph = facebook.GraphAPI(token)
    posts = graph.get_connections('me','posts')

    while True:
        try:
            with open('my_posts.jsonl' , 'a') as f:
                for post in posts['data']:
                    f.write(json.dumps(post)+"\n")

                posts = requests.get(posts['paging']['next']).json()

        except KeyError:
            break

