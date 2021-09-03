FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/chaejinims2/djangoProject2.git

WORKDIR /home/djangoProject2

RUN echo "SECRET_KEY=django-insecure-m_%apm8v8g@$6%bda3g#*kk2&^5br1y9d@283b4)$!y09p4&js"

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]