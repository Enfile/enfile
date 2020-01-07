build:
	docker-compose down
	docker-compose build

up:
	docker-compose down
	docker-compose build
	docker-compose up -d

down:
	docker-compose down

migrate:
	docker-compose run web python manage.py makemigrations
	docker-compose run web python manage.py migrate

createuser:
	docker-compose run web python manage.py createsuperuser

logs:
	docker-compose logs -f

sh:
	docker-compose exec web sh

