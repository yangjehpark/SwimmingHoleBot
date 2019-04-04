#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.

This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""

import sys
import os
sys.path.append(os.path.join(os.path.abspath('.'), 'venv/lib/python2.7/site-packages'))
import telegram
from flask import Flask, request

app = Flask(__name__)

global bot
bot = telegram.Bot(token='869916009:AAEYrIlwDAlSLyJ6SsOEzjv-rEw6FJpW8VM')


@app.route('/HOOK', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        
        chat_id = update.message.chat.id
        
        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text.encode('utf-8')
        
        # repeat the same message back (echo)
        echo = text + '~'
        bot.sendMessage(chat_id=chat_id, text=echo)
    
    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('https://swimmingholebot.appspot.com/HOOK')
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return '.'
