from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

options=Options()
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"

options.add_argument(f"user-agent={user_agent}")
options.add_argument("--start-maximized")
## 화면 안꺼짐 이거있으면

options.add_experimental_option("detach",True)

options.add_experimental_option("excludeSwitches",["enable-logging"])

url="https://search.shopping.naver.com/ns/search?query="
keyword=input("검색할 제품을 입력하세요 :")
base_url=url+keyword
service=Service(ChromeDriverManager().install())


driver=webdriver.Chrome(service=service,options=options)
driver.implicitly_wait(10)
driver.get(base_url)
time.sleep(2)

driver.execute_script("window.scrollTo(0,2000)")
time.sleep(2)

html=driver.page_source
driver.quit()


soup=BeautifulSoup(html,"html.parser")

# print(html[:1000])
## class가 뒤에 __T떙떙떙 처럼 자주바뀌기 때문에 class를 이런식으로 하면 뒤에껄 안쓰고 할수있음
base_divs=soup.select("[class^=basicProductCard_basic_product_card]")
print(len(base_divs))

main_text_list=[]
for base_div in base_divs:

    ad_button=base_div.select_one("[class^=advertisementTag_icon]")
    
    if ad_button:
        
        continue

    title=base_div.select_one("[class^=basicProductCardInformation_title]")
    price=base_div.select_one("[class^=basicProductCardInformation_wrap_price]")
    


    title_text=title.text

    # if문으로 똥꼬쇼안하고 스페이스 필요한자리에 자동으로 채워주더라.. 사기야 이건 
    price_text=price.get_text(" ")

   


    prod_text=f"{title_text}  |  {price_text}"
    print(prod_text)
    print()

    

print(prod_text)
driver.quit()