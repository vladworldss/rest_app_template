all: build

build:
	docker build --target base --tag ${USER}/local-docker-hub:latest .

rm:
	docker rmi ${USER}/local-docker-hub
