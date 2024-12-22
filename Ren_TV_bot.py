import telebot
import s_token
from telebot import types
import xmltodict
import requests

bot = telebot.TeleBot(s_token.bot_token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я Рен-тв бот, отвечаю за ПРАВДИВЫЕ новости ')
    response = requests.get('https://elementy.ru/rss/news/cosmos')
    data = xmltodict.parse(response.text)
    channel = data['rss']['channel']
    item = channel['item']
    for new in item:
        print(new)
        category = new['category']
        description = new['description'][3:-4]
        if '</b>' in description:
            description = description.replace('</b>','')
        link = new['link']
        pubDate = new['pubDate']
        title = new['title']
        image_url = new['enclosure']['@url']
        bot.send_photo(message.chat.id, image_url,
                       f"{title}\n\n{category}\n\n{description}\n\n{pubDate}",
                       reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text='подробнее',url=link)))




bot.infinity_polling()
