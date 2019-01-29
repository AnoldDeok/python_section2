import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://blogfiles.naver.net/20120717_72/sunjahwang_1342512929146R1wSv_JPEG/%B5%BF%B9%B00_%28411%29.jpg"
htmlURL = "http://google.com"

savefile1 = "c:/test1.jpg"
savefile2 = "c:/index.html"

dw.urlretrieve(imgUrl,savefile1)
dw.urlretrieve(htmlURL,savefile2)
print("다운 완료")
