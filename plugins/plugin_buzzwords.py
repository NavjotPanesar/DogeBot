from abstractplugin import AbstractPlugin
from models.tweetresponse import TweetResponse
class Buzzwords(AbstractPlugin):
    registered_commands = ['#smite','#rekt','#dealwithit','#swag']
    #TODO: add image check to unit test for this
    def get_response(self, command):
        operator = command.get_command_operator()
        if operator == "#smite":
            response_text = "Get smitten, scrub"
            response = TweetResponse( command, response_text )
            response.set_image_loc('resources/smite.jpg')
            return response

        if operator == "#rekt":
            response_text = "get #REKT"
            response = TweetResponse( command, response_text )
            response.set_image_loc('resources/rekt.gif')
            return response

        if operator == "#dealwithit":
            response_text = "deal with it"
            response = TweetResponse( command, response_text )
            response.set_image_loc('resources/dealwithit.gif')
            return response

        if operator == "#swag":
            response_text = "swag"
            response = TweetResponse( command, response_text )
            response.set_image_loc('resources/swag.jpg')
            return response
