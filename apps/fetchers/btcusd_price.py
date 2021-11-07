#!/usr/bin/python3

import sqlite3
import requests
import os

response = requests.get(os.getenv('BTCUSD_URL'), headers = {'X-CoinAPI-Key' : os.getenv('BTCUSD_APIKEY')})

if response.status_code == 200:
	obj = response.json()
	con = sqlite3.connect(os.getenv('DATABASE_URL'))
	cur = con.cursor()
	cur.execute("INSERT INTO ValueHistory(type, unit, value, value_time) VALUES ('BTCUSD', 'USD', %s, '%s')" % (obj['time'], obj['rate']))
	con.commit()
	con.close()