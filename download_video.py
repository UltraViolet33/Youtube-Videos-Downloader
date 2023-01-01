from pytube import *
from pytube.exceptions import RegexMatchError
import os
from moviepy.editor import *


def download_video(link, file_type):
    try:
        yt = YouTube(link)
    except RegexMatchError:
        return False
    else:
        if file_type == "video":
            stream = yt.streams.get_highest_resolution()
            stream.download("./videos")
            return True
        elif file_type == "audio":
            yt = YouTube(link, on_complete_callback=MP4toMP3())
            stream = yt.streams.get_audio_only()
            stream.download("./audios")
            return True


def MP4toMP3():
    mp4_files = os.listdir("./audios")
    for file in mp4_files:
        mp3_filename = file.split("mp4")[0] + "mp3"
        filename = f"audios/{file}"
        file_to_convert = AudioFileClip(filename)
        mp3_path = f"mp3/{mp3_filename}"
        file_to_convert.write_audiofile(mp3_path)
        file_to_convert.close()


def delete_mp4_audio_files():
    mp4_files = os.listdir("./audios")
    for file in mp4_files:
        os.remove(f"audios/{file}")
