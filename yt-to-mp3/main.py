from __future__ import unicode_literals
import youtube_dl
print("Insert the YouTube link")
link = input ("")

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '144',
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])