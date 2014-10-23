from tweepy import *
from logger import Log
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
    def send_tweet(self, tweet):
        if(tweet.get_is_image_tweet()):
            if tweet.get_image():
                self.api.update_with_media("resources/doge.jpg", tweet.get_status(), in_reply_to_status_id=tweet.get_reply_to_id(), file=tweet.get_image())
                Log.v("SEND","with image: " + Log.sanitizeOuput(tweet.get_status()) )
            elif tweet.get_image_loc():
                self.api.update_with_media(tweet.get_image_loc(), tweet.get_status(), in_reply_to_status_id=tweet.get_reply_to_id())
                Log.v("SEND","with image: " + Log.sanitizeOuput(tweet.get_status()) )
        else:
            self.api.update_status(tweet.get_status(), tweet.get_reply_to_id())
            Log.v("SEND", Log.sanitizeOuput(tweet.get_status()) )
