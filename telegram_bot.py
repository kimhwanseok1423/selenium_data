import requests
import json
from bs4 import BeautifulSoup

bot_token="7409964283:AAFibCbNUPYbxrk7Woa796y5JyfY0RZ-NKI"
def get_updates():
    url=f"https://api.telegram.org/bot{bot_token}/getUpdates"

    res=requests.get(url)

    print(res)

    if res.status_code==200:
        return json.loads(res.text)
    
    # .. # 
chat_id= "7768980985"
def send_message(message=None):
    if not message:
        message=input("message: ")
    data={"chat_id":chat_id,"text":message}

    url=f"https://api.telegram.org/bot{bot_token}/sendMessage"
    res=requests.get(url,data=data)
    if res.status_code==200:
        return json.loads(res.text)

keyword=input("keyword : ")
url=f"https://search.naver.com/search.naver?where=nexearch&query={keyword}"

res=requests.get(url)

if res.status_code==200:
    html=res.text
    soup=BeautifulSoup(html,"html.parser")
    new_title=soup.select(".BHYkUbEQ2afEbTC7LXoA.tQzTN_dJmfJcpqVyJEAz")

    title_list=[]
    

    for title in new_title:
        print(title.text)
        print(title["href"])

        title_list.append(f"{title.text}\n{title['href']}")
        print ()
    message="\n\n".join(title_list)

    send_message(message)       


 