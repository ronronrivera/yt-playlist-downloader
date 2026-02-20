import yt_dlp
import sys
from pathlib import Path


def download_playlist_video(playlist_url: str):
    video_path = Path.home() / "Videos"      
    video_path.mkdir(parents=True, exist_ok=True)

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',

        'outtmpl': str(video_path / "%(playlist_title)s/%(title)s.%(ext)s"),

        'ignoreerrors': False,

        'writethumbnail': True,
        'postprocessors': [
            {
                'key': 'EmbedThumbnail',
            },
            {
                'key': 'FFmpegMetadata',
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])


if len(sys.argv) < 2:
    print("Usage: python downloader.py <playlist_url>")
    sys.exit(1)

url = sys.argv[1]
download_playlist_video(url)
