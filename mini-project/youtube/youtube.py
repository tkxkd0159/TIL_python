import os
import youtube_dl

os.chdir('./mini-project/youtube')

ydl_opt = {
    'outtmpl': '%(title)s %(resolution)s.%(ext)s'
}

with youtube_dl.YoutubeDL() as ydl:
    ydl.download(["https://www.youtube.com/playlist?list=PLSN_PltQeOyjmRIsC7VNirXOBqWoypd4V"])