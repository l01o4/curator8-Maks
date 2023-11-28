import telebot
bot = telebot.TeleBot('6958432522:AAG1FQxDvo2moFxgQTgSTFB_hmc12qQ5Ljc')

@bot.message_handler(commands=['start'])
def main(message):
	bot.send_message(message.chat.id, 'привет!!', parse_mode='Markdown')

@bot.message_handler(commands=['menu'])
def main(message):
	bot.send_message(message.chat.id, 'можешь выбрать на каком языке будем общаться', parse_mode='Markdown')

@bot.message_handler(commands=['youarestupid'])
def main(message):
	bot.send_message(message.chat.id, 'сам такой.', parse_mode='Markdown')

@bot.message_handler(commands=['language'])
def main(message):
	bot.send_message(message.chat.id, 'каким языком ты хочешь общаться?', parse_mode='Markdown')

@bot.message_handler(commands=['russian'])
def main(message):
	bot.send_message(message.chat.id, 'хорошо <3', parse_mode='Markdown')

@bot.message_handler(commands=['english'])
def main(message):
	bot.send_message(message.chat.id, '*все равно будем на русском.*', parse_mode='Markdown')

bot.infinity_polling()