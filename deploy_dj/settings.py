from pathlib import Path
from decouple import config

# import dj_database_url

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "whitenoise.runserver_nostatic",
    # third party packages
    "corsheaders",
    "rest_framework",
    # internal app
    "api_portfolio",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "deploy_dj.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "deploy_dj.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases zila-tech-backend-v1

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        # 'USER': 'oluku',
        # 'PASSWORD': 'Mysql@Olu1.ku',
        # 'HOST': 'oluku.mysql.pythonanywhere-services.com',
        # 'PORT': '3306',
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'oluku$mydbtest',
        # 'USER': 'oluku',
        # 'PASSWORD': 'Mysql@Olu1.ku',
        # 'HOST': 'oluku.mysql.pythonanywhere-services.com',
        # 'PORT': '3306',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': config('DB_PORTFOLIO'),
    #     'USER': config('DB_USERNAME'),
    #     'PASSWORD': config('DB_PASSWORD'),
    #     'HOST': config('DB_HOSTNAME'),
    #     # 'PORT': config('DB_PORT'),
    # }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'railway',
    #     'USER': 'postgres',
    #     'PASSWORD': 'W9V13Fx0d8qZSIFWYlmt',
    #     'HOST': 'containers-us-west-195.railway.app',
    #     'PORT': '7543',
    # }
}
# DATABASES['default'] = dj_database_url.config('DATABASE_URL')


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]



LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles_build" / "static"
STATICFILES_DIRS = [
    "deploy_dj/static",
]
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# media file configuration
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

CORS_ALLOW_ALL_ORIGINS = True
SESSION_EXPIRE_SECONDS = 3600
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
