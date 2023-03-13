.PHONY: all
all:
	make export_requirements
	faas-cli up -f functionytdlp.yml --no-cache --env write_debug=true

.PHONY: build
build:
	make export_requirements
	faas-cli build -f functionytdlp.yml --tag latest

.PHONY: deploy
deploy:
	faas-cli deploy -f functionytdlp.yml

.PHONY: export_requirements
export_requirements:
	poetry export -f requirements.txt -o functionytdlp/requirements.txt
