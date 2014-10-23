#Just a blackboard of bot plugins trying to respond to the tweet
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

    def notify_reponse_generated(self, status):
            for on_response_generated_listener in self.on_response_generated_listeners:
                on_response_generated_listener(status)

    def add_plugin(self, plugin):
        self.plugin_list.append(plugin)

    def load_plugins(self):
        for pluginName in pluginList:
            pluginClass = getattr(pluginClasses, pluginName)
            plugin = pluginClass()
            self.add_plugin(plugin)

    def generate_response_tweet(self, incoming_tweet):
        if self.plugin_list is not None:
            command_tweet = TweetCommand(incoming_tweet)
            for single_plugin in self.plugin_list:
                is_supported = single_plugin.is_command_supported( command_tweet.get_command_operator() )
                if is_supported:
                    response_tweet = single_plugin.get_response(command_tweet)
                    if response_tweet is not None:
                        Log.v("ANALYZER","response received: " + Log.sanitizeOuput(response_tweet))
                        self.notify_reponse_generated(response_tweet)
                        return response_tweet
