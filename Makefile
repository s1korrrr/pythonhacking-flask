init:
	pip install -r requirements.txt
	python manage.py init_db

reset-db:
	python manage.py drop_db
	python manage.py init_db

run:
	python manage.py runserver

