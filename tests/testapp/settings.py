"""Django settings for test project."""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-django-tasks-pgmq-test-secret-key"  # noqa: S105

DEBUG = True

ALLOWED_HOSTS = ["localhost"]

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django_tasks_pgmq",
    "tests",
]

ROOT_URLCONF = "tests.testapp.urls"

WSGI_APPLICATION = "tests.testapp.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("PGDATABASE", "postgres"),
        "USER": os.environ.get("PGUSER", "postgres"),
        "PASSWORD": os.environ.get("PGPASSWORD", "postgres"),
        "HOST": os.environ.get("PGHOST", "localhost"),
        "PORT": os.environ.get("PGPORT", "5432"),
    }
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TASKS = {
    "default": {
        "BACKEND": "django_tasks_pgmq.PGMQBackend",
        "QUEUES": ["default"],
    },
}
