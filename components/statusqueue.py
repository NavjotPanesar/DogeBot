import threading

from logger import Log
import traceback

class StatusQueue():

    def __init__(self):
        self.thread = threading.Thread(target=self.work_on_tweet)
        self.tweet_queue = []
        self.thread_locked = False
        self.thread = None
        self.on_status_ready_listener = []

    def clear_listeners(self):
        self.on_status_ready_listener = []

    def add_status_ready_listener(self, observer):
        self.on_status_ready_listener.append(observer)

    def notify_add_on_status_ready_listeners(self, tweet):
        if self.on_status_ready_listener is not None:
            for observer in self.on_status_ready_listener:
                observer(tweet)

    def queue_tweet(self, wrapped_tweet):
        self.tweet_queue.append(wrapped_tweet)
        Log.v("READ", "Added new tweet to queue: ")
        wrapped_tweet.print_incoming_status()
        if not self.thread_locked:
            self.thread_locked = True
            self.thread = threading.Thread(target=self.work_on_tweet)
            self.thread.start();
        else:
            return
    def work_on_tweet(self):
        if not self.tweet_queue:
            self.thread_locked = False
            return
        else:
            wrapped_tweet = self.tweet_queue[0]
            del self.tweet_queue[0]
            Log.v("QUEUE", 'doing work on tweet: ')
            wrapped_tweet.print_incoming_status()
            try:
                self.notify_add_on_status_ready_listeners(wrapped_tweet)
            except Exception as e:
                Log.report_exception(e, traceback)
            Log.v("QUEUE", 'finished work on tweet: ')
            wrapped_tweet.print_incoming_status()
            self.work_on_tweet()
