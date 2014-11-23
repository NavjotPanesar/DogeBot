from plugins.plugins import *
from models.tweetcommand import TweetCommand
class StatusAnalyzer:
    def __init__(self):
        self.on_response_generated_listeners = []


    def add_response_generated_listener(self, observer):
        self.on_response_generated_listeners.append(observer)

    def clear_listeners(self):
        self.on_response_generated_listeners = []

    def notify_response_generated(self, status):
            for on_response_generated_listener in self.on_response_generated_listeners:
                on_response_generated_listener(status)

    def get_plugin_for_command(self, command):
            command_to_plugin_map = plugin_classes.get_command_to_plugin_map()
            return command_to_plugin_map[command]

    def generate_response_tweet(self, wrapped_tweet):
        command_tweet = TweetCommand(wrapped_tweet.get_incoming_status())
        wrapped_tweet.set_tweet_command(command_tweet)
        plugin = self.get_plugin_for_command(command_tweet.command_operator)
        response_tweet = plugin.get_response(wrapped_tweet)
        wrapped_tweet.set_tweet_command(command_tweet)
        wrapped_tweet.set_tweet_response(response_tweet)
        if wrapped_tweet.get_tweet_response() is not None:
            wrapped_tweet.print_tweet_response()
            self.notify_response_generated(wrapped_tweet)
            return wrapped_tweet.get_tweet_response()

