import telebot
import os
token = os.environ['TOKEN']
my_id = os.environ['ID']
bot = telebot.TeleBot(token)

try:
    f = open("bot.txt", "r")
    data = f.read()
    photo_url = "https://lh3.googleusercontent.com/proxy/7huI_QgzjiNTeqK3fXr5JMgZZ6pXwIOkOjf0_MEyTcMNDPumwmnTdgvgL3ZxMEp0L3QhQbpWwlaO9XbouUX9P1qGwfjuyWo133k"
    bot.send_photo(my_id, photo=photo_url, caption=str(data))

except FileNotFoundError as e:
    data = "все в порядке"
    photo_url = "https://st3.depositphotos.com/6998422/18874/i/600/depositphotos_188741414-stock-photo-like-3d.jpg"
    bot.send_photo(my_id, photo=photo_url, caption=str(data))


