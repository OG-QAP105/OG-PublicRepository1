import telebot

TOKEN = "6269541299:AAEO8EUIu7pj5ggmz-dhr_srLEvEpu047oM"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['voice'])
def voice(message: telebot.types.Message):
    bot.send_message(message.chat.id, "У тебя козлиный голос!")


bot.polling(none_stop=True)

