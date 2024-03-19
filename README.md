# Anvisa Meds

## Instruções

### Backend
Na raiz do projeto, siga as instruções abaixo:

    cd api
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Crie um banco de dados chamado anvisa_meds e realize as configurações do banco de dados no arquivo api/settings.py

Caso queira inserir os registros manualmente (__ISSO LEVARÁ MAIS TEMPO__), execute o comando abaixo:

    python manage.py migrate

Para inserir os registros através do dump execute o comando abaixo:

    psql anvisa_meds < data/database.sql

Agora basta subir o servidor:

    python manage.py runserver

O servidor rodará na porta 8000.

endpoints disponíveis:

Para consultar os dados: /api/meds

Para inserir os registros manualmente: /resources/pmvg-data/insert/


### Frontend

Na raiz do projeto, siga as instruções abaixo:

    cd vue-app
    npm install
    npm run dev

O servidor irá rodar na porta 9090.

### Executando o projeto

Basta abrir o navegador na url: http://localhost:9090

    