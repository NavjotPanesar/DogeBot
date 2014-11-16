__author__ = 'Navjot'

from tweetanalytic import TweetAnalytic
from logger import Log
class TweetWrapper:

    def __init__(self):
        self._status_incoming = None
        self._tweet_command = None
        self._tweet_response = None
        self.tweet_analytic = TweetAnalytic()

    def set_incoming_status(self, status):
        self._status_incoming = status
        self.tweet_analytic.track_start_time()
        self.tweet_analytic.reply_to_username = status.user.screen_name

    def get_incoming_status(self):
        return self._status_incoming

    def print_incoming_status(self):
        Log.v("TWEET", self._status_incoming)

    def set_tweet_command(self, tweet_command):
        self._tweet_command = tweet_command
        self.tweet_analytic.plugin_name = tweet_command.plugin_name

    def get_tweet_command(self):
        return self._tweet_command

    def get_tweet_response(self):
        return self._tweet_response

    def set_tweet_response(self, tweet_response):
        self._tweet_response = tweet_response
        self.tweet_analytic.track_end_time()

    def print_tweet_response(self):
        Log.v("ANALYZER","response received: " + Log.sanitizeOuput(self._tweet_response))

    def set_new_status(self, new_status):
        self._new_status = new_status
        self.tweet_analytic.new_tweet_id = new_status.id