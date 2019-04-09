FROM python:3.7

WORKDIR /app

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip && pip install pipenv
ADD . /app

RUN pipenv install

RUN pipenv install --deploy --system

EXPOSE 8000

ENTRYPOINT [ "uwsgi", "--ini", "fileAPI.ini" ]
# ENTRYPOINT ["pipenv","run","python","manage.py","runserver"]