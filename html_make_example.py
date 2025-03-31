from datetime import datetime
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
random_sec=random.uniform(1,2)

user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
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










soup=BeautifulSoup(html,"html.parser")

#112312
items=soup.select("[class=search-product]")

main_text = ""
text_block=""
sub_text = ""
sub_text1 = ""
sub_text2 = ""
rank=1
for item in items:
    badge_rocket=item.select_one(".badge.rocket")
    if not badge_rocket:
        continue
    name=item.select_one(".name")
    price=item.select_one(".price-value")
    thumb=item.select_one(".search-product-wrap-img")
    link=item.a["href"]
    link=f"https://coupang.com{link}"


  
    print(f"{rank}위")
    print(name.text)
    print(f"{price.text} 원")
    print(link)
    if thumb.get("data-img-src"):
        img_url=f"http:{thumb.get('data-img-src')})"
        img_url=img_url.rstrip(')')
        
    else:
        img_url=f"http:{thumb['src']}"
        
	
	
        
    img_url=img_url.replace("320x320ex","350x350ex")
    img_url=img_url.rstrip(')')
    print(img_url)
    print()
    
    # if rank == 1:
    #     main_text = f"<a href='{link}' target='_blank' class='image featured'><img src='{img_url}' alt='' /></a> <p><h2>{rank}위:{name.text}</h2><b> 가격 : {price.text}원</b></p>"
   
    # elif rank % 3 == 1:
    #     sub_text += f"<a href='{link}' target='_blank' class='image featured'><img src='{img_url}' alt='' /></a> <p><h3>{rank}위:{name.text}</h3><b> 가격 : {price.text}원</b></p><ul class='actions'><li><a href='#' class='button style1'>Learn More</a></li>"

    # elif rank % 3 == 2:
    #     sub_text1 += f"<a href='{link}' target='_blank' class='image featured'><img src='{img_url}' alt='' /></a> <p><h3>{rank}위:{name.text}</h3><b> 가격 : {price.text}원</b></p><ul class='actions'><li><a href='#' class='button style1'>Learn More</a></li>"

    # elif rank % 3 == 0:
    #     sub_text2 += f"<a href='{link}' target='_blank' class='image featured'><img src='{img_url}' alt='' /></a> <p><h3>{rank}위:{name.text}</h3><b> 가격 : {price.text}원</b></p><ul class='actions'><li><a href='#' class='button style1'>Learn More</a></li>"
    if rank == 1:
        main_text = f"""<a href='{link}' target='_blank' class='image featured'><img src='{img_url}' alt='' /></a> <p><h2>{rank}위: {name.text}</h2><b> 가격 : {price.text}원</b></p>"""
    else:
          text_block = f"""<a href='{link}' target='_blank' class='image featured'><img src='{img_url}' alt='' /></a> <p><h3>{rank}위: {name.text}</h3><b> 가격 : {price.text}원</b></p><ul class='actions'><li><a href='#' class='button style1'>Learn More</a></li>"""
          if rank % 3 == 1:
             sub_text += text_block
          elif rank % 3 == 2:
             sub_text1 += text_block
          else:
             sub_text2 += text_block
   
    rank +=1

    if rank == 11:
        break
    

time.sleep(random_sec)
driver.quit()


now=datetime.now()
today_date=f"{now.year}년 {now.month}월 {now.day}일"

#파이썬으로 html만들기
# 쿠팡 셀레니움 크롤링
file_name="index.html"
title_text=f"오늘의 {keyword} 인기상품"
summary_text= f"{today_date}, {keyword}의 최신 인기상품을 확인하세요!"
title_main="쿠팡 실시간 인기상품 랭킹 크롤링"
title_sub="최신 상품 순위 자동 수집하기"
html_text=f"""
<!DOCTYPE HTML>

<html>
	<head>
		<title>No Sidebar - Escape Velocity by HTML5 UP</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
	</head>
	<body class="no-sidebar is-preload">
		<div id="page-wrapper">

			<!-- Header -->
				<section id="header" class="wrapper">

					<!-- Logo -->
						<div id="logo">
							<h1><a href="index.html">{title_main}</a></h1>
							<p>{title_sub}</p>
						</div>

				

				</section>

			<!-- Main -->
				<div id="main" class="wrapper style2">
					 <div class="title">{today_date}</div> 
					<div class="container">

						<!-- Content -->
							<div id="content">
								<article class="box post">
									<header class="style1">
										<h2>{title_text}</h2>
										<p><{summary_text}/p>
									</header>
                                    
								
									{main_text}


								

								</article>
							</div>

					</div>
				</div>

			<!-- Highlights -->
				<section id="highlights" class="wrapper style3">
					<div class="title">"인기상품 TOP10"</div>
					<div class="container">
						<div class="row aln-center">
							<div class="col-4 col-12-medium">
								<section class="highlight">
								
									{sub_text}
									
									
								</section>
							</div>
							<div class="col-4 col-12-medium">
								<section class="highlight">
									{sub_text1}
								
								</section>
							</div>
							<div class="col-4 col-12-medium">
								<section class="highlight">
									{sub_text2}
								
								</section>
							</div>
						</div>
					</div>
				</section>

			

							</div>
						
						</div>
						<div id="copyright">
							<ul>
								<li>&copy; Untitled.</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
							</ul>
						</div>
					</div>
				</section> 

		</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.dropotron.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>
"""
with open(f"html5up-escape-velocity/{file_name}","w",encoding="utf-8") as f:
    f.write(f"{html_text}")

    