import sys
import os
from pytube import YouTube
from pytube import Playlist

DOWNLOAD_PATH = "C:\\Users\\Adi Mishael\\Downloads"  # Change this to your desired download directory

def download_video(url, format, playlist_name=None):
    try:
        yt = YouTube(url)
        if format.lower() == "mp3":
            stream = yt.streams.filter(only_audio=True).first()
        else:
            stream = yt.streams.get_highest_resolution()
        
        if playlist_name:
            playlist_folder = os.path.join(DOWNLOAD_PATH, playlist_name)
            if not os.path.exists(playlist_folder):
                os.makedirs(playlist_folder)
            output_path = playlist_folder
        else:
            output_path = DOWNLOAD_PATH
        
        print(f"Downloading: {yt.title}...")
        stream.download(output_path=output_path)
        
        # If downloading as MP3, convert the downloaded file to MP3 format
        if format.lower() == "mp3":
            mp4_file = os.path.join(output_path, stream.default_filename)
            mp3_file = os.path.splitext(mp4_file)[0] + ".mp3"
            os.rename(mp4_file, mp3_file)
        
        print("Download completed successfully!")
    except Exception as e:
        print(f"Error downloading file: {str(e)}")

def download_playlist(playlist_url, format):
    try:
        playlist = Playlist(playlist_url)
        playlist_name = playlist.title
        if format == "mp4":
         print(f"Downloading {len(playlist)} videos from the playlist '{playlist_name}'...")
        else: 
         print(f"Downloading {len(playlist)} audio files from the playlist '{playlist_name}'...")

        for video_url in playlist.video_urls:
            download_video(video_url, format, playlist_name)
        print("Download completed successfully!")
    except Exception as e:
        print(f"Error downloading playlist: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python yt_downloader.py <video_or_playlist_url> <format>")
        sys.exit(1)
    
    url = sys.argv[1]
    format = sys.argv[2]

    if "/playlist?" in url:
        download_playlist(url, format)
    else:
        download_video(url, format)
