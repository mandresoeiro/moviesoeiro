#!/bin/bash
# 🚀 Script de Deploy da Documentação MkDocs + Git Push

echo "🔁 Ativando ambiente virtual com Poetry..."
poetry install > /dev/null 2>&1
poetry shell

echo "📦 Adicionando arquivos ao Git..."
git add .

echo "💬 Informe a mensagem de commit:"
read commit_msg
git commit -m "$commit_msg"

echo "📤 Enviando alterações para a branch main..."
git push origin main

echo "🚀 Gerando e publicando documentação MkDocs..."
poetry run mkdocs gh-deploy

echo "✅ Deploy concluído com sucesso!"