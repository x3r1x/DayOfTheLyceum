import telebot
import BotAPI

bot = telebot.TeleBot(BotAPI.botToken)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, BotAPI.botStartMessage)
    bot.register_next_step_handler(message, getTeamNumber)


def getTeamNumber(message):
    if message.text.isdigit():
        bot.reply_to(message, "Done!")
    else:
        bot.reply_to(message, BotAPI.botErrorTeamNumberMessage)
        bot.register_next_step_handler(message, getTeamNumber)


@bot.message_handler(commands=['help'])
def sendHelp(message):
    bot.send_message(message.chat.id, f'{message.from_user.username}' + BotAPI.botHelpMessage)


bot.infinity_polling()
