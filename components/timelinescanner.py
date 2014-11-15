import tweepy
from logger import Log
import time
from models.tweetwrapper import TweetWrapper
class TimelineScanner(tweepy.StreamListener):

    def __init__(self, api):
        self.on_new_status_listeners = []
        self.api = api

    def add_new_status_listener(self, observer):
        self.on_new_status_listeners.append(observer)

    def notify_new_status(self, status):
        if self.on_new_status_listeners is not None:
            for on_new_tweet_listener in self.on_new_status_listeners:
                on_new_tweet_listener(status)

    def on_status(self, status):
        Log.v("TIMELINE SCANNER", "New tweet: ")
        Log.v("TWEET", status)
        tweetWrapper = TweetWrapper()
        tweetWrapper.setIncomingTweet(status)
        tweetWrapper.start_time = long(time.time() * 1000) #time in milliseconds
        self.notify_new_status(tweetWrapper)

    def on_error(self, status):
        print status