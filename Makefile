
migrate:
	python manage.py migrate --settings=settings.local

runserver: migrate
	python manage.py runserver --settings=settings.local

makemigrations:
	python manage.py makemigrations --settings=settings.local

createsuperuser:
	python manage.py createsuperuser --settings=settings.local

tests:
	python manage.py test --settings=settings.local

test-one:
	python manage.py test $(TEST_NAME) --settings=settings.local -v 2

shellplus:
	python manage.py shell_plus --ipython --settings=settings.local

