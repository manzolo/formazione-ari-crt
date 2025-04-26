FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

#RUN python manage.py collectstatic --noinput

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000

#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "lezioni_progetto.wsgi"]
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
