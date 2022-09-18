FROM python:3.11.0rc2-alpine3.16

WORKDIR /usr/src/

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

WORKDIR /usr/src/app

EXPOSE 8000

RUN python manage.py test

# CMD [ "python", "manage.py", "test"]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
