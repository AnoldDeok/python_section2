import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://blogfiles.naver.net/20120717_72/sunjahwang_1342512929146R1wSv_JPEG/%B5%BF%B9%B00_%28411%29.jpg"
htmlURL = "http://google.com"

savefile1 = "c:/test1.jpg"
savefile2 = "c:/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

save1 = open(savefile1,'wb')  # w : write    a : add    r : read    b = binary
save1.write(f)
save1.close()


with open(savefile2,'wb') as save2:     # 위에 17~19 줄과 같은 역할
    save2.write(f2)

print("다운 완료")
