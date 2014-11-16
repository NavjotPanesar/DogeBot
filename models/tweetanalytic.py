__author__ = 'Navjot'

import time
class TweetAnalytic:
    def __init__(self):
        self.new_tweet_id = None
        self.reply_to_username = None
        self.plugin_name = None
        self.start_time = None
        self.end_time = None


    def get_total_time(self):
        return long(self.end_time - self.start_time)

    def track_start_time(self):
        self.start_time = self._get_time_millis()
    def track_end_time(self):
        self.end_time = self._get_time_millis()

    def _get_time_millis(self):
        timeMs = long(time.time() * 1000)
        return timeMs