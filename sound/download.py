# pip install pytube
# pip install os
# https://shawsk.tistory.com/entry/python-youtube-mp3-converter
from pytube import YouTube
import os

link = input("Enter a youtube video's URL")
yt = YouTube(link)
filePath = yt.streams.filter(only_audio=True).first().download()
wavFilePath = filePath.replace("mp4", "wav")
os.rename(filePath, wavFilePath)
# print(f"")