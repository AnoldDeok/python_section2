import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url="http://www.afreecatv.com/"

mem = req.urlopen(url)

#print(type(mem))
#print(type({}))
#print(type([]))
#print(type(()))

#print("geturl",mem.geturl())
#print("status",mem.status) #200 정상  404낫파운드 403거절 500서버에러
#print("headers",mem.getheaders())
#print("info",mem.info())
#print("code",mem.getcode())
#print("read",mem.read(50).decode("utf-8"))  #50 바이트만큼 가져오기
print(urlparse("http://www.afreecatv.com/")) # 많이사용
