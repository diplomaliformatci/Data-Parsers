import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    """Setup Twitter authentication


    :return: tweepy.OAuthHandler object
    Twitter(auth=OAuth('MjuHWoGbzYmJv3ZuHaBvSENfyevu00NQuBc40VM','anJLBCOALCXl7aXeybmNA5oae9E03Cm23cKNMLaScuXwk','kl3E14NQx84qxO1dy247V0b2W','5VFVXVMq9bDJzFAKPfWOiYmJZin2F7YLhSfoyLBXf6Bc9ngX3g'))

    """
    try:
        consumer_key = 'kl3E14NQx84qxO1dy247V0b2W'
        consumer_secret = '5VFVXVMq9bDJzFAKPfWOiYmJZin2F7YLhSfoyLBXf6Bc9ngX3g'
        access_token = '3893134475-MjuHWoGbzYmJv3ZuHaBvSENfyevu00NQuBc40VM'
        access_secret = 'anJLBCOALCXl7aXeybmNA5oae9E03Cm23cKNMLaScuXwk'

    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)

    auth = OAuthHandler(consumer_key , consumer_secret)
    auth.set_access_token(access_token,access_secret)
    return auth

def get_twitter_client():
    """
    Setup Twitter API client

    :return: tweepy.API object
    """

    auth = get_twitter_auth()
    client = API(auth)
    return client
