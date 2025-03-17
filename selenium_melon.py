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

chat_list=driver.find_element(By.ID,"_chartList")

items=chat_list.find_elements(By.CLASS_NAME,"list_item")
print(len(items))
driver.quit()


