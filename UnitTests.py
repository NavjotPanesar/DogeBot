import unittest
import base64
import time

from components.statusanalyzer import StatusAnalyzer
from components.statusqueue import StatusQueue
from logger import Log
from plugins.plugin_meme_gen import MemeGenerator

class User:
    screen_name = ""
    def __init__(self, name):
        self.screen_name = name

class StatusMock:
    user = None
    text = ""
    id = 1
    def __init__(self, text, name):
        self.user = User(name)
        self.text = text
        self.id = 123456


class TestEnd2End(unittest.TestCase):
    response = []

    def setUp(self):
        self.response = []
        Log.showV = False
        Log.v("TEST", "NEW TEST---------------------------------------")

    def handleResponse(self, tweet):
        self.response.append(tweet)

    def buildMockTweet(self, text):
        returnedTweet= StatusMock(text, "n4vjot")
        return returnedTweet

    def postTweetToBot(self, reader, tweet):
        reader.queue_tweet(tweet)

    def waitForResponse(self, count):
        while len(self.response) < count:
            pass;#wait

    def getResponse(self, response_number):
        return self.response[response_number - 1]

    def returnedTweetContains(self, tweet, text):
        tweet_text = tweet.get_status().encode('ascii', 'ignore')
        matches = text in tweet_text
        return matches

    def returnTweetHasImage(self, tweet):
        test_image = MemeGenerator.generate_custom("I like", "test driven development!", 'resources/henry.jpg')
        henry_image_base64 = base64.b64encode(test_image.read())
        image = tweet.get_image()
        image_base64 = base64.b64encode(image.read())
        if henry_image_base64 in image_base64:
            return True
        else:
            return False

    def testParrot(self):
        reader = StatusQueue()
        bot = StatusAnalyzer()
        bot.add_response_generated_listener(self.handleResponse)
        reader.add_status_ready_listener(bot.generate_response_tweet)
        inputText = "#dogebot #parrot hello world!"
        expectedOutputText = "@n4vjot hello world!, Woof"
        inputTweet = self.buildMockTweet(inputText)
        self.postTweetToBot(reader, inputTweet)
        self.waitForResponse(1)
        self.assertTrue( self.returnedTweetContains(self.getResponse(1), expectedOutputText) )

    def testMemeGen(self):
        inputText = "#dogebot #meme #henry I like, test driven development!"
        reader = StatusQueue()
        bot = StatusAnalyzer()
        bot.add_response_generated_listener(self.handleResponse)
        reader.add_status_ready_listener(bot.generate_response_tweet)
        inputTweet = self.buildMockTweet(inputText)
        self.postTweetToBot(reader, inputTweet)
        self.waitForResponse(1)
        #image = self.getResponse(1).get_image()
        #image_base64 = base64.b64encode(image.read())
        #print image_base64
        self.assertTrue( self.returnTweetHasImage(self.getResponse(1)) )

    def testMemeGenImplicitSyntax(self):
        inputText = "#dogebot #henry I like, test driven development!"
        reader = StatusQueue()
        bot = StatusAnalyzer()
        bot.add_response_generated_listener(self.handleResponse)
        reader.add_status_ready_listener(bot.generate_response_tweet)
        inputTweet = self.buildMockTweet(inputText)
        self.postTweetToBot(reader, inputTweet)
        self.waitForResponse(1)
        self.assertTrue( self.returnTweetHasImage(self.getResponse(1)) )

    def testComplexReply(self):
        inputText = "@hanray #dogebot #parrot hello world!"
        expectedOutputText = "@n4vjot @hanray hello world!, Woof"
        reader = StatusQueue()
        bot = StatusAnalyzer()
        bot.add_response_generated_listener(self.handleResponse)
        reader.add_status_ready_listener(bot.generate_response_tweet)
        inputTweet = self.buildMockTweet(inputText)
        self.postTweetToBot(reader, inputTweet)
        self.waitForResponse(1)
        self.assertTrue( self.returnedTweetContains(self.getResponse(1), expectedOutputText) )

    def testStackedTweets(self):
        reader = StatusQueue()
        bot = StatusAnalyzer()
        bot.add_response_generated_listener(self.handleResponse)
        reader.add_status_ready_listener(bot.generate_response_tweet)
        input1 = self.buildMockTweet("@hanray #dogebot #parrot hello world!")
        input2 = self.buildMockTweet( "#dogebot #parrot hello world!")
        input3 = self.buildMockTweet("#dogebot #henry I like, test driven development!")
        input4 = self.buildMockTweet("#dogebot #meme #henry I like, test driven development!")
        self.postTweetToBot(reader, input1)
        self.postTweetToBot(reader, input2)
        self.postTweetToBot(reader, input3)
        self.postTweetToBot(reader, input4)
        self.waitForResponse(4)
        self.assertTrue( self.returnedTweetContains(self.getResponse(1), "@n4vjot @hanray hello world!, Woof") )
        self.assertTrue( self.returnedTweetContains(self.getResponse(2), "@n4vjot hello world!, Woof") )
        self.assertTrue( self.returnTweetHasImage(self.getResponse(3)) )
        self.assertTrue( self.returnTweetHasImage(self.getResponse(4)) )

    def testErrorRecovery(self):
        Log.showE = False
        reader = StatusQueue()
        bot = StatusAnalyzer()
        bot.add_response_generated_listener(self.handleResponse)
        reader.add_status_ready_listener(bot.generate_response_tweet)
        input1 = self.buildMockTweet("#dogebot #henry missing comma is broken syntax!")
        input2 = self.buildMockTweet("#dogebot #meme #henry I like, test driven development!")
        self.postTweetToBot(reader, input1)
        self.postTweetToBot(reader, input2)
        self.waitForResponse(1)
        Log.showE = True
        self.assertTrue( self.returnTweetHasImage(self.getResponse(1)) )

    def testSmite(self):
        reader = StatusQueue()
        bot = StatusAnalyzer()
        bot.add_response_generated_listener(self.handleResponse)
        reader.add_status_ready_listener(bot.generate_response_tweet)
        inputText = "#dogebot #smite this guy"
        expectedOutputText = "@n4vjot Get smitten, scrub"
        inputTweet = self.buildMockTweet(inputText)
        self.postTweetToBot(reader, inputTweet)
        self.waitForResponse(1)
        self.assertTrue( self.returnedTweetContains(self.getResponse(1), expectedOutputText) )

    def testRektResponds(self):
        reader = StatusQueue()
        bot = StatusAnalyzer()
        bot.add_response_generated_listener(self.handleResponse)
        reader.add_status_ready_listener(bot.generate_response_tweet)
        inputText = "#dogebot #rekt"
        inputTweet = self.buildMockTweet(inputText)
        self.postTweetToBot(reader, inputTweet)
        self.waitForResponse(1)
        self.assertTrue( True )

    def testDongerResponds(self):
        reader = StatusQueue()
        bot = StatusAnalyzer()
        bot.add_response_generated_listener(self.handleResponse)
        reader.add_status_ready_listener(bot.generate_response_tweet)
        inputText = "#dogebot #donger"
        inputTweet = self.buildMockTweet(inputText)
        self.postTweetToBot(reader, inputTweet)
        self.waitForResponse(1)
        self.assertTrue( True )

if __name__ == '__main__':
    unittest.main()

