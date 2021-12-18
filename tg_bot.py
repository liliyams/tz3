import telebot
import os
token = os.environ['TOKEN']
my_id = os.environ['ID']
bot = telebot.TeleBot(token)

photo_url = "https://st3.depositphotos.com/6998422/18874/i/600/depositphotos_188741414-stock-photo-like-3d.jpg"
bot.send_photo(my_id, photo=photo_url, caption='все работает')


