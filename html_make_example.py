from datetime import datetime

now=datetime.now()
today_date=f"{now.year}년 {now.month}월 {now.day}일"

#파이썬으로 html만들기
# 쿠팡 셀레니움 크롤링
file_name="index.html"
title_text="연습용 웹사이트"

main_text="<p>연습 웹사이트 첫번째<br>연습 웹사이트 첫번째<br>연습 웹사이트 첫번째<br></p>"
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
							<h1><a href="index.html">Escape Velocity</a></h1>
							<p>A free responsive site template by HTML5 UP</p>
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
										<p>Tempus feugiat veroeros sed nullam dolore</p>
									</header>
									<a href="#" class="image featured">
										<img src="images/pic01.jpg" alt="" />
									</a>
									{main_text}


								

								</article>
							</div>

					</div>
				</div>

			<!-- Highlights -->
				<section id="highlights" class="wrapper style3">
					<div class="title">The Endorsements</div>
					<div class="container">
						<div class="row aln-center">
							<div class="col-4 col-12-medium">
								<section class="highlight">
									<a href="#" class="image featured"><img src="images/pic02.jpg" alt="" /></a>
									<h3><a href="#">Aliquam diam consequat</a></h3>
									<p>Eget mattis at, laoreet vel amet sed velit aliquam diam ante, dolor aliquet sit amet vulputate mattis amet laoreet lorem.</p>
									<ul class="actions">
										<li><a href="#" class="button style1">Learn More</a></li>
									</ul>
								</section>
							</div>
							<div class="col-4 col-12-medium">
								<section class="highlight">
									<a href="#" class="image featured"><img src="images/pic03.jpg" alt="" /></a>
									<h3><a href="#">Nisl adipiscing sed lorem</a></h3>
									<p>Eget mattis at, laoreet vel amet sed velit aliquam diam ante, dolor aliquet sit amet vulputate mattis amet laoreet lorem.</p>
									<ul class="actions">
										<li><a href="#" class="button style1">Learn More</a></li>
									</ul>
								</section>
							</div>
							<div class="col-4 col-12-medium">
								<section class="highlight">
									<a href="#" class="image featured"><img src="images/pic04.jpg" alt="" /></a>
									<h3><a href="#">Mattis tempus lorem</a></h3>
									<p>Eget mattis at, laoreet vel amet sed velit aliquam diam ante, dolor aliquet sit amet vulputate mattis amet laoreet lorem.</p>
									<ul class="actions">
										<li><a href="#" class="button style1">Learn More</a></li>
									</ul>
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

    