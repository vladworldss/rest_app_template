all: build

build:
	docker build --target base --tag ${USER}/rest-app-template:latest .

rm:
	docker rmi ${USER}/rest-app-template
