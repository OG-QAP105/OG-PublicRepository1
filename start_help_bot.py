import telebot

TOKEN = "6269541299:AAEO8EUIu7pj5ggmz-dhr_srLEvEpu047oM"
bot = telebot.TeleBot(TOKEN)


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass


