# -*- coding: UTF-8 -*-

import requests, json, math, os
from stringcolor import *

# The Money you have
BTC_TO_SELL = 0.047

# Get APIs:
print("Rates: ")

# Get BTC/USDT API on cryptocompare:
content = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USDT")
btc_to_usdt_json = json.loads(content.content)
btc_to_usdt = btc_to_usdt_json["USDT"]
print("BTC/USDT: "+str(btc_to_usdt))

# Get USDT/CNY OTC sell though Huobi API:
content = requests.get("https://otc-api-hk.eiijo.cn/v1/data/trade-market?coinId=2&currency=1&tradeType=buy&currPage=1&payMethod=0&country=37&blockType=general&online=1&range=0&amount=")
usdt_cny_json = json.loads(content.content)
usdt_to_cny_price = (usdt_cny_json["data"][0]["price"])
print("USDT/CNY: "+ str(usdt_to_cny_price))

# Get BTC/CNY OTC sell though Huobi API:
content = requests.get("https://otc-api-hk.eiijo.cn/v1/data/trade-market?coinId=1&currency=1&tradeType=buy&currPage=1&payMethod=0&country=37&blockType=general&online=1&range=0&amount=")
btc_cny_json = json.loads(content.content)
btc_cny_price = (btc_cny_json["data"][0]["price"])
print("BTC/CNY: "+ str(btc_cny_price))


# Calculate How Much CNY you can get:
print("\n\n")
print(str(BTC_TO_SELL)+" BTC 所能获得的CNY：")


# Trade BTC though OTC:
print("通过Huobi OTC交易: ")
# CNY -> BTC:
btc_to_cny = BTC_TO_SELL * btc_cny_price
print("BTC -> CNY: " + str(btc_to_cny))

# Trade BTC though USDT:
btc_usdt_cny_result = btc_to_usdt * BTC_TO_SELL * usdt_to_cny_price
print("\n")
print("通过USDT交易: ")
print("BTC -> USDT -> CNY: "+ str(btc_usdt_cny_result))

# Claculate loss on SpotTrading/OTC:
print("\n")
print("SpotTrade / OTC: " + str(btc_usdt_cny_result/btc_to_cny))
