import os
import urllib, json
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.filters import Filters

def command_help(bot, update):
    update.message.reply_text(
        "Hello human! I'm Urban Dictionary Unofficial Bot. Send me a word and I'll lookup on Urban Dictionary!")

def command_lookup(bot, update):
    response = json.loads(urllib.urlopen("https://api.urbandictionary.com/v0/define?term={}".format(update.message.text)).read())
    for i in range(4):
        update.message.reply_text(
            "*+{} -{} {}* _{}_\n{}\n[Permalink]({})".format(
            response['list'][i]['thumbs_up'],
            response['list'][i]['thumbs_down'],
            response['list'][i]['word'],
            response['list'][i]['author'],
            response['list'][i]['definition'],
            response['list'][i]['permalink']),
            parse_mode="Markdown", disable_web_page_preview=True)

updater = Updater(os.environ['TG_BOT_API_KEY'])

updater.dispatcher.add_handler(CommandHandler('start', command_help))
updater.dispatcher.add_handler(CommandHandler('help', command_help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, command_lookup))

updater.start_polling()
updater.idle()
