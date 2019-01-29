import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

img = "https://ssl.pstatic.net/tveta/libs/1217/1217834/9f36ca0e548069b8da58_20181224134141457_1.jpg"
mp4 = "https://tvetamovie.pstatic.net/libs/1222/1222371/078c6b5e02417d0e2ebe_20181214162656677.mp4-pBASE-v0-f70720-20181214162840624.mp4"

saveimg = "c:/img1.jpg"
savemp4 = "c:/youngsang1.mp4"

a=req.urlopen(img).read()
b=req.urlopen(mp4).read()

with open(saveimg,'wb') as imgsave:
    imgsave.write(a)
with open(savemp4,'wb') as mp4save:
    mp4save.write(b)
print("완료")
