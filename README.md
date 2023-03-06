# function_ytdlp

# 環境構築

```
docker run --rm -it --name functions -v ${PWD}/data:/app/data -v /var/run/docker.sock:/var/run/docker.sock -p 8080:8080 iron/functions
docker run --rm -it --link functions:api -p 4000:4000 -e "API_URL=http://api:8080" iron/functions-ui:0.0.2
```

# ビルドコマンドの導入

```
curl -LSs git.io/ironfn | sh
```

# ビルド

初回
```
make init
```

2回目以降
```
make build
```
