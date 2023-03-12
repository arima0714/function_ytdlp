from yt_dlp import YoutubeDL
import boto3
import botocore
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

    s3_client = boto3.client(
        "s3",
        use_ssl=False,
        endpoint_url = "http://10.1.21.85:9000",
        aws_access_key_id = os.environ['username'],
        aws_secret_access_key = os.environ['password']
    )

    URL = "https://www.youtube.com/watch?v=BaW_jenozKc"
    URLS = [URL]
    ydl_opts = {'outtmpl': './resolution'+'%(resolution)s'+'duration'+'%(duration)s'+'_.mp4'}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(URL, download=False)
        dict_informations = json.loads(json.dumps(ydl.sanitize_info(info)))
        resolution = dict_informations["resolution"]
        duration = dict_informations["duration"]

        ydl.download(URLS)

    print('botocore vertion is {0}'.format(botocore.__version__))
    print('boto3 vertion is {0}'.format(boto3.__version__))

    print(f"resolution={resolution}, duration = {duration}")
    ls_file_name = os.listdir()
    print(f"{ls_file_name = }")
    filenames = [s for s in ls_file_name if 'resolution' in s]
    filename = filenames[0]

    bucketname = "videos"
    s3_client.upload_file(f"./{filename}", bucketname, filename)

    for i_filename in filenames:
        os.remove(f"./{i_filename}")

    return req
