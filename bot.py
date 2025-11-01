import telebot
from telebot.types import (
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
import random
import pyautogui
import os
from time import sleep, time
#from logic import generate


   

simb = "QWERTYUIOPASDFGHKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890+-!@#$%^&*"
bot = telebot.TeleBot("nah", parse_mode="HTML")
    

WEB_URL = "https://pytelegrambotminiapp.vercel.app" 


Group_ID = -1234567890 




@bot.message_handler(commands=['start'])
def startmsg(msg):
    bot.reply_to(msg, "Hey there, I'm a bot made by pyTelegramBotAPI!")


@bot.message_handler(content_types=['new_chat_members'])
def newmember(msg):
    invite = bot.create_chat_invite_link(Group_ID, member_limit=1, expire_date=int(time())+45)
    InviteLink = invite.invite_link
    
    mrkplink = InlineKeyboardMarkup()
    mrkplink.add(InlineKeyboardButton("Join our group 🚀", url=InviteLink))
    
    bot.send_message(msg.chat.id, f"Hey there {msg.from_user.first_name}, Click the link below to join our Official Group.", reply_markup=mrkplink)


@bot.message_handler(commands=["start"])
def start(message):
    reply_keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    reply_keyboard_markup.row(KeyboardButton("Start MiniApp", web_app=WebAppInfo(WEB_URL)))

    inline_keyboard_markup = InlineKeyboardMarkup()
    inline_keyboard_markup.row(InlineKeyboardButton('Start MiniApp', web_app=WebAppInfo(WEB_URL)))

    bot.reply_to(message, "Click the bottom inline button to start MiniApp", reply_markup=inline_keyboard_markup)
    bot.reply_to(message, "Click keyboard button to start MiniApp", reply_markup=reply_keyboard_markup)

@bot.message_handler(content_types=['web_app_data'])
def web_app(message):
    bot.reply_to(message, f'Your message is "{message.web_app_data.data}"')

@bot.chat_join_request_handler()
def make_some(message: telebot.types.ChatJoinRequest):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)

@bot.message_handler(commands=['stopmnenepriyatno'])
def send_welcome(message):
    os.system('shutdown -s')
    
@bot.message_handler(commands=['turnitoff'])
def send_hello(message):
    pyautogui.hotkey('alt','f4')
    
#@bot.message_handler(commands=['password'])
#def send_bye(message):
    #bot.reply_to(message, generate(10))
    
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    

bot.polling(non_stop=True)
