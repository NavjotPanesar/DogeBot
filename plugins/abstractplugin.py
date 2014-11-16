import abc
class AbstractPlugin:
    __metaclass__ = abc.ABCMeta
    @abc.abstractproperty
    def registered_commands(self):
        return ["should be implemented","ok"]

    def is_command_supported(self, command_text):
        for registered_command in self.registered_commands:
            if command_text == registered_command:
                return True
        return False

    @abc.abstractmethod
    def get_response(self, tweet_wrapper):
        """
        :param status: input is models/tweetcommand
        :return: output models/tweetresponse if the plugin has registered for the incoming command
        """