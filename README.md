# function_ytdlp

# 環境構築

```
docker run --rm -it --name functions -v ${PWD}/data:/app/data -v /var/run/docker.sock:/var/run/docker.sock -p 8080:8000 iron/functions
docker run --rm -it --link functions:api -p 4000:4000 -e "API_URL=http://api:8000" iron/functions-ui:0.0.2
```

# ビルドコマンドの導入

```
brew install iron-functions
```

# ビルド

```
fn init testapp/function_ytdlp
fn build
fn apps create function_ytdlp
fn routes create function_ytdlp /function_ytdlp
```
