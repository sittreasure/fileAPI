FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8080

ENTRYPOINT [ "python","manage.py","runserver","0.0.0.0:8080" ]
# ENTRYPOINT ["pipenv","run","python","manage.py","runserver"]