from telebot import TeleBot
from telebot.types import Message
import requests
bot = TeleBot('7428949465:AAGwcYhBF5ZZekHToE_iFEGs67hDdRsxAHg')

@bot.message_handler(commands=['start'])

def start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text='Davay')


@bot.message_handler(commands=['car'])

def reaction_to_car(message: Message):
    chat_id = message.chat.id
    
    car=requests.get('http://127.0.0.1:8000/api/v1/car/').json()
    
    for c in car:
        text = f"name:{c['name']}\ccontent:{c['content']}"
        bot.send_message(chat_id, text)
    
  
    
bot.infinity_polling()