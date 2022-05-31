import requests
import json
import os
import re
from bs4 import BeautifulSoup

hotpage = requests.get("https://tw.yahoo.com/")
main = BeautifulSoup(hotpage.text, 'html.parser')
print(main.text) #這裡可以print看看已抓取到除標籤外的文字