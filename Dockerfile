FROM python:3.6.3-stretch

ADD . /home
WORKDIR /home
RUN pip install -r requirements.txt && \
    python manage.py init_db

CMD ["python", "manage.py", "runserver", "--host", "0.0.0.0"]
