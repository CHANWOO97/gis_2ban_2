FROM python:3.9.0

WORKDIR /home/

RUN echo "asdcxaef"

RUN git clone https://github.com/CHANWOO97/gis_2ban_2.git

WORKDIR /home/gis_2ban_2/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=gis_2ban_woo1.settings.deploy && python manage.py migrate --settings=gis_2ban_woo1.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=gis_2ban_woo1.settings.deploy gis_2ban_woo1.wsgi --bind 0.0.0.0:8000"]

