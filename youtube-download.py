import os
import tkinter as tk
from pytube import YouTube, Playlist
from moviepy.editor import AudioFileClip

def get_music_directory():
    music_dir = os.path.join(os.path.expanduser('~'), 'Music')
    return music_dir

def format_folder_name(name):
    return "".join(x for x in name if x.isalnum() or x in (' ', '.', '_')).rstrip()

def download_video_or_playlist():
    url = entry.get()
    try:
        if is_playlist(url):
            download_playlist(url)
        else:
            download_video(url)
    except Exception as e:
        status_text.insert(tk.END, f"Erro: {str(e)}\n")
    finally:
        status_text.yview_moveto(1)

def is_playlist(url):
    return 'list=' in url.lower()

def download_playlist(url):
    playlist = Playlist(url)
    music_dir = get_music_directory()
    
    playlist_folder_name = format_folder_name(playlist.title)
    playlist_folder = os.path.join(music_dir, playlist_folder_name)
    os.makedirs(playlist_folder, exist_ok=True)
    
    total_videos = len(playlist.video_urls)
    for idx, video_url in enumerate(playlist.video_urls):
        try:
            yt = YouTube(video_url)
            stream = yt.streams.filter(only_audio=True).first()
            audio_file = stream.download(output_path=playlist_folder)
            base, ext = os.path.splitext(audio_file)
            new_file = base + '.mp3'
            audio = AudioFileClip(audio_file)
            audio.write_audiofile(new_file)
            os.remove(audio_file)
            status_text.insert(tk.END, f"Música {idx + 1}/{total_videos} baixada: {yt.title}\n")
            status_text.update()
            status_text.yview_moveto(1)
        except Exception as e:
            status_text.insert(tk.END, f"Erro ao baixar música: {str(e)}\n")
    status_text.insert(tk.END, 'Playlist baixada com sucesso!\n')
    status_text.yview_moveto(1)

def download_video(url):
    try:
        yt = YouTube(url)
        music_dir = get_music_directory()
        stream = yt.streams.filter(only_audio=True).first()
        audio_file = stream.download(output_path=music_dir)
        base, ext = os.path.splitext(audio_file)
        new_file = base + '.mp3'
        audio = AudioFileClip(audio_file)
        audio.write_audiofile(new_file)
        os.remove(audio_file)
        status_text.insert(tk.END, 'Música baixada com sucesso!\n')
    except Exception as e:
        status_text.insert(tk.END, f"Erro ao baixar música: {str(e)}\n")
    finally:
        status_text.yview_moveto(1)

def create_interface():
    root = tk.Tk()
    root.title("Baixar Música do YouTube")
    root.geometry("600x200")
    root.configure(bg='white')
    
    label = tk.Label(root, text="Cole a URL de sua playlist ou música abaixo e clique em baixar", bg='white', font=('Arial', 12))
    label.pack(pady=10)
    
    global entry
    entry = tk.Entry(root, width=60)
    entry.pack(padx=20)
    
    button = tk.Button(root, text="Baixar", command=download_video_or_playlist, bg='#4CAF50', fg='white')
    button.pack(pady=10)
    
    global status_text
    status_text = tk.Text(root, height=5, width=70)
    status_text.pack(padx=20, pady=10)
    status_text.config(yscrollcommand=tk.Scrollbar(root, orient=tk.VERTICAL, command=status_text.yview).set)
    
    root.mainloop()

# Chamando a função para criar a interface
create_interface()
