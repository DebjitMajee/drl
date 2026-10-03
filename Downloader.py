import subprocess
import os
from pathlib import Path

url = input("Enter the video URL or video playlist URL: ")

output_path = str(Path.home() / "Downloads")
def download_url(url: str, output_format: str = "mp4"):
    """
    Downloads a single video or all videos in the playlist using the best video and best audio,
    merges them into a single file each, and saves them to the specified output directory.
    
    :param url: video URL or playlist URL.
    :param output_format: The final output format (default is 'mp4').
    """
    filename_template = f"{output_path}/%(title)s.%(ext)s"

    command = [
        "yt-dlp",
        "-f", "bv+ba",  # Best video + best audio
        "--merge-output-format", output_format,
        "-o", filename_template,
        "--yes-playlist",  # Ensures entire playlist is processed
        "--remux-video", output_format,
        url
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Video download completed: {url}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading video: {e}")

# Ensure output directory exists
os.makedirs(output_path, exist_ok=True)

download_url(url)
