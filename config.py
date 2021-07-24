#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 1827335732:AAHo1IKD-_Cx0KJ7fo-mJQBPxF4K877ODWM"")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID"7372385")
    API_HASH = os.environ.get("API_HASH"e3a3ddc4c3abf338ab4f65b4f5e9f56f") 



    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS",-599398694 "").split())
    
