from logger import Log
import re
class TweetCommand:
    command_tag = "#dogebot"

    def __init__(self, status):
        self.parse_tweet(status)
        self.plugin_name = self.command_operator

    def parse_tweet(self, status):
        self.command_operator = ""
        self.command_operands = ""
        self.reply_to_id = status.id
        command_search_pattern = '(.*)' + self.command_tag + ' (.+?) (.*)'
        command_no_operand_pattern = '(.*)' + self.command_tag + ' (.+)'
        mention_search_pattern = '\B@[a-z0-9_-]+'
        text = status.text
        reply_to_name = "@" + status.user.screen_name + " "
        
        command_match = re.match(command_search_pattern, text)
        text_before_command = ""
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
        Log.v("COMMAND PARSE", "Reply Header: " + self.reply_header)
        Log.v("COMMAND PARSE", "command operator: " + self.command_operator)
        Log.v("COMMAND PARSE", "command operands: " + self.command_operands)
        Log.v("COMMAND PARSE", "reply Id: " + str(self.get_reply_to_id()))

    def get_command_operator(self):
        return self.command_operator

    def get_command_operands(self):
        return self.command_operands

    def get_reply_header(self):
        return self.reply_header

    def get_reply_to_id(self):
        return self.reply_to_id
