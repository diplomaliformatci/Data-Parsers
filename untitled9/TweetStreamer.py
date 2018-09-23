import sys
import string
import time
from tweepy import Stream
from tweepy.streaming import StreamListener
from TweeterConnector import get_twitter_auth

class Listener(StreamListener):


    def on_data(self,data):
        try:
            tweet = data.split(',"text:"')[1].split('","source')
            with open(self.outfile , 'a') as f:
                f.write(data)
                return True

        except BaseException as e:
            sys.stderr.write("error on_data: {}\n".format(e))
            time.sleep(5)

        return True

    def on_error(self,status):
        if status == 420:
            sys.stderr.write("Rate Limit Exceeded\n".format(status))
            return False
        else:
            sys.stderr.write("Error {}\n".format(status))
            return True

    def format_filename(self):