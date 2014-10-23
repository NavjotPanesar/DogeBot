from abstractplugin import AbstractPlugin
from models.tweetresponse import TweetResponse
class Parrot(AbstractPlugin):
    registered_commands = ['#parrot']

    def get_response(self, command):
        operands = command.get_command_operands()
        if operands:
            response_text = operands + ", Woof "
            response = TweetResponse( command, response_text )
            return response