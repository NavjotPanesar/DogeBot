#Just a blackboard of bot plugins trying to respond to the tweet, TODO: use a hashmap lookup instead.
from plugins.plugins import *
from logger import Log
from models.tweetcommand import TweetCommand
class StatusAnalyzer:
    plugin_list = []
    def __init__(self):
        self.load_plugins()
        self.on_response_generated_listeners = []


    def add_response_generated_listener(self, observer):
        self.on_response_generated_listeners.append(observer)

    def clear_listeners(self):
        self.on_response_generated_listeners = []

    def notify_response_generated(self, status):
            for on_response_generated_listener in self.on_response_generated_listeners:
                on_response_generated_listener(status)

    def add_plugin(self, plugin):
        self.plugin_list.append(plugin)

    def load_plugins(self):
        for pluginName in pluginList:
            pluginClass = getattr(pluginClasses, pluginName)
            plugin = pluginClass()
            self.add_plugin(plugin)

    def generate_response_tweet(self, wrapped_tweet):
        if self.plugin_list is not None:
            command_tweet = TweetCommand(wrapped_tweet.get_incoming_status())
            wrapped_tweet.set_tweet_command(command_tweet)
            for single_plugin in self.plugin_list:
                is_supported = single_plugin.is_command_supported( command_tweet.get_command_operator() )
                if is_supported:
                    response_tweet = single_plugin.get_response(wrapped_tweet)
                    wrapped_tweet.set_tweet_command(command_tweet)
                    wrapped_tweet.set_tweet_response(response_tweet)
                    if wrapped_tweet.get_tweet_response() is not None:
                        wrapped_tweet.print_tweet_response()
                        self.notify_response_generated(wrapped_tweet)
                        return wrapped_tweet.get_tweet_response()
