# -*- coding: utf-8 -*-
from tweepy import OAuthHandler, API, Stream, TweepError
from tweepy.streaming import StreamListener
import os
import json 
import telepot

consumer = os.environ.get("consumer_key")
secret = os.environ.get("consumer_secret")
access_key = os.environ.get("access_token_key")
access_secret = os.environ.get("access_token_secret")
bot_token = os.environ.get("telepot_token")


def hashtag (number):
    return '#'*number

def getTrack():
    file = "//spiders//files//track.txt"
    with open (file, 'r') as fichier:
        content = fichier.read()
        track= content.strip().split(',')
    return track

def getCoinList(cls, api):
    users = list()
    filename = '/var/www/scrypto/integration/scrypto/spiders/files/links.txt'
    with open(filename, 'r', encoding='utf-8') as fichier:
        var = fichier.read()
        coins = var.strip().split('\n')
        for i, coin_name in enumerate(coins):
            try:
                user = api.get_user(coin_name)
                user = user.id_str
                users.append(user)
            except TweepError as e:
                print("Error on retrieving coin user : %s" % str(e))
                print(coin_name)
    return users


class FollowTwitterListener(StreamListener):
    def __init__(self, bot):
        self.bot = bot

    def on_data(self, data):
        decoded = json.loads(data)
        filename = 'var/www/scrypto/integration/scrypto/spiders/files/follow.txt'
        with open(filename, 'a', encoding='utf-8') as fichier:
            try:
                if (decoded['user']['id_str'] in ids) and (decoded['in_reply_to_screen_name'] == None) and ((' RT@' or ' RT @') not in decoded['text']):
                    name = decoded['user']['screen_name'].upper()
                    tweet = decoded['text']
                    time = decoded['created_at']
                    message  = f'\n {name}\nTweeted : {tweet} @{time} \n'
                    print(message)
                    self.bot.sendMessage(476895805, message)
                except KeyError as e:
                    print("Error on retrieving coin user : %s" % str(e))
        return True

    def on_error(self, status_code):
        if status_code == 420:
            print('Got an error with status code: ' + str(status_code))
            return False
        return True  # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True  # To continue listening





class TrackTwitterListener(StreamListener):
    def __init__(self):



    def on_data(self, data):
        decoded = json.loads(data)
        filename = 'var/www/scrypto/integration/scrypto/spiders/files/follow_track.txt'
        with open(filename, 'a', encoding='utf-8') as fichier:
            try:
                if (decoded['user']['id_str'] in ids) and (decoded['in_reply_to_screen_name'] == None) and ((' RT@' or ' RT @') not in decoded['text']):
                    name = decoded['user']['screen_name'].upper()
                    tweet = decoded['text']
                    time = decoded['created_at']
                    message  = f'\n {name}\nTweeted : {tweet} @{time} \n'
                    print(message)
                except KeyError as e:
                    print("Error on retrieving coin user : %s" % str(e))
        return True

    

    def on_error(self, status_code):
        if status_code == 420:
            print('Got an error with status code: ' + str(status_code))
            return False
        return True  # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True  # To continue listening


if __name__ == '__main__':
    bot = telepot.Bot(bot_token)    
    follow_listener = FollowTwitterListener(bot)
    track_listener = TrackTwitterListener()
    auth = OAuthHandler(consumer, secret)
    auth.set_access_token(access_key, access_secret)
    auth.secure = True
    api = API(auth)
    track = getTrack()
    coins = None
    try:
        coins = getCoinList(api)
    except TweepError as e:
        print("Error on retrieving coin user : %s" % str(e))
    finally:
        streamf = Stream(auth, follow_listener)
        streamc = Stream(auth, track_listener)
        streamf.filter(follow=coins)
        streamc.filter(follow=coins, track=track, languages=['en'])
