# 🎬 moviesoeiro

**Controle de Filmes Profissional com Django + Poetry + MkDocs**

---

## 🚀 Sobre o Projeto

Sistema completo para cadastro e visualização de filmes com suporte a:

- ✅ Categorias e Atores
- ✅ Upload de fotos por mês/ano
- ✅ Slug para URLs amigáveis
- ✅ Integração com Django Admin
- ✅ API pronta para DRF (em progresso)
- ✅ Documentação com MkDocs e GitHub Pages

---

## 🧱 Tecnologias

- Python 3.11+
- Django
- Poetry
- MkDocs com tema Material
- Docker (em breve)

---

## 🛠️ Setup do Projeto

```bash
git clone https://github.com/SEU_USUARIO/moviesoeiro.git
cd moviesoeiro
poetry install
cp .env.example .env
poetry run python manage.py migrate
poetry run python manage.py createsuperuser
poetry run python manage.py runserver
```

---

## 📚 Documentação

Documentação local:

```bash
make docs-serve
```

Deploy online:

```bash
make docs-deploy
```

Acesse: [https://SEU_USUARIO.github.io/moviesoeiro](https://SEU_USUARIO.github.io/moviesoeiro)

---

## 🤝 Contribuições

Sinta-se livre para abrir *issues* e *pull requests*. Este projeto segue os padrões do **DevilLint™** para qualidade de código e documentação.

---

> Desenvolvido por [mandresoeiro](https://github.com/mandresoeiro) com ❤️ e Django.