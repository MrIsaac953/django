from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_b_-3rnwk-ng3=&cj^+!^!-z#821h$_x!1avg=w)p2e^=7v8uw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


#INSTALLED_APP=[]


ALLOWED_HOSTS = [
 '192.168.1.102',
 '127.0.0.1'
]


# sites framework
SITE_ID = 2


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT= BASE_DIR /'static'
MEDIA_ROOT= BASE_DIR /'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics"
]

X_FRAME_OPTIONS = "SAMEORIGIN"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

