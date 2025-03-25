
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import time
import random


# 123456
random_sec=random.uniform(3,5)

user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
options=Options()
print(random_sec)
options.add_argument(f"user-agent={user_agent}")
options.add_argument('accept-language=ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7') 
options.add_argument("--start-maximized")
options.add_experimental_option("detach",True)
options.add_experimental_option("excludeSwitches",["enable-logging"])
options.add_argument("--disable-blink-features=AutomationControlled")

base_url="https://www.coupang.com/np/search?component=&q="

keyword=input("검색할 상품을 입력하세요 : ")

search_url=base_url+keyword
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=options)

driver.get(search_url)


time.sleep(random_sec)

html=driver.page_source

driver.quit()

soup=BeautifulSoup(html,"html.parser")

#112312
items=soup.select("[class=search-product]")

rank=1
for item in items:
    badge_rocket=item.select_one(".badge.rocket")
    if not badge_rocket:
        continue
    name=item.select_one(".name")
    price=item.select_one(".price-value")
    thumb=item.select_one(".search-product-wrap-img")
    link=item.a["href"]


  
    print(f"{rank}위")
    print(name.text)
    print(f"{price.text} 원")
    print(f"https://coupang.com{link}")
    if thumb.get("data-img-src"):
        img_url=f"http:{thumb.get('data-img-src')})"
        
    else:
        img_url=f"http:{thumb['src']}"
        

    print(img_url)
    print()
   


    rank+=1

time.sleep(random_sec)



