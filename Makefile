
run_makemigrations:
	@echo "Making Migration files"
	docker-compose run --rm app python manage.py makemigrations

run_migrations:
	@echo "Running Migrations Docker"
	docker-compose run --rm app python manage.py migrate

run_flake8:
	@echo "Running flake8"
	docker-compose run --rm app flake8
