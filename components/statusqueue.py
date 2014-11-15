import threading

from logger import Log


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

    def queue_tweet(self, tweetWrapper):
        self.tweet_queue.append(tweetWrapper)
        Log.v("READ", "Added new tweet to queue: ")
        Log.v("TWEET", tweetWrapper.incoming_tweet)
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
            tweetWrapper = self.tweet_queue[0]
            del self.tweet_queue[0]
            Log.v("QUEUE", 'doing work on tweet: ')
            Log.v("TWEET", tweetWrapper.incoming_tweet)
            try:
                self.notify_add_on_status_ready_listeners(tweetWrapper)
            except Exception as e:
                Log.e("EXCEPTION", str(e))
            Log.v("QUEUE", 'finished work on tweet: ')
            Log.v("TWEET", tweetWrapper.incoming_tweet)
            self.work_on_tweet()
