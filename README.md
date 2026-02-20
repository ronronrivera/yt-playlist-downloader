# ▶ YouTube Playlist Downloader (CLI)

> Tired of YouTube downloader ads and sketchy websites?  
> Use this script directly inside your terminal — fast, clean, and ad‑free.

A simple command-line YouTube playlist downloader built with **Python** and `yt-dlp`.  
Download full playlists in **MP4 (video)** or extract **MP3 (audio)** with embedded thumbnails and metadata.

---

## ◆ Features

• Download entire YouTube playlists  
• Extract high-quality MP3 audio  
• Download best quality video (merged to MP4)  
• Automatically embed YouTube thumbnail as cover art  
• Write proper metadata (title, uploader, etc.)  
• Organize files into playlist folders  
• No ads. No browser extensions. No sketchy websites.  

---

## ◆ Requirements

• Python 3.9+  
• yt-dlp  
• ffmpeg  

---

## ◆ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ronronrivera/yt-playlist-downloader/
cd yt-playlist-downloader
```
### 2. Create a virtual environment (recommended)

```bash
Linux / macOS

python3 -m venv venv
source venv/bin/activate   

Windows:
venv\Scripts\activate
```
### 3. Install yt-dlp

```bash
pip install yt-dlp
```
### 4. Install FFmpeg

```bash
Arch Linux:

sudo pacman -S ffmpeg

Ubuntu / Debian:

sudo apt install ffmpeg

macOS:

brew install ffmpeg

Windows:
Download from https://ffmpeg.org/download.html

Add it to your system PATH.

Verify installation:

ffmpeg -version
```

◆ Usage
Download Playlist as Video (MP4)
python downloader.py <playlist_url>

Example:

python downloader.py https://www.youtube.com/playlist?list=XXXXXXXX
Download Playlist as MP3 (Audio Only)
python downloader_mp3.py <playlist_url>
◆ Output Location

All files are automatically organized into playlist folders.

Video Output:

Saved to:

~/Videos/<Playlist Name>/

Example:

/home/yourusername/Videos/Mix - Music of Japan/


