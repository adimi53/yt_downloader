import sys
from pytube import YouTube

def download_video(url, path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}...")
        stream.download(output_path=path)
        print("Download completed successfully!")
    except Exception as e:
        print(f"Error downloading video: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python download_video.py <video_url>")
        sys.exit(1)
    
    video_url = sys.argv[1]
    #video_url = "https://youtu.be/4Fdwc-Odtmo?si=IKYcsKs8rtPzjkXG"
    download_path = "C:\\Users\\Adi Mishael\\Downloads"  #downloads dir
    download_video(video_url, download_path)
