"""
Напишите обработчик, который на сообщения с фотографией будет отвечать сообщением «Nice meme XDD».
Бот должен отвечать не отдельным сообщением, а с привязкой к картинке.
"""

import telebot

bot = telebot.TeleBot('6269541299:AAEO8EUIu7pj5ggmz-dhr_srLEvEpu047oM')


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


bot.polling(none_stop=True)

