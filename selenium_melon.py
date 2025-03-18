from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

options=Options()
user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"

options.add_argument(f"user-agent={user_agent}")
options.add_argument("--start-maximized")
## 화면 안꺼짐 이거있으면

options.add_experimental_option("detach",True)

options.add_experimental_option("excludeSwitches",["enable-logging"])

service=Service(ChromeDriverManager().install())

driver=webdriver.Chrome(service=service,options=options)

 
url="https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(2)

if driver.current_url != url:
    driver.get(url)
    time.sleep(2)

driver.find_element(By.LINK_TEXT,"멜론차트").click()

driver.find_elements(By.ID,"moreBtn")[1].click()
time.sleep(2)

chat_list=driver.find_element(By.ID,"_chartList")

items=chat_list.find_elements(By.CLASS_NAME,"list_item")





action=ActionChains(driver)


# element로 이동 내가원한건 90번째 위치로 가게끔
# action.move_to_element(items[90]).perform()

# 10개씩 내려서 보여줌
for rank,item in enumerate(items[:10],1) :
    action.move_to_element(item).perform()
    name=item.find_element(By.CLASS_NAME,"name.ellipsis")
    
    title=item.find_element(By.CLASS_NAME,"title.ellipsis")
    thumb=item.find_element(By.CLASS_NAME,"inner > span")
    thumb.click()
    time.sleep(1)
    album_url=driver.current_url
    driver.back()
    time.sleep(1)


    print(f"<<<{rank}>>>")
    print(name.text)
    print(title.text)
    print(f"album_url : {album_url}")
    print()

    time.sleep(1)

    




# print(len(items))



# driver.quit()


