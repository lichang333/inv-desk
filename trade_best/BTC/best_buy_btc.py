# -*- coding: UTF-8 -*-

import requests, json, math, os
from stringcolor import *

# The Money you have
CNY_TO_BUY = 1000

# Get APIs:
print("Rates: ")
    # Get USDT/CNY OTC though Huobi API:
content = requests.get("https://otc-api-hk.eiijo.cn/v1/data/trade-market?coinId=2&currency=1&tradeType=sell&currPage=1&payMethod=0&country=37&blockType=general&online=1&range=0&amount=")
usdt_cny_json = json.loads(content.content)
usdt_to_cny_price = (usdt_cny_json["data"][0]["price"])
print("USDT/CNY: "+ str(usdt_to_cny_price))

    # Get USDT/CNY API for Wechat API:
content = requests.get("https://otc-api-hk.eiijo.cn/v1/data/trade-market?coinId=2&currency=1&tradeType=sell&currPage=1&payMethod=3&country=&blockType=general&online=1&range=0&amount=")
usdt_to_cny_wechat_json = json.loads(content.content)
usdt_to_cny_wechat = (usdt_to_cny_wechat_json["data"][0]["price"])
print("USDT/wxCNY: "+ str(usdt_to_cny_wechat))

    # Get BTC/USDT API on cryptocompare:
content = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USDT")
btc_to_usdt_json = json.loads(content.content)
btc_to_usdt = btc_to_usdt_json["USDT"]
print("BTC/USDT: "+str(btc_to_usdt))

    # Get BTC/CNY OTC though Huobi API:
content = requests.get("https://otc-api-hk.eiijo.cn/v1/data/trade-market?coinId=1&currency=1&tradeType=sell&currPage=1&payMethod=0&country=37&blockType=general&online=1&range=0&amount=")
btc_to_cny_json = json.loads(content.content)
btc_to_cny_price = (btc_to_cny_json["data"][0]["price"])
print("BTC/CNY: "+ str(btc_to_cny_price))

    # Get BTC/CNY API for Wechat API:
content = requests.get("https://otc-api-hk.eiijo.cn/v1/data/trade-market?coinId=1&currency=1&tradeType=sell&currPage=1&payMethod=3&country=37&blockType=general&online=1&range=0&amount=")
btc_to_cny_wechat_json = json.loads(content.content)
btc_to_cny_wechat = (btc_to_cny_wechat_json["data"][0]["price"])
print("BTC/wxCNY: "+ str(btc_to_cny_wechat))


# Calculate How Much BTC you can get:
print("\n\n")
print(str(CNY_TO_BUY)+" CNY 所能获得的比特币：")

# Trade BTC though USDT:
cny_usdt_btc_result = CNY_TO_BUY / usdt_to_cny_price / btc_to_usdt
print("\n")
print("通过USDT交易: ")
print("CNY -> USDT -> BTC: "+ str(cny_usdt_btc_result))

# CNY(wx) -> USDT -> BTC:
wxcny_usdt_btc_result = CNY_TO_BUY / usdt_to_cny_wechat / btc_to_usdt
print("wxCNY -> USDT -> BTC: "+str(wxcny_usdt_btc_result))

# Claculate Wechat loss:
cny_usdt_btc_loss = cny_usdt_btc_result - wxcny_usdt_btc_result
cny_usdt_btc_loss_in_usdt = cny_usdt_btc_loss * btc_to_usdt
print("交易差额: " + str(cny_usdt_btc_loss) +
" BTC.   \n约合USDT: " + str(cny_usdt_btc_loss_in_usdt) +
", 人民币: "+ str(cny_usdt_btc_loss_in_usdt*usdt_to_cny_price))


# Trade BTC though OTC:
print("\n")
print("通过Huobi OTC交易: ")
# CNY -> BTC:
cny_to_btc = CNY_TO_BUY / btc_to_cny_price
print("CNY -> BTC: " + str(cny_to_btc))

# CNY(wx) -> BTC:
wxcny_to_btc = CNY_TO_BUY / btc_to_cny_wechat
print("wxCNY -> BTC: " + str(wxcny_to_btc))
# Claculate Wechat loss:
cny_btc_loss = cny_to_btc - wxcny_to_btc
cny_btc_loss_in_usdt = cny_btc_loss * btc_to_usdt
print("交易差额: " + str(cny_btc_loss) + " BTC" )
print("约合USDT: " + str(cny_btc_loss_in_usdt) +
", 人民币: "+ str(cny_btc_loss_in_usdt*usdt_to_cny_price))

usdt_cny_remind = cny_usdt_btc_result - cny_to_btc
# print("\n\nUSDT-OTC: "+str(usdt_cny_remind))
print("微信手续费: "+str(CNY_TO_BUY*0.001))


# Step 4:
# Print: Highest BTC option.


# GOLD_TOTAL_GRAMS = 111.4889

# gold_everage_buying_price = GOLD_TOTAL_COST / GOLD_TOTAL_GRAMS

# clear screen on linux / os x
# os.system('clear')



# Fetch Current Gold Price from CMB API
# gold_cmb_price = (json["data"][1]["CurPrice"])

# calculating...

# floating_income_origin = GOLD_TOTAL_GRAMS * (float(gold_cmb_price) - gold_everage_buying_price)

# remain 2 decimal
# floating_income = (round(floating_income_origin, 2))

# Print
# print("Au(T+D)/CNY")

# print("买入均价：" + str((round(gold_everage_buying_price, 2))))
# print ("持仓量：" + str(GOLD_TOTAL_GRAMS) + "g")
#
# if floating_income < 0:
#     print(cs(("当前金价：" + str(gold_cmb_price)), "#F75959"))
#     print(cs(("浮动盈亏：" + str(floating_income)), "#F75959"))
#
# else:
#     print(cs(("当前卖价：" + str(gold_cmb_price)), "#42FFA4"))
#     print(cs(("浮动盈亏：+" + str(floating_income)), "#ffff87"))



# print
