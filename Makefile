.PHONY: docs docs-serve docs-deploy git-init git-update

## 🛠️ Instala dependências de documentação (MkDocs)
docs:
	poetry add mkdocs mkdocs-material --group docs

## ▶️ Roda o servidor local da documentação
docs-serve:
	mkdocs serve

## 🚀 Publica a documentação no GitHub Pages
docs-deploy:
	mkdocs gh-deploy

## 🆕 Inicializa o repositório Git local e conecta ao GitHub
git-init:
	git init
	git branch -M main
	git remote add origin https://github.com/mandresoeiro/moviesoeiro.git
	git add .
	git commit -m "feat: projeto inicial com Cookiecutter DevilLint"
	git push -u origin main

## 🔁 Atualiza o repositório com as últimas alterações
git-update:
	git add .
	git commit -m "chore: atualizações no projeto"
	git push
