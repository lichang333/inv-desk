# -*- coding: UTF-8 -*-

import requests, json, math, os
from stringcolor import *

# 总共投资额：1021.08 CNY
BTC_TOTAL_AMOUT = 0.030556
# BTC_TOTAL_AMOUT = 5.03245259

BTC_EVERYAGER_BUY_PRICE = 62460.5828749
# BTC_EVERYAGER_BUY_PRICE = 53195.8805137

content = requests.get("https://otc-api-hk.eiijo.cn/v1/data/trade-market?coinId=1&currency=1&tradeType=sell&currPage=1&payMethod=&country=&blockType=general&online=1&range=0&amount=")
json = json.loads(content.content)

# Show the best price for sell USDT/CNY on Huobi
best_otc_price = (json["data"][0]["price"])


# calculating...
floating_income_origin = BTC_TOTAL_AMOUT * (best_otc_price - BTC_EVERYAGER_BUY_PRICE)

# remain 2 decimal
floating_income = (round(floating_income_origin, 2))


# Get USDT/CNY OTC though Huobi API:
# content = requests.get("https://otc-api-hk.eiijo.cn/v1/data/trade-market?coinId=2&currency=1&tradeType=sell&currPage=1&payMethod=0&country=37&blockType=general&online=1&range=0&amount=")
# usdt_cny_json = json.loads(content.content)
# usdt_to_cny_price = (usdt_cny_json["data"][0]["price"])
# print("USDT/CNY: "+ str(usdt_to_cny_price))

# Print

print("BTC/CNY")

print("买入均价：" + str(BTC_EVERYAGER_BUY_PRICE))
print ("持仓量：" + str(BTC_TOTAL_AMOUT) + "BTC")

if floating_income < 0:
    print(cs(("当前卖价：" + str(best_otc_price)), "#F75959"))
    print(cs(("浮动盈亏：" + str(floating_income)), "#F75959"))

else:
    print(cs(("当前卖价：" + str(best_otc_price)), "#42FFA4"))
    print(cs(("浮动盈亏：+" + str(floating_income)), "#ffff87"))



# print
