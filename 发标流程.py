# -*- coding: utf-8 -*-
import requests
from pprint import pprint

def dafen(UserId,listId):

    url = 'http://api.userscore.risk.ppdaicorp.com/SetSingleOnceUserScore'
    data = {'UserId':'%d','listId':'%d'} % (UserId,listId)
    dafen_r = requests.post(url=url,json=data)
    dafen_r_json = dafen_r.json()

