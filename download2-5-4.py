from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
<div id="main">
  <h1>강의목록</h1>
  <ul class="lecs">
    <li>Java 초고수 되기</li>
    <li>파이썬 기초 프로그래밍</li>
    <li>파이썬 머신러닝 프로그래밍</li>
    <li>안드로이드 블루투스 프로그래밍</li>
  </ul>
  <p id="ahd">안홍덕</p>
</div>
<div id="sub">
    <p>ㅎㅇㅎㅇ</p>
    <p>gdgd</p>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

h1= soup.select("div#main > h1") #가져올게 하나면 select_one 사용
print(h1) # list라서 그냥 h1.string하면 오류남 for문 써야함
list_li = soup.select("div#main > ul.lecs > li")
for li in list_li:
    print("li>>",li.string)

p=soup.select("#sub>p")
for i in p:
    print(i.string)
