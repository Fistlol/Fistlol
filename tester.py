import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types

TOKEN = '1310525345:AAHiMjI0XcARm12abTRSFBhGHYiO5_kuH-g' 

bot = telebot.TeleBot(TOKEN)

value = 'https://bai.kz/bank/kaspi-bank/kursy/'
bitvalue = 'https://ifin.kz/crypto/KZT'

page = requests.get(value)
bitpage = requests.get(bitvalue)

soup = BeautifulSoup(page.content, 'html.parser')
bitsoup = BeautifulSoup(bitpage.content, 'html.parser')

convert = soup.findAll("td")
bitconvert = bitsoup.findAll("td")

@bot.message_handler(commands=['start'])
def welcome(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("USD")
    item2 = types.KeyboardButton("EUR")
    item3 = types.KeyboardButton("RUB")
    item4 = types.KeyboardButton("BTC")
    item5 = types.KeyboardButton("ETH")
    item6 = types.KeyboardButton("LTC")
 
    markup.add(item1, item2, item3, item4, item5, item6)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nВы можете выбрать валюту, а я покажу ее курс по отношению к тенге.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'USD':
            bot.send_message(message.chat.id, "1 Доллар США = " + convert[3].text + " тенге")
        elif message.text == 'EUR':
            bot.send_message(message.chat.id, "1 Евро = " + convert[8].text + " тенге")
        elif message.text == 'RUB':
            bot.send_message(message.chat.id, "1 Российский рубль = " + convert[13].text + " тенге")
        elif message.text == 'BTC':
            bot.send_message(message.chat.id, "1 Bitcoin = " + bitconvert[2].text[:12] + " тенге")
        elif message.text == 'ETH':
            bot.send_message(message.chat.id, "1 Ethereum = " + bitconvert[8].text[:11] + " тенге")
        elif message.text == 'LTC':
            bot.send_message(message.chat.id, "1 Litecoin = " + bitconvert[14].text[:10] + " тенге")
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить')
 
bot.polling(none_stop=True)