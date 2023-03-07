FROM iron/python:3-dev

WORKDIR /app
COPY . /app

ENTRYPOINT ["python3", "function_ytdlp.py"]
