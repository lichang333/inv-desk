# -*- coding: UTF-8 -*-

import requests, json, math, os
from stringcolor import * 

USDT_TOTAL_AMOUT = 559.44    
USDT_EVERYAGER_BUY_PRICE = 7.15

# clear screen on linux / os x
os.system('clear')  

content = requests.get("https://otc-api-hk.eiijo.cn/v1/data/trade-market?coinId=2&currency=1&tradeType=buy&currPage=1&payMethod=0&country=37&blockType=general&online=1&range=0&amount=")
json = json.loads(content.content)

# Show the best price for sell USDT/CNY on Huobi
best_otc_price = (json["data"][0]["price"])


# calculating...
floating_income_origin = USDT_TOTAL_AMOUT * (best_otc_price - USDT_EVERYAGER_BUY_PRICE)

# remain 2 decimal
floating_income = (round(floating_income_origin, 2))

# Print

print("USDT/CNY")

print("买入均价：" + str(USDT_EVERYAGER_BUY_PRICE))
print ("持仓量：" + str(USDT_TOTAL_AMOUT) + "USDT")

if floating_income < 0:
    print(cs(("当前卖价：" + str(best_otc_price)), "#F75959"))
    print(cs(("浮动盈亏：" + str(floating_income)), "#F75959"))  
    
else:
    print(cs(("当前卖价：" + str(best_otc_price)), "#42FFA4"))
    print(cs(("浮动盈亏：+" + str(floating_income)), "#ffff87"))  



# print
