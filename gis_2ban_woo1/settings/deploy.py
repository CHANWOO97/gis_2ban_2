from .base import *

def read_secrets(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()  # 왼쪽 오른 쪽 공백 지우기
    file.close()
    return secret

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = read_secrets('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # mysql에서 분화되서 나온것이 maria DB
        'NAME': 'django',
        'USER': read_secrets('MARIADB_USER'),
        'PASSWORD': read_secrets('MARIADB_PASSWORD'),
        'HOST': 'mariadb', # container name을 도메인으로 받아들이도록 설정했기 때문에~
        'PORT': '3306',
    }
}