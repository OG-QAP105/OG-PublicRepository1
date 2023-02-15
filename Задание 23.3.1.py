"""
Допишите обработчик так, чтобы он из сообщения брал username и выдавал приветственное сообщение
с привязкой к пользователю.
"""

import telebot

TOKEN = "6269541299:AAEO8EUIu7pj5ggmz-dhr_srLEvEpu047oM"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, \ c{message.chat.username}")


bot.polling(none_stop=True)
