class TweetResponse:
    is_image_tweet = False
    reply_header = ""
    body = ""
    reply_id = ""
    image = ""
    
    def __init__(self, command, body):
        self.reply_header = command.get_reply_header().decode('utf-8')
        self.body = body.decode('utf-8')
        self.reply_id = command.get_reply_to_id()
        self.is_image_tweet = False
    
    def set_image(self, image):
        self.is_image_tweet = True
        self.image = image

    def set_image_loc(self, image_loc):
        self.is_image_tweet = True
        self.image_loc = image_loc
    
    def get_status(self):
        return self.reply_header + self.body

    def get_reply_to_id(self):
        return self.reply_id
        
    def get_is_image_tweet(self):
        return self.is_image_tweet
        
    def get_image(self):
        if(not self.is_image_tweet):
            return None
        else:
            return self.image

    def get_image_loc(self):
        return self.image_loc