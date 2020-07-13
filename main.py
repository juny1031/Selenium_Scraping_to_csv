from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd

# Seleniumをあらゆる環境で起動させるChromeオプション
options = Options()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');
# options.add_argument('--headless'); # ※ヘッドレスモードを使用する場合、コメントアウトを外す

DRIVER_PATH = 'パス'
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)


list = []
for i in range(1,14):
  url = 'URL'+ str(i)
  driver.get(url)
  time.sleep(90)
  html = driver.page_source.encode('utf-8')
  soup = BeautifulSoup(html, 'html.parser')
  titles =soup.select("h2 a")
  for title in titles:
    name = title.text
    link = title.get("href")
    list.append([name,link])

df = pd.DataFrame(list)
df.to_csv("ファイル名.csv", encoding='utf_8_sig')