import telebot
import BotAPI

bot = telebot.TeleBot(BotAPI.botToken)


@bot.message_handler(commands=['start'])
def start(message):
    if BotAPI.isUserInStorage(message.from_user.username):
        bot.send_message(message.chat.id, f"{BotAPI.botStartMessageIfInTeamStart} {BotAPI.getUsersTeam(message.from_user.username)},"
                                          f" {message.from_user.username}!")
        wantToChangeTeam(message)
    else:
        bot.send_message(message.chat.id, BotAPI.botStartMessage)
        bot.register_next_step_handler(message, getTeamNumber)


@bot.message_handler(commands=['help'])
def sendHelp(message):
    bot.send_message(message.chat.id, f'{message.from_user.username}' + BotAPI.botHelpMessage)


@bot.message_handler(commands=['teams'])
def getUsers(message):
    bot.send_message(message.chat.id, BotAPI.getTeams())


def getTeamNumber(message):
    if message.text.isdigit():
        if 1 <= int(message.text) <= 8:
            BotAPI.registerUser(int(message.text), message.from_user.username)
            bot.reply_to(message, f"{message.from_user.username}, {BotAPI.botRegisteredToTeamMessage} {message.text}!")
            wantToChangeTeam(message)
        else:
            bot.reply_to(message, BotAPI.botErrorTeamNumber2Message)
            bot.register_next_step_handler(message, getTeamNumber)
    else:
        bot.reply_to(message, BotAPI.botErrorTeamNumber1Message)
        bot.register_next_step_handler(message, getTeamNumber)


def wantToChangeTeam(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    button1 = telebot.types.KeyboardButton(BotAPI.userWantToChangeTeamButton)
    button2 = telebot.types.KeyboardButton(BotAPI.userDontWantToChangeTeamButton)
    markup.row(button1, button2)
    bot.send_message(message.chat.id, BotAPI.botWantToChangeTeamMessage, reply_markup=markup)


bot.infinity_polling()