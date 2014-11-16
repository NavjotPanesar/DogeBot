import requests
from components.statusanalyzer import StatusAnalyzer
from config import analytics_url
from config import analytics_auth_token
from logger import Log
class StatusAnalyticsSender:
    enabled = True
    @staticmethod
    def post_analytic(tweetWrapper):
        if StatusAnalyticsSender.enabled is False:
            return
        tweet_analytic = tweetWrapper.tweet_analytic
        tweetId = tweet_analytic.new_tweet_id
        username = tweet_analytic.reply_to_username
        command = tweet_analytic.plugin_name
        commandOperands = tweetWrapper.get_tweet_command().get_command_operands()
        timeTaken = tweet_analytic.get_total_time()
        payload = {'token': analytics_auth_token, 'tweetId': tweetId, 'username' : username, 'command': command,'commandOperands': commandOperands, 'time': timeTaken}
        print payload
        r = requests.post(analytics_url, data=payload)
        Log.v("[ANALYTICS]", r.text)