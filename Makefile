hello:
	echo "hello world"

.PHONY: help build push all

help:
	@echo "Makefile commands:"
	@echo "build"
	@echo "up"
	@echo "ssh"
	@echo "server"
	@echo "down"
	@echo "flake8"
	@echo "test"


build:
	docker-compose build --no-cache
	docker-compose run -d

up:
	docker-compose up -d

ssh:
	docker exec -it blogapp bash

server:
	python manage.py runserver

down:
	docker stop blogapp

flake8:
	flake8

test:
	python manage.py test