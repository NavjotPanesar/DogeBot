from tweepy import *
from components.statusanalytics import StatusAnalyticsSender
from logger import Log
import time
class TweetSender:
    def __init__(self, api):
        self.api = api
    #observers = []
    #def addObserver(self, observer):
    #    self.observers.append(observer)
    #def notifyObservers(self, tweet):
    #    if self.observers is not None:
    #        for observer in self.observers:
    #            observer(tweet)
    def send_tweet(self, wrapped_tweet):
        tweet_response = wrapped_tweet.get_tweet_response()
        new_status = self.update_status(tweet_response)
        wrapped_tweet.set_new_status(new_status)
        self.send_analytic(wrapped_tweet)


    def update_status(self, tweet_response):
        if(tweet_response.get_is_image_tweet()):
            if tweet_response.get_image():
                Log.v("SEND","with image: " + Log.sanitizeOuput(tweet_response.get_status()) )
                return self.api.update_with_media("resources/doge.jpg", tweet_response.get_status(), in_reply_to_status_id=tweet_response.get_reply_to_id(), file=tweet_response.get_image())
            elif tweet_response.get_image_loc():
                Log.v("SEND","with image: " + Log.sanitizeOuput(tweet_response.get_status()) )
                return self.api.update_with_media(tweet_response.get_image_loc(), tweet_response.get_status(), in_reply_to_status_id=tweet_response.get_reply_to_id())
        else:
            Log.v("SEND", Log.sanitizeOuput(tweet_response.get_status()) )
            return self.api.update_status(tweet_response.get_status(), tweet_response.get_reply_to_id())

    def send_analytic(self, tweetWrapper):
        try:
            StatusAnalyticsSender.post_analytic(tweetWrapper)
        except Exception as e:
                Log.e("EXCEPTION", str(e))