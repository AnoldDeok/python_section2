from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html="""
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.google.com">google</a></li>
        <li><a href="http://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")

a = soup.find_all("a",string='daum') #daum 포함하는 태그
b = soup.find_all("a",limit=3)
c = soup.find_all(string=["naver","google"]) ##해당 스트링만 반환


for i in links:
    #print('i',type(i),i)
    href = i.attrs['href']   #딕셔너리 형식이라 href가 키 values가 dns주소가 돼
    txt = i.string   # string만 가져옴
    print("txt>>",txt,'href >>',href)
