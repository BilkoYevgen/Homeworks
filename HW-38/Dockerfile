FROM python:3.11

WORKDIR /app

COPY requeirements.txt .

RUN pip install -r requeirements.txt

COPY . .

RUN python manage.py migrate

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000