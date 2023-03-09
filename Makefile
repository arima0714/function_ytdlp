.PHONY: init
init:
	fn init testapp/function_ytdlp
	fn build
	fn apps create function_ytdlp
	fn routes create function_ytdlp /function_ytdlp

.PHONY: build
build:
	poetry export -f requirements.txt -o requirements.txt
	fn bump
	fn build
	fn routes update function_ytdlp /function_ytdlp
