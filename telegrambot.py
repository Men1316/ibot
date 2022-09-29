#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '5165246550:AAHu3aWMdBrzKmLxLeKAhY61H89bg0iTyvI'

bot = telebot.TeleBot(API_TOKEN)


def gen_markup():
    markup=InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton("📸 Instagram 📸",url="https://www.instagram.com/_xvittori_o_/" ),
               InlineKeyboardButton("▶️ Youtube ▶️", url="https://www.youtube.com/channel/UCXUIH5rcTDKkDx5eZ6GmgoA"),
               InlineKeyboardButton("👾 Twitch 👾",url="https://www.twitch.tv/bakanor_" ))
    return markup

@bot.callback_query_handler(func=lambda call: True)
# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Ciao, sono un bot creato da poco , Menne mi sta insegnando molte cose, come posso aiutarti?\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):

    if message.text == '/help' or message.text == 'help':
      bot.reply_to(message,'Questo è il comando help \nEcco la lista di comandi che posso esegurire: \n \n \n/links      Tutti i canali del mio sviluppatore \n/help      Ti mostro cosa posso fare \n \n \nPer ora posso fare poche cose, sto imparando molto!')
      bot.send_message(message.chat.id,"Cosa vuoi che faccia?")
    elif message.text== '/links':
      bot.send_message(message.chat.id,"Ciao cosa posso fare per te?",reply_markup=gen_markup())
    elif message.text == 'Ciao':
      bot.reply_to(message, message.text+" , come va?")
    elif message.text== 'Tutto bene':
      bot.reply_to(message,"Mi fa piacere!")
    elif message.text== 'Ciao sono Menne':
      bot.reply_to(message,"Ciao Padrone")
    elif message.text=='Ciao sono Giorgio':
      bot.reply_to(message,"Ciao Giorgio")
    else :
      bot.reply_to(message,"Mi dispiace , purtroppo non capisco tutto, sto ancora imparando!")

bot.infinity_polling()