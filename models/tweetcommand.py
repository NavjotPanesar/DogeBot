from logger import Log
import re
from plugins.plugins import *

class TweetCommand:

    def __init__(self, status):
        self.parse_tweet(status)
        self.plugin_name = self.command_operator

    def parse_tweet(self, status):
        self.command_operator = ""
        self.command_operands = ""
        self.reply_to_id = status.id

        command_tag_alternation = ""
        command_tags = plugin_classes.get_commands_list()
        for command_tag in command_tags:
            command_tag_alternation += command_tag + "|"
        command_tag_alternation = command_tag_alternation[:-1]
        command_search_pattern = '(.*)(' + command_tag_alternation + ')\s*(.*)'

        text = status.text

        self._extract_command_info(command_search_pattern, text)

        reply_to_name = "@" + status.user.screen_name + " "
        self._generate_reply_header(reply_to_name)


        Log.v("COMMAND PARSE", "Reply Header: " + self.reply_header)
        Log.v("COMMAND PARSE", "command operator: " + self.command_operator)
        Log.v("COMMAND PARSE", "command operands: " + self.command_operands)
        Log.v("COMMAND PARSE", "reply Id: " + str(self.get_reply_to_id()))

    def _extract_command_info(self, command_search_pattern, text):
            command_match = re.match(command_search_pattern, text, re.IGNORECASE)
            if command_match and command_match.group():
                self.text_before_command = command_match.group(1)
                self.command_operator = command_match.group(2)
                self.command_operator = self.command_operator.lower()
                self.command_operands = command_match.group(3)

    def _generate_reply_header(self, reply_to_name):
        mention_search_pattern = '\B@[a-z0-9_-]+'
        previous_mentions = ""
        mention_search = re.findall(mention_search_pattern, self.text_before_command, re.I)
        if mention_search:
            previous_mentions = ( ' '.join(mention_search) )
            previous_mentions += " "
        self.reply_header = reply_to_name + previous_mentions

    def get_command_operator(self):
        return self.command_operator

    def get_command_operands(self):
        return self.command_operands

    def get_reply_header(self):
        return self.reply_header

    def get_reply_to_id(self):
        return self.reply_to_id