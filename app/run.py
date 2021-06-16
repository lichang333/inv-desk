# -*- coding: UTF-8 -*-
import os, time

# clear screen on linux / os x
os.system('clear')

def current_time():
    print_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(print_time)

def run():
    current_time()
    # os.system("python3 get_otc_usdt_price.py")
    # print("\n")
    # os.system("python3 get_otc_btc_price.py")
    # print("\n")
    os.system("python3 get_cmb_gold_price.py")
    print("\n")

while True:
    run()
    time.sleep(1800)
