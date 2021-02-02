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
	docker-compose build
	docker-compose up -d

up:
	docker-compose up -d

ssh:
	docker exec -it blogapp bash

server:
	docker exec -it blogapp python manage.py runserver

down:
	docker stop blogapp

flake8:
	docker exec -it blogapp flake8

test:
	docker exec -it blogapp python manage.py test