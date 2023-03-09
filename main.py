import json
from json import dumps
import telebot
from telebot import types
import crss


bot = telebot.TeleBot("5825648838:AAFzcnFi8m599ETimgob3Rgve31AxXGEFyg")


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Привет, <b><u>{message.from_user.username}</u></b>"
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def go(message):
    if (message.text == "crossout") or (message.text == "Crossout"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        go_but = types.KeyboardButton("crossout")
        markup.add(go_but)
        message_text = "___Resources___\n"
        array = crss.crossout()
        for i in array:
            message_text = message_text + str(array[i]) + "\n"
            if i == 5:
                message_text = message_text + "\n___Decor Sell Price___\n"
            if i == 9:
                message_text = message_text + "\n___Items to Buy___\n"
                if len(array) == 10:
                    message_text = message_text + "Empty"

        bot.send_message(message.chat.id, message_text, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
