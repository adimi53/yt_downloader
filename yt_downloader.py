import sys
from pytube import YouTube, Playlist

DOWNLOAD_PATH = "C:\\Users\\Adi Mishael\\Downloads"  # Change this to your desired download directory

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}...")
        stream.download(output_path=DOWNLOAD_PATH)
        print("Download completed successfully!")
    except Exception as e:
        print(f"Error downloading video: {str(e)}")

def download_playlist(playlist_url):
    try:
        playlist = Playlist(playlist_url)
        print(f"Downloading {len(playlist)} videos from the playlist...")
        for video_url in playlist.video_urls:
            download_video(video_url)
        print("Download completed successfully!")
    except Exception as e:
        print(f"Error downloading playlist: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python download_video.py <video_or_playlist_url>")
        sys.exit(1)
    
    url = sys.argv[1]

    if "/playlist?" in url:
        download_playlist(url)
    else:
        download_video(url)
