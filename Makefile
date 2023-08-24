all: build

build:
	docker build --target base --tag vladworldss/local-docker-hub:latest .

rm:
	docker rmi vladworldss/local-docker-hub .
