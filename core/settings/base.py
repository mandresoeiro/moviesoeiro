###########################
# core/settings/base.py
###########################
"""
Configurações base do Django para o projeto.
Usado como base para dev.py e prod.py.
"""


from pathlib import Path
from decouple import config


# Diretório base do projeto (3 níveis acima)
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# -----------------------------------------------------------------------------
# Segurança
# -----------------------------------------------------------------------------
SECRET_KEY = config("SECRET_KEY", default="unsafe-secret-key")
DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1,localhost").split(",")


# -----------------------------------------------------------------------------
# Apps instalados
# -----------------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Apps locais
    "movies",
]


# -----------------------------------------------------------------------------
# Middlewares
# -----------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# -----------------------------------------------------------------------------
# URLs e WSGI
# -----------------------------------------------------------------------------
ROOT_URLCONF = "core.urls"
WSGI_APPLICATION = "core.wsgi.application"


# -----------------------------------------------------------------------------
# Internacionalização
# -----------------------------------------------------------------------------
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True


# -----------------------------------------------------------------------------
# Arquivos estáticos
# -----------------------------------------------------------------------------
STATIC_URL = "static/"
