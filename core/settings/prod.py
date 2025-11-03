###########################
# core/settings/prod.py
###########################
"""
Configurações para ambiente de PRODUÇÃO.
Nunca use DEBUG=True aqui.
"""


from .base import *


DEBUG = False


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("POSTGRES_HOST", default="localhost"),
        "PORT": config("POSTGRES_PORT", default="5432"),
    }
}
