import sys
sys.path.append("packages")
import os
import json

from yt_dlp import YoutubeDL

name = "World"
if not os.isatty(sys.stdin.fileno()):
    obj = json.loads(sys.stdin.read())
    if obj["name"] != "":
        name = obj["name"]

    URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']
    with YoutubeDL() as ydl:
        ydl.download(URLS)

print(f"Hello {name} !!!")
