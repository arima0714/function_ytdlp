.PHONY: init
init:
	fn init testapp/function_ytdlp
	fn build
	fn apps create function_ytdlp
	fn routes create function_ytdlp /function_ytdlp

.PHONY: build
build:
	fn bump
	fn build
	fn routes update function_ytdlp /function_ytdlp
