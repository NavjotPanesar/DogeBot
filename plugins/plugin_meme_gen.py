from abstractplugin import AbstractPlugin
from models.tweetresponse import TweetResponse
import re

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from cStringIO import StringIO


class ExplicitMemeGen(AbstractPlugin):
    registered_commands = ['#meme']
    def get_response(self, command):
        syntax_pattern = '#(.+?) (.+?),\s?(.+)'
        syntax_match = re.match(syntax_pattern, command.get_command_operands())
        if syntax_match and syntax_match.group():
            img = syntax_match.group(1)
            line1 = syntax_match.group(2)
            line2 = syntax_match.group(3)
            response = TweetResponse( command, "" )
            src_file = MemeGenerator.generate_custom(line1, line2, 'resources/' + img + '.jpg')
            response.set_image(src_file)
            return response
        raise Exception("Argument count mismatch")

class ImplicitMemeGen(AbstractPlugin):
    registered_commands = ["#doge", "#henry", "#steve" , "#uzyr", "#dogdre", "#gdre", "#shaun", "#rosen", "#abster", "#tspinner", "#henrythresh", "#ssjfarhan", "#hamza","#clarinetboy]
    def get_response(self, command):
        syntax_pattern = '(.+?),\s?(.+)'
        syntax_match = re.match(syntax_pattern, command.get_command_operands())
        if syntax_match and syntax_match.group():
            img = command.get_command_operator().replace("#","")
            line1 = syntax_match.group(1)
            line2 = syntax_match.group(2)
            response = TweetResponse( command, "" )
            src_file = MemeGenerator.generate_custom(line1, line2, 'resources/' + img + '.jpg')
            response.set_image(src_file)
            return response
        raise Exception("Argument count mismatch")


class MemeGenerator:
    @staticmethod
    def generate_custom(topString, bottomString,  image):
        topString = topString.decode('string_escape')
        bottomString = bottomString.decode('string_escape')
        img = Image.open(image)
        imageSize = img.size

        # find biggest font size that works
        fontSize = imageSize[1]/5
        font = ImageFont.truetype("resources/impact.ttf", fontSize)
        topTextSize = font.getsize(topString)
        bottomTextSize = font.getsize(bottomString)
        while topTextSize[0] > imageSize[0]-20 or bottomTextSize[0] > imageSize[0]-20:
            fontSize = fontSize - 1
            font = ImageFont.truetype("resources/impact.ttf", fontSize)
            topTextSize = font.getsize(topString)
            bottomTextSize = font.getsize(bottomString)

        # find top centered position for top text
        topTextPositionX = (imageSize[0]/2) - (topTextSize[0]/2)
        topTextPositionY = 0
        topTextPosition = (topTextPositionX, topTextPositionY)

        # find bottom centered position for bottom text
        bottomTextPositionX = (imageSize[0]/2) - (bottomTextSize[0]/2)
        bottomTextPositionY = (imageSize[1] - bottomTextSize[1]) - 20
        bottomTextPosition = (bottomTextPositionX, bottomTextPositionY)

        draw = ImageDraw.Draw(img)

        # draw outlines
        # there may be a better way
        outlineRange = fontSize/15
        for x in range(-outlineRange, outlineRange+1):
            for y in range(-outlineRange, outlineRange+1):
                draw.text((topTextPosition[0]+x, topTextPosition[1]+y), topString, (0,0,0), font=font)
                draw.text((bottomTextPosition[0]+x, bottomTextPosition[1]+y), bottomString, (0,0,0), font=font)

        draw.text(topTextPosition, topString, (255,255,255), font=font)
        draw.text(bottomTextPosition, bottomString, (255,255,255), font=font)

        output = StringIO()
        img.save(output, format='JPEG')
        output.seek(0)
        return output
