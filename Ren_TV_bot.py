import telebot
import s_token
from telebot import types
import xmltodict
import requests
import time

bot = telebot.TeleBot(s_token.bot_token)


@bot.message_handler(commands=['start'])
def start(message):
    # bot.send_message(message.chat.id, 'Привет, я Рен-тв бот, отвечаю за ПРАВДИВЫЕ новости ')
    response = requests.get('https://elementy.ru/rss/news/cosmos')
    data = xmltodict.parse(response.text)
    channel = data['rss']['channel']
    item = channel['item']
    for new in item:
        print(new)
        category = new['category']
        description = new['description'][3:-4]
        if '</b>' in description:
            description = description.replace('</b>', '')
        link = new['link']
        pubDate = new['pubDate']
        title = new['title']
        image_url = new['enclosure']['@url']
        bot.send_photo(-1002461564930, image_url,
                       f"{title}\n\n{category}\n\n{description}\n\n{pubDate}",
                       reply_markup=types.InlineKeyboardMarkup().add(
                           types.InlineKeyboardButton(text='подробнее', url=link)))
        time.sleep(20)


@bot.message_handler(commands=['more'])
def start(message):
    # bot.send_message(message.chat.id, 'Привет, я Рен-тв бот, отвечаю за ПРАВДИВЫЕ новости ')
    response = requests.get('https://elementy.ru/rss/news/mathematics')
    data = xmltodict.parse(response.text)
    channel = data['rss']['channel']
    item = channel['item']
    for new in item:
        print(new)
        category = new['category']
        description = new['description'][3:-4]
        if '</b>' in description:
            description = description.replace('</b>', '')
        link = new['link']
        pubDate = new['pubDate']
        title = new['title']
        image_url = new['enclosure']['@url']
        bot.send_photo(-1002461564930, image_url,
                       f"{title}\n\n{category}\n\n{description}\n\n{pubDate}",
                       reply_markup=types.InlineKeyboardMarkup().add(
                           types.InlineKeyboardButton(text='подробнее', url=link)))
        time.sleep(20)




@bot.message_handler(commands=['large'])
def start(message):
    # bot.send_message(message.chat.id, 'Привет, я Рен-тв бот, отвечаю за ПРАВДИВЫЕ новости ')
    response = requests.get('https://elementy.ru/rss/news/chemistry')
    data = xmltodict.parse(response.text)
    channel = data['rss']['channel']
    item = channel['item']
    for new in item:
        print(new)
        category = new['category']
        description = new['description'][3:-4]
        if '</b>' in description:
            description = description.replace('</b>', '')
        link = new['link']
        pubDate = new['pubDate']
        title = new['title']
        image_url = new['enclosure']['@url']
        bot.send_photo(-1002461564930, image_url,
                       f"{title}\n\n{category}\n\n{description}\n\n{pubDate}",
                       reply_markup=types.InlineKeyboardMarkup().add(
                           types.InlineKeyboardButton(text='подробнее', url=link)))
        time.sleep(20)


bot.infinity_polling()
