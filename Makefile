.PHONY: build
build:
	poetry export -f requirements.txt -o functionytdlp/requirements.txt
	faas-cli build -f functionytdlp.yml --tag latest

.PHONY: deploy
deploy:
	faas-cli deploy -f functionytdlp.yml
