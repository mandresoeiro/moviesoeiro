# Makefile com comandos úteis para documentação

.PHONY: docs docs-serve docs-deploy

## 🛠️ Instala dependências de documentação (MkDocs)
docs:
	poetry add mkdocs mkdocs-material --group docs

## ▶️ Roda o servidor local da documentação
docs-serve:
	mkdocs serve

## 🚀 Publica a documentação no GitHub Pages
docs-deploy:
	mkdocs gh-deploy