#!/bin/python3
# -*- coding: utf-8 -*-
import json
__all__ = ["get_config"]

TESTING_DB = "./testing_data.csv"
USERS_DB = "./users_db.sqlite3"
BOT_TOKEN = "./bot_token.json"

def get_config():
    params = {}
    params['TESTING_DB'] = TESTING_DB
    params['USERS_DB'] = USERS_DB
    with open(BOT_TOKEN) as jsonf:
        bot_token = json.load(jsonf)
    params['BOT_TOKEN'] = bot_token['token']

    return params
