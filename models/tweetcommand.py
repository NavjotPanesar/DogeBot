from logger import Log
import re
class TweetCommand:
    command_tag = "#dogebot"
    command_operator = ""
    command_operands = ""
    original_status = None

    def __init__(self, status):
        self.original_status = status #store this, so we can get the reply id. if we need more info from original tweet,
        # just add accessor to this method instead of having to add data field to this model

        self.parse_tweet(status)

    def parse_tweet(self, status):
        command_search_pattern = '(.*)' + self.command_tag + ' (.+?) (.*)'
        command_no_operand_pattern = '(.*)' + self.command_tag + ' (.+)'
        mention_search_pattern = '\B@[a-z0-9_-]+'
        text = status.text
        reply_to_name = "@" + status.user.screen_name + " "
        
        command_match = re.match(command_search_pattern, text)
        if command_match and command_match.group():
            text_before_command = command_match.group(1)
            self.command_operator = command_match.group(2)
            self.command_operands = command_match.group(3)
        else:
            command_match = re.match(command_no_operand_pattern, text)
            if command_match and command_match.group():
                text_before_command = command_match.group(1)
                self.command_operator = command_match.group(2)
                self.command_operands = ""
        
        previous_mentions = ""
        mention_search = re.findall(mention_search_pattern, text_before_command, re.I)
        if mention_search:
            previous_mentions = ( ' '.join(mention_search) )
            previous_mentions += " "

        self.reply_header = reply_to_name + previous_mentions
        Log.v("COMMAND PARSE", "rHeader: " + self.reply_header)
        Log.v("COMMAND PARSE", "command operator: " + self.command_operator)
        Log.v("COMMAND PARSE", "command operands: " + self.command_operands)
        Log.v("COMMAND PARSE", "rId: " + str(self.get_reply_to_id()))

    def get_command_operator(self):
        return self.command_operator

    def get_command_operands(self):
        return self.command_operands

    def get_reply_header(self):
        return self.reply_header

    def get_reply_to_id(self):
        return self.original_status.id
