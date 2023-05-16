## Instalaciones necesarias:
## Instalamos ffmpeg
## sudo apt install ffmpeg
## Libreria de audio
## pip install pydub
## Libreria de video
## pip install pytube

from pytube import *
# from moviepy.video.io.VideoFileClip import VideoFileClip
from pydub import AudioSegment

import os

# Link to download
video_url = "https://www.youtube.com/watch?v=djRxYZQSe_k"

# Download video from YouTube
yt = YouTube(video_url)
stream = yt.streams.get_highest_resolution()
stream.download()

# Convierte el archivo de video descargado a MP3

# Ruta del archivo de video a convertir
video_path = f"/home/isai/Documents/DownloadMp3Python/{yt.title}mp4"

# Ruta de salida para el archivo de audio en formato MP3
# audio_path = f"/home/isai/Documents/DownloadMp3Python/{yt.title}mp3"

print(video_path)

# Crea un objeto VideoFileClip con el archivo de video
# video = VideoFileClip(video_path)

# Extrae la pista de audio del archivo de video
# audio = video.audio

# Extrae la pista de audio del archivo de video y guárdalo como un archivo de audio
# os.system(f"ffmpeg -i {video_path} -vn -acodec libmp3lame {audio_path}")


# Crea un archivo de audio en formato MP3
# audio.write_audiofile(audio_path)


# Carga el archivo de video con pydub
# video = AudioSegment.from_file(video_path)

# Extrae el audio del archivo de video
# audio = video.export(audio_path, format="mp3")

# Elimina el archivo de video
# video.close()

# os.remove(video_path)
# cerrar el audio
# audio.close()