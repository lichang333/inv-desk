# -*- coding: UTF-8 -*-

import requests, json, math, os
from stringcolor import * 

GOLD_TOTAL_GRAMS = 111.4889
GOLD_TOTAL_COST = 41474
gold_everage_buying_price = GOLD_TOTAL_COST / GOLD_TOTAL_GRAMS



content = requests.get("https://m.cmbchina.com/api/rate/getgoldrate")
json = json.loads(content.content)

# Fetch Current Gold Price from CMB API
gold_cmb_price = (json["data"][1]["CurPrice"])

# calculating...

floating_income_origin = GOLD_TOTAL_GRAMS * (float(gold_cmb_price) - gold_everage_buying_price)

# remain 2 decimal
floating_income = (round(floating_income_origin, 2))

# Print
print("Au(T+D)/CNY")

print("买入均价：" + str((round(gold_everage_buying_price, 2))))
print ("持仓量：" + str(GOLD_TOTAL_GRAMS) + "g")

if floating_income < 0:
    print(cs(("当前金价：" + str(gold_cmb_price)), "#F75959"))
    print(cs(("浮动盈亏：" + str(floating_income)), "#F75959"))  
    
else:
    print(cs(("当前卖价：" + str(gold_cmb_price)), "#42FFA4"))
    print(cs(("浮动盈亏：+" + str(floating_income)), "#ffff87"))  



# print
