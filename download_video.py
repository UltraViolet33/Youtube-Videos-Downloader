from pytube import *
from pytube.exceptions import RegexMatchError

def download_video(link, file_type):
    try:
        yt = YouTube(link)
    except RegexMatchError:
        return False
    else:
        if file_type == "video":
            
            streams = yt.streams.filter(progressive=True)
            itag = streams[0].itag
            stream = yt.streams.get_highest_resolution()
            stream.download("./videos")
            return True
        elif file_type == "audio":
            stream = yt.streams.get_audio_only()
            print(stream)
            stream.download("./audios")
            return True