import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

i = 1
chrome = webdriver.Chrome()

# Tinderに飛ぶ
chrome.get("https://tinder.com/app/login")

# 手動でログインしたら、yキーを1回押してスタート
key = input('Tinderのトップページが出たらy→Enterを押してください')
if key == "y":
    # ↓の < の右にある数字でフリック数の上限を指定
    while i <= 2000:
        i = i + 1
        chrome.find_element_by_tag_name("body").send_keys(Keys.RIGHT)
        # (a,b)の間の秒数ランダムでフリック
        time.sleep(random.uniform(0.5, 3))
        print(i)
    else:
        print("3000人にいいねしました")
        chrome.close()
