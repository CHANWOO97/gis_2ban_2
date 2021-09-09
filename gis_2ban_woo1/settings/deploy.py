from .base import *

env_list = dict()

local_env = open(os.path.join(BASE_DIR, '.env'))

while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\n', '')
    start = line.find('=')
    key = line[:start]
    value = line[start+1:]
    env_list[key] = value

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env_list['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # mysql에서 분화되서 나온것이 maria DB
        'NAME': 'django',
        'USER': 'django-woo',
        'PASSWORD': 'mypassword1234',
        'HOST': 'mariadb', # container name을 도메인으로 받아들이도록 설정했기 때문에~
        'PORT': '3306',
    }
}