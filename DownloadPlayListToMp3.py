
import pytube
from pydub import AudioSegment
import os

# url = "https://www.youtube.com/watch?v=S9o_fhR2eGY&list=PLyX6kueuK9ugkHPuPlVcIGrUNElm3sQsi"
url = "https://youtube.com/playlist?list=PLoit4GKRCf7hWe_fpZkUpAE2_itli98Gw"

# Crea un objeto Playlist con la URL
playlist = pytube.Playlist(url)

# Obtiene los diferentes URLs de los videos en el álbum
videos = playlist.video_urls

# Descarga cada video en la lista
for video_url in videos:
    # Crea un objeto YouTube con la URL del video
    yt = pytube.YouTube(video_url)
    # stream = yt.streams.filter(only_audio=True).first()
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print(f"Download {yt.title}...")

    # if yt.title.endswith('.'):
        # Ruta del archivo de video a convertir
        # video_path = f"/home/isai/Documents/DownloadMp3Python/{yt.title}mp4"
        # Ruta de salida para el archivo de audio en formato MP3
        # audio_path = f"/home/isai/Documents/DownloadMp3Python/{yt.title}mp3"
    # else:
        # Ruta del archivo de video a convertir
        # video_path = f"/home/isai/Documents/DownloadMp3Python/{yt.title}.mp4"
        # Ruta de salida para el archivo de audio en formato MP3
        # audio_path = f"/home/isai/Documents/DownloadMp3Python/{yt.title}.mp3"

    # print(audio_path, video_path)

    # Carga el archivo de video con pydub
    # video = AudioSegment.from_file(video_path)

    # Extrae el audio del archivo de video
    # audio = video.export(audio_path, format="mp3")

    # os.remove(video_path)
    # audio.close()

print("Done")