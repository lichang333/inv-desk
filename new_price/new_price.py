# -*- coding: UTF-8 -*-

import requests, json, math, os


OLD_BTC_AVERAGE_PRICE = 63829.787234
OLD_BTC_AMOUNT = 0.047

NEW_BTC_BUY_PRICE = 10000
NEW_BTC_AMOUNT = 0.016142571188738943

# calculating...
old_total_invest = OLD_BTC_AVERAGE_PRICE * OLD_BTC_AMOUNT
new_additional_invest = NEW_BTC_BUY_PRICE * NEW_BTC_AMOUNT

new_total_invest = old_total_invest + new_additional_invest
new_total_amount = OLD_BTC_AMOUNT + NEW_BTC_AMOUNT
new_average_price = new_total_invest / new_total_amount



print("旧买入均价: " + str(OLD_BTC_AVERAGE_PRICE))
print("旧持仓量: " + str(OLD_BTC_AMOUNT) + " BTC.")
print("\n")
print("新买入均价: " + str(new_average_price))
print("新持仓量: " + str(new_total_amount) + " BTC.")
