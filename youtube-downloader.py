import pytube
import os
import subprocess #커맨드 환경 관련

a = input("다운받을 유튜브 영상 url 입력:")
yt = pytube.YouTube(a) # 다운 받을 영상 URL 지정
videos = yt.streams.all()

for i in range(len(videos)):
    print(i,' , ', videos[i])

cNum = int(input("다운 받을 화질넘버 : "))

down_dir = "D:\youtube"

videos[cNum].download(down_dir)

newFileName = input("변환 할 mp3 파일명은?(.mp3포함 입력)")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg','-i',
                os.path.join(down_dir,oriFileName),
                os.path.join(down_dir,newFileName)]) #커맨드 명령어부분
print("동영상 다운로드 및 mp3 변환 완료!")
#python D:\PythonData\Atomproject\youtube-downloader.py 실행
