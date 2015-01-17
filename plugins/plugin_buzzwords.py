# -*- coding: UTF-8 -*-
from abstractplugin import AbstractPlugin
from models.tweetresponse import TweetResponse
import random


class Buzzwords(AbstractPlugin):
    registered_commands = ['#donger', '#smite', '#rekt', '#dealwithit', '#swag']
    # TODO: add image check to unit test for this
    def get_response(self, tweet_wrapper):
        command = tweet_wrapper.get_tweet_command()
        operator = command.get_command_operator()
        if operator == "#smite":
            response_text = "Get smitten, scrub"
            response = TweetResponse(command, response_text)
            response.set_image_loc('resources/smite.jpg')
            return response

        if operator == "#rekt":
            response_text = self.getRektText()
            response = TweetResponse(command, response_text)
            response.set_image_loc('resources/rekt.gif')
            return response

        if operator == "#dealwithit":
            response_text = "deal with it"
            response = TweetResponse(command, response_text)
            response.set_image_loc('resources/dealwithit.gif')
            return response

        if operator == "#swag":
            response_text = "swag"
            response = TweetResponse(command, response_text)
            response.set_image_loc('resources/swag.jpg')
            return response

        if operator == "#donger":
            response_text = self.getDongerText()
            response = TweetResponse(command, response_text)
            return response

        if operator == "#toucan":
            response_text = self.getToucanText()
            response = TweetResponse(command, response_text)
            return response

    rekt_list = ["REKT", "REKTangle", "SHREKT", "REKT-it Ralph", "Total REKTall", "The Lord of the REKT",
                 "The Usual SusREKTs", "North by NorthREKT", "REKT to the Future", "Once Upon a Time in the REKT",
                 "The Good, the Bad, and the REKT ", "Tyrannosaurus REKT"]

    def getRektText(self):
        random.shuffle(self.rekt_list)
        choice_one = self.rekt_list[0]
        choice_two = self.rekt_list[1]
        response_text = u"\n☐"
        response_text += " Not REKT"
        response_text += u"\n☑ "
        response_text += choice_one
        response_text += u"\n☐ "
        response_text += choice_two
        return response_text



    donger_lines = [
        u"༼ ºل͟º༼ ºل͟º༼ ºل͟º༼ ºل͟º ༽ºل͟º ༽ºل͟º ༽YOU CAME TO THE WRONG DONGERHOOD༼ ºل͟º༼ ºل͟º༼ ºل͟º༼ ºل͟º ༽ºل͟º ༽ºل͟º ༽ ",
        u" ༼ ºل͟º ༼ ºل͟º ༼ ºل͟º ༽ ºل͟º ༽ ºل͟º ༽ YOU PASTARINO'D THE WRONG DONGERINO ༼ ºل͟º ༼ ºل͟º ༼ ºل͟º ༽ ºل͟º ༽ ºل͟º ༽",
        u"༼ ºل͟º༼ ºل͟º༽ºل͟º ༽ YOU COPERINO﻿ FRAPPUCCIONO PASTARINO'D THE WRONG DONGERINO ༼ ºل͟º༼ ºل͟º༽ºل͟º ༽",
        u" ༼ ºل͟º༼ ºل͟º༼ ºل͟º༼ ºل͟º ༽ºل͟º ༽ºل͟º ༽You either die a DONG, or live long enough to become the DONGER༼ ºل͟º༼ ºل͟º༼ ºل͟º༼ ºل͟º ༽ºل͟º ༽ºل͟º ༽",
        u"༼ ಠل͟ರೃ༼ ಠل͟ರೃ༼ ಠل͟ರೃ༼ ಠل͟ರೃ ༽ಠل͟ರೃ ༽ಠل͟ರೃ ༽ YOU ARRIVED IN THE INCORRECT DONGERHOOD, SIR༼ ಠل͟ರೃ༼ ಠل͟ರೃ༼ ಠل͟ರೃ༼ ಠل͟ರೃ ༽ಠل͟ರೃ ༽ಠل͟ರೃ ༽   ",
        u"ᕙ༼ຈل͜ຈ༽ᕗ. ʜᴀʀᴅᴇʀ,﻿ ʙᴇᴛᴛᴇʀ, ғᴀsᴛᴇʀ, ᴅᴏɴɢᴇʀ .ᕙ༼ຈل͜ຈ༽ᕗ ",
        u"(ง ͠° ͟ل͜ ͡°)ง ᴍᴀsᴛᴇʀ ʏᴏᴜʀ ᴅᴏɴɢᴇʀ, ᴍᴀsᴛᴇʀ ᴛʜᴇ ᴇɴᴇᴍʏ (ง ͠° ͟ل͜ ͡°)ง ",
        u"(ง ͠° ل͜ °)ง LET ME DEMONSTRATE DONGER DIPLOMACY (ง ͠° ل͜ °)ง",
        u"乁( ◔ ౪◔)ㄏ",
        u"(\ ( ͠° ͟ل͜ ͡°) /) OUR DONGERS ARE RAZOR SHARP (\ ( ͠° ͟ل͜ ͡°) /) ",
        u"ヽ༼◥▶ل͜◀◤༽ﾉ RO RO RAISE YOUR DONGERS ヽ༼◥▶ل͜◀◤༽ﾉ ",
        u"̿̿ ̿̿ ̿'̿'̵͇̿̿з=༼ ▀̿̿Ĺ̯̿̿▀̿ ̿ ༽=ε/̵͇̿̿/’̿’̿ ̿ ̿̿[} ̿ ̿ ̿ ̿^ Stop right there criminal scum! no one RIOTs on my watch. I'm confiscating your goods. now pay your fine, or it's off to jail. ",
        u"̿̿ ̿̿ ̿̿ ̿'̿'̵͇̿̿з=༼ ▀̿̿Ĺ̯̿̿▀̿ ̿ ༽ YOU'RE UNDER ARREST FOR BEING CASUAL. COME OUT WITH YOUR DONGERS RAISED ̿̿ ̿̿ ̿̿ ̿'̿'̵͇̿̿з=༼ ▀̿̿Ĺ̯̿̿▀̿ ̿ ༽   ",
        u"(ง'̀-'́)ง ＤＯＮＧ ＯＲ ＤＩＥ (ง'̀-'́)ง   ",
        u"ヽ༼ຈل͜ຈ༽ﾉ raise your dongers ヽ༼ຈل͜ຈ༽ﾉ ",
        u"ヽ༼ຈل͜ຈ༽ﾉ VOICE OF AN ANGEL ヽ༼ຈل͜ຈ༽ﾉ ",
        u"ヽ༼ຈل͜ຈ༽ﾉ LETS GET DONGERATED ヽ༼ຈل͜ຈ༽ﾉ ",
        u"ヽ༼ຈل͜ຈ༽ﾉ RAISE YOUR BARNO ヽ༼ຈل͜ຈ༽ﾉ ",
        u"ヽ༼ຈل͜ຈ༽ﾉ OJ poured and candle lit, with this chant i summon Kripp ヽ༼ຈل͜ຈ༽ﾉ ",
        u" ☑ OJ poured ☑ Candle lit ☑ Summoning the Kripp ヽ༼ຈل͜ຈ༽ﾉ",
        u"ヽ༼ຈل͜O༽ﾉ ʀᴀɪs ᴜʀ ᴅᴀɢᴇʀᴏ ヽ༼ຈل͜___ຈ༽ﾉ  ",
        u"(ง ͠° ͟ʖ ͡°)งSuccubus release Kripp or taste our rage(ง ͠° ͟ʖ ͡°)ง   ",
        u"ノ(ಠ_ಠノ ) ʟᴏᴡᴇʀ ʏᴏᴜʀ ᴅᴏɴɢᴇʀs ノ(ಠ_ಠノ)",
        u"ヽ༼Ὸل͜ຈ༽ﾉ HOIST THY DONGERS ヽ༼Ὸل͜ຈ༽ﾉ ",
        u"ヽ( ͡° ͜ʖ ͡°)ﾉ Kripp you are kinda like my dad, except you're always there for me. ヽ( ͡° ͜ʖ ͡°)ﾉ ",
        u" █▄༼ຈل͜ຈ༽▄█ yeah i work out  ",
        u"༼ ºل͟º ༽ I AM A DONG ༼ ºل͟º ༽ ",
        u"༼ ºل͟º༽ I DIDN'T CHOOSE THE DONGLIFE, THE DONGLIFE CHOSE ME ༼ ºل͟º༽ ",
        u"༼ ºل͟º༽ NO ONE CARED WHO I WAS UNTIL I PUT ON THE DONG ༼ ºل͟º༽  ",
        u"༼ ºººººل͟ººººº ༽ I AM SUPER DONG ༼ ºººººل͟ººººº ༽ ",
        u"┌∩┐༼ ºل͟º ༽┌∩┐ SUCK MY DONGER ┌∩┐༼ ºل͟º ༽┌∩┐ ",
        u"ζ༼Ɵ͆ل͜Ɵ͆༽ᶘ FINALLY A REAL DONG ζ༼Ɵ͆ل͜Ɵ͆༽ᶘ ",
        u"<ᴍᴇssᴀɢᴇ ᴅᴏɴɢᴇʀᴇᴅ> ",
        u"ヽ༼ʘ̚ل͜ʘ̚༽ﾉIS THAT A DONGER IN YOUR POCKET?ヽ༼ʘ̚ل͜ʘ̚༽ﾉ  ",
        u" ༼ ͡■ل͜ ͡■༽ OPPA DONGER STYLE ༼ ͡■ل͜ ͡■༽  ",
        u"( ° ͜ ʖ °) REGI OP ( ° ͜ ʖ °) ",
        u"(̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄ IM DONG,JAMES DONG (̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄ ",
        u"(ง⌐□ل͜□)ง WOULD YOU HIT A DONGER WITH GLASSES (ง⌐□ل͜□)ง ",
        u"ʕ•ᴥ•ʔ CUDDLE UR DONGERS ʕ•ᴥ•ʔ ",
        u"ლ(́◉◞౪◟◉‵ლ) let me hold your donger for a while ლ(́◉◞౪◟◉‵ლ) ",
        u"ヽ༼ຈل͜ຈ༽ง MY RIGHT DONG IS ALOT STRONGER THAN MY LEFT ONE ヽ༼ຈل͜ຈ༽ง",
        u"(✌ﾟ∀ﾟ)☞ May the DONG be with you! ☚(ﾟヮﾟ☚)   ",
        u"(⌐■_■)=/̵͇̿̿/'̿'̿̿̿ ̿ ̿̿ ヽ༼ຈل͜ຈ༽ﾉ Keep Your Dongers Where i Can See Them ",
        u"̿'̿'\̵͇̿̿\з=( ͠° ͟ʖ ͡°)=ε/̵͇̿̿/'̿̿ ̿ ̿ ̿ ̿ ̿ DUDE̿̿ ̿̿ ̿'̿'\̵͇̿̿\з=( ͠° ͟ʖ ͡°)=ε/̵͇̿̿/'̿̿ ̿ ̿ ̿ ̿ ̿ PLEASE NO COPY PASTERONI MACORONI DONGERIN ",
        u"( ͝° ͜ʖ͡°) Mom always said my donger was big for my age ( ͝° ͜ʖ͡°)",
        u"(/ﾟДﾟ)/ WE WANT SPELUNKY (/ﾟДﾟ)/",
        u"─=≡Σ((( つ◕ل͜◕)つ sᴜᴘᴇʀ ᴅᴏɴɢ  ",
        u"(✌ﾟ∀ﾟ)☞ POINT ME TO THE DONGERS (✌ﾟ∀ﾟ)☞ ",
        u"ᕙ( ^ₒ^ c) 〇〇〇〇ᗩᗩᗩᗩᕼᕼ ᕙ( ^ₒ^ c)",
        u"ヽ༼ຈل͜ຈ༽ﾉ ArcheAge or BEES ヽ̛͟͢༼͝ຈ͢͠لຈ҉̛༽̨҉҉ﾉ̨",
        u" ୧༼ಠ益ಠ༽୨ MRGLRLRLR ୧༼ಠ益ಠ༽୨",
        u"┏(-_-)┓┏(-_-)┛┗(-_-﻿ )┓┗(-_-)┛┏(-_-)┓ ┏(-_-)┛┗(-_-﻿ )┓┗(-_-)┛┏(-_-)┓┏(-_-)┛┗(-_-﻿ )┓┗(-_-)┛┏(-_-)┓┏(-_-)┛┗(-_-﻿ )┓┗(-_-)┛┏(-_-)┓ ",
        u"ヽ༼ຈل͜ຈ༽ﾉITS A HARD DONG LIFE ヽ༼ຈل͜ຈ༽ﾉ",
        u"ヽ༼ຈل͜ຈ༽ﾉMOLLYヽ༼ຈل͜ຈ༽ﾉ",
        u"༼ つ ຈل͜ຈ ༽つ GIVE MOLLY ༼ つ ຈل͜ຈ ༽つ",
        u" †ヽ༼ຈل͜ຈ༽ﾉ† By the power of donger I summon MOLLY †ヽ༼ຈل͜ຈ༽ﾉ† ",
        u"ヽ༼ຈل͜ຈ༽ﾉTAKING A DUMPヽ༼ຈل͜ຈ༽ﾉ ",
        u"ヽ༼ຈل͜ຈ༽ﾉ WHAT DOESNT KILL ME ONLY MAKES ME DONGER ᕙ༼ຈل͜ຈ༽ᕗ  ",
        u"ヽ༼ຈل͜ຈ༽ﾉ FOREVER DONG ヽ༼ຈل͜ຈ༽ﾉ ",
        u"[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅] Mo' money, mo' Dongers [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅] ",
        u"༼ᕗຈل͜ຈ༽ᕗ Drop Bows on 'em ༼ᕗຈل͜ຈ༽ᕗ ",
        u"Ѱζ༼ᴼل͜ᴼ༽ᶘѰ HIT IT WITH THE FORK Ѱζ༼ᴼل͜ᴼ༽ᶘѰ  ",
        u"Ψ༼ຈل͜ຈ༽Ψ hit﻿ it with the fork Ψ༼ຈل͜ຈ༽Ψ"
    ]

    def getDongerText(self):
        response_text = random.choice(self.donger_lines)
        return response_text

    toucan = [u"""░░░░░░░░▄▄▄▀▀▀▄▄███▄
░░░░░▄▀▀░░░░░░░▐░▀██▌
░░░▄▀░░░░▄▄███░▌▀▀░▀█
░░▄█░░▄▀▀▒▒▒▒▒▄▐░░░░█▌
░▐█▀▄▀▄▄▄▄▀▀▀▀▌░░░░░▐█▄
░▌▄▄▀▀░░░░░░░░▌░░░░▄███████"""];

    def getToucanText(self):
        response_text = self.toucan;
        return response_text;