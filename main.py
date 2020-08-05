from config import TOKEN
import telebot
import utils

bot = telebot.TeleBot(TOKEN)
markup = utils.generate_markup()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     """Привет!)
Я MonopolyBot, и я скажу что тебе делать,
если ты попал на поле "общественная казна" или "шанс" """,
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Общественная казна':
        bot.send_message(message.chat.id, utils.get_storage('treasure'), reply_markup=markup)
    elif message.text == 'Шанс':
        bot.send_message(message.chat.id, utils.get_storage('chance'), reply_markup=markup)


if __name__ == '__main__':
    utils.create_storage()
    bot.infinity_polling()
