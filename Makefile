build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down --remove-orphans

test:
	py -3.9 -m pytest tests