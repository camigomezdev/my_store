
migrate:
	python manage.py migrate --settings=settings.local

runserver: migrate
	python manage.py runserver --settings=settings.local

makemigrations:
	python manage.py makemigrations --settings=settings.local
