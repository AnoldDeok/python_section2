from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
url = "https://www.inflearn.com/%EC%B6%94%EC%B2%9C-%EA%B0%95%EC%A2%8C/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res , "html.parser")

recommand = soup.select("ul.slides")[0]

for i,e in enumerate(recommand,1):
    print(i,e.select_one("h4").string)
