import yt_dlp
import sys
import os

def download_playlist_audio(playlist_url: str):
    
    music_path = os.path.expanduser("~/Music")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{music_path}/%(playlist_title)s/%(title)s.%(ext)s',
        'ignoreerrors': False,
        'writethumbnail': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            },

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

download_playlist_audio(url)


