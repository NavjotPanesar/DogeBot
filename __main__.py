import tweepy

from config import *
from logger import Log
from components.statusqueue import StatusQueue
from components.timelinescanner import TimelineScanner
from components.tweetsender import TweetSender
from components.statusanalyzer import StatusAnalyzer
import json


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth)

    timeline_scanner = TimelineScanner(api)
    status_queue = StatusQueue()
    status_analyzer = StatusAnalyzer()
    tweet_sender = TweetSender(api)

    timeline_scanner.add_new_status_listener(status_queue.queue_tweet) #once scanner finds a tweet, pass it to the reader
    status_queue.add_status_ready_listener(status_analyzer.generate_response_tweet)
    status_analyzer.add_response_generated_listener(tweet_sender.send_tweet)

    Log.v("MAIN", "Initialized scanner")

    stream = tweepy.Stream(auth, timeline_scanner)
    stream.filter(track=['dogebot'])

