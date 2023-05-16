import os
from pydub import AudioSegment

# Get directory path
path = os.getcwd()

# Get all files in directory
files = os.listdir(path)

# Loop through files
for file in files:
    # Check if file is a mp4
    if file.endswith('.mp4'):
        # Get file name
        name = os.path.splitext(file)[0]

        # Create mp3 file name
        mp3 = name + '.mp3'

        # Convert mp4 to mp3
        print(f'Converting {file} to {mp3}...')

        # Carga el archivo de video con pydub
        video = AudioSegment.from_file(file)

        # Extrae el audio del archivo de video
        audio = video.export(mp3, format="mp3")

        # Delete mp4 file
        os.remove(file)
        audio.close()

print('Done')
