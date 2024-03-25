#!/bin/bash

# instalação de dependências para o frontend
cd frontend

npm install -g @vue/cli
npm install axios

# instalação de dependências para o backend
cd ../backend
pip install Flask
pip install -U flask-cors


# executando a aplicação

# rodando servidor do frontend 
# (comando abaixo sendo executado em segundo plano)
npm run serve &

# rodando servidor backend (API)
cd ../backend
python3 app.py

