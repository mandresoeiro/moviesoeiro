###########################
# core/settings/dev.py
###########################
"""
Configurações para ambiente de DESENVOLVIMENTO.
"""


from .base import *


DEBUG = True
ALLOWED_HOSTS = ["*"]


# Banco de dados SQLite para desenvolvimento
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
