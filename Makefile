.PHONY: build
build:
	faas-cli build -f functionytdlp.yml --tag latest

.PHONY: deploy
deploy:
	faas-cli deploy -f functionytdlp.yml
