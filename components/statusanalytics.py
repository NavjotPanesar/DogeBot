import requests
from components.statusanalyzer import StatusAnalyzer
from config import analytics_url
from config import analytics_auth_token
from logger import Log
class StaticAnalytics:
    enabled = True
    @staticmethod
    def postAnalytic(tweetWrapper):
        if StaticAnalytics.enabled is False:
            return
        tweetId = tweetWrapper.tweetId
        username = tweetWrapper.incoming_tweet.user.screen_name
        command = tweetWrapper.tweet_command.get_command_operator()
        commandOperands = tweetWrapper.tweet_command.get_command_operands()
        timeTaken = long(tweetWrapper.finish_time - tweetWrapper.start_time)
        payload = {'token': analytics_auth_token, 'tweetId': tweetId, 'username' : username, 'command': command,'commandOperands': commandOperands, 'time': timeTaken}
        r = requests.post(analytics_url, data=payload)
        Log.v("[ANALYTICS]", r.text)