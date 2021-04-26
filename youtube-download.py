import youtube_dl
import os

while(True):
    #os.chdir('C:/Users/cardo/Music/')
    link_youtube=input('Cole a URL de sua música ou playlist: ')

    file_format = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(file_format) as audio:
        audio.download([link_youtube])
 
