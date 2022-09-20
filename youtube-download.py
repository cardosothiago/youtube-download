import tkinter as tk
import youtube_dl

frame = tk.Tk()
text = tk.Text(frame)
frame.title("YOUTUBE DOWNLOAD")
frame.geometry("800x400")
frame.configure(background="black")


def execute():
    url = inputtxt.get(1.0, "end-1c")
    blank_url = tk.Label(
        frame, text="Link vazio, por favor, coloque um link!", fg="red", bg="black"
    )
    if url:
        download(url)
    else:
        blank_url.grid(row=1, column=2)


def download(url):
    file_format = {
        "format": "bestaudio/best",
        "nocheckcertificate": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with youtube_dl.YoutubeDL(file_format) as audio:
        a = tk.Label(frame, text="")
        audio.download([url])
        a.config(text="MUSICAS BAIXADAS!")
        a.grid(row=1, column=2)


spacer1 = tk.Label(frame, text=None, background="black", height=5, width=70)
spacer1.grid(row=1, column=2)


inputtxt = tk.Text(frame, height=1.4, width=85)

inputtxt.grid(row=6, column=2)

place_holder = tk.Label(
    frame,
    text='Link do Youtube: ',
    bg="black",
    fg="white"
)
place_holder.grid(row=6, column=1)


spacer2 = tk.Label(frame, text=None, background="black", height=1, width=70)
spacer2.grid(row=1, column=2)

download_button = tk.Button(
    frame, text="BAIXAR MÚSICAS", command=execute, fg="green", bg="black"
)
download_button.grid(row=8, column=2)

frame.mainloop()
