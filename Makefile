build:
	docker-compose down
	docker-compose build

up:
	docker-compose down
	docker-compose build
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

sh:
	docker-compose exec web sh

