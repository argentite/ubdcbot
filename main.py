import os
import urllib, json
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.filters import Filters

def start(bot, update):
    update.message.reply_text(
        "Hello {}! Welcome to Urban Dictionary Unofficial Bot."
        .format(update.message.from_user.first_name))

def lookup(bot, update):
    response = json.loads(urllib.urlopen("https://api.urbandictionary.com/v0/define?term={}".format(update.message.text)).read())
    for i in range(4):
        update.message.reply_text(
            "*+{} -{}* _{}_\n{}\n[Permalink]({})".format(
            response['list'][i]['thumbs_up'],
            response['list'][i]['thumbs_down'],
            response['list'][i]['author'],
            response['list'][i]['definition'],
            response['list'][i]['permalink']),
            parse_mode="Markdown", disable_web_page_preview=True)

updater = Updater(os.environ['TG_BOT_API_KEY'])

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, lookup))

updater.start_polling()
updater.idle()
