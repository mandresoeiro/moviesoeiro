"""
Configurações para ambiente de DESENVOLVIMENTO.
"""

from .base import *  # Importa todas as configurações base

# -----------------------------------------------------------------------------
# Segurança
# -----------------------------------------------------------------------------
DEBUG = True
ALLOWED_HOSTS = ["*"]  # Permite acesso de qualquer host em dev

# -----------------------------------------------------------------------------
# Banco de dados local (SQLite)
# -----------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
