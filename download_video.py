from pytube import *
from pytube.exceptions import RegexMatchError

def download_video(link):
    try:
        yt = YouTube(link)
    except RegexMatchError:
        return False
    else:
        streams = yt.streams.filter(progressive=True)
        itag = streams[0].itag
        stream = yt.streams.get_highest_resolution()
        stream.download("./videos")
        return True
