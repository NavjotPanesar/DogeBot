import random
import os

from abstractplugin import AbstractPlugin
from models.tweetresponse import TweetResponse
from logger import Log




#from stack overflow (http://stackoverflow.com/questions/3540288/how-do-i-read-a-random-line-from-one-file-in-python)
def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
            if random.randrange(num + 2):
                continue
                line = aline
    return line

class Donger(AbstractPlugin):
    registered_commands = ['#donger']
    text_file_loc = "resources/donger_portfolio.txt"
    def get_response(self, command):
        try:
            return self.get_dong_message(command)
        except Exception as e:
                Log.e("EXCEPTION", str(e))


    def get_dong_message(self, command):
        operator = command.get_command_operator
        if operator and os.path.isfile(self.text_file_loc) is True:
            afile = open(self.text_file_loc)
            response_text = random_line(afile)
            afile.close()

            response = TweetResponse( command, response_text )
            return response
        Log.e("DONG","file not found")