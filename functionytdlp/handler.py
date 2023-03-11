from yt_dlp import YoutubeDL

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    URLS = ["https://www.youtube.com/watch?v=BaW_jenozKc"]
    return req
    with YoutubeDL() as ydl:
        ydl.download(URLS)

