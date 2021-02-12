#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Sample Python3 OAuthRequest
"""

import requests as req
from requests_oauthlib import OAuth1
from xml.etree.ElementTree import *

NAME = ''
KEY = ''
SECRET = ''
URL = ''

consumer = OAuth1(KEY , SECRET)

params = {
    'key': KEY,
    'name': NAME,
}    # その他のパラメータについては、各APIのリクエストパラメータに従って設定してください。

try:
    res = req.post(URL , data=params , auth=consumer)
    res.encoding = 'utf-8'
    print("[res]")
    print(res)
    print(res.text)

    xelm = fromstring(res.text)
    print(xelm.findtext(".//message"))

except Exception as e:
    print('=== Error ===')
    print('type:' + str(type(e)))
    print('args:' + str(e.args))
    print('e:' + str(e))

