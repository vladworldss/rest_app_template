all: build

build:
	docker build --target base --tag vladworldss/local-docker-hub:latest .
