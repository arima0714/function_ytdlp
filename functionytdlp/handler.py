from yt_dlp import YoutubeDL
import boto3
import os
import json

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    s3 = boto3.resource(
        's3',
        endpoint_url = "http://10.1.21.85:9000",
        aws_access_key_id = os.environ['username'],
        aws_secret_access_key = os.environ['password']
    )

    print("all buckets")
    for bucket in s3.buckets.all():
        print(bucket.name)

    URL = "https://www.youtube.com/watch?v=BaW_jenozKc"
    URLS = [URL]
    with YoutubeDL() as ydl:
        info = ydl.extract_info(URL, download=False)
        print(json.loads(json.dumps(ydl.sanitize_info(info)))["title"])
        ydl.download(URLS)

    return req
