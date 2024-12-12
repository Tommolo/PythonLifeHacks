import os

def remove_spotify_from_filenames(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.mp3'):
                file_path = os.path.join(root, file_name)
                # Crea il nuovo nome del file senza "[SPOTIFY-DOWNLOADER.COM] "
                new_file_name = file_name.replace("[SPOTIFY-DOWNLOADER.COM] ", "")
                new_file_path = os.path.join(root, new_file_name)
                # Rinomina il file
                os.rename(file_path, new_file_path)


folder_path = r"C:\Users\pieru\Desktop\Musica_festa\Annuel"
remove_spotify_from_filenames(folder_path)
