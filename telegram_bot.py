import requests



bot_token="7172527809:AAHDa9sGKvF9wkB8yj4hs7hcXJ_31kDrlDk"
url=f"https://api.telegram.org/bot{bot_token}/getUpdates"

res=requests.get(url)

print(res)

if res.status_code==200:
    print(res.text)