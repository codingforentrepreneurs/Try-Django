FROM python:3.11

RUN apt update -y && apt upgrade -y && apt install -y sqlite3 && pip install pipenv && mkdir /django-app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /django-app
COPY . /django-app/
RUN pip install --upgrade pip
RUN pipenv sync --system
RUN python src/manage.py migrate
EXPOSE 8000
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
