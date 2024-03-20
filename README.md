# Anvisa Meds
![version](https://img.shields.io/badge/Version-v1.2.4-green)
![License](https://img.shields.io/badge/License-MIT-blue)
![vue](https://img.shields.io/badge/Vue.js-blue)
![django](https://img.shields.io/badge/Django-blue)

Página web para visualizar a lista de medicamentos da planilha [PMVG.xls](https://www.gov.br/anvisa/pt-br/assuntos/medicamentos/cmed/precos).
Através da aplicação é possível filtrar por Substância, Laboratório e Cnpj.

![App](https://github.com/josafaverissimo/anvisa-meds/assets/50150682/a1b67f4e-d7b3-4726-beb2-b1fa0b004e62)


## Instruções
É possível implantar a aplicação manualmente ou com docker. Basta seguir os passos mostrados abaixo.

### Docker
Na raiz do projeto execute o comando:

    docker compose up --build

O comando acima também já cria o banco de dados e insere os dados contidos no
arquivo /api/data/database.sql.

### Implantação manual
#### Backend
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


#### Frontend

Na raiz do projeto, siga as instruções abaixo:

    cd vue-app
    npm install
    npm run dev

O servidor irá rodar na porta 9090.

### Executando o projeto

Basta abrir o navegador na url: http://localhost:9090

## Endpoints

### GET api/meds
#### ?med_substance=str&laboratory_name=str&laboratory_cnpj&term=str

Este endpoint permite realizar buscas nas colunas de substância, nome do laboratório e cnpj.
Também é possível realizar uma busca por similaridade em todas as colunas citadas 
através do parâmetro __*term*__ da query string.

### POST api/resources/pmvg-data/insert

Este endpoint serve para atualizar o banco de dados. Para fazer isto basta baixar a planilha
[PMVG.xls](https://www.gov.br/anvisa/pt-br/assuntos/medicamentos/cmed/precos) e coloca-la no diretório
api/data nomeada como pmvg.xls e acessar a url: http://localhost:9090/resources/pmvg-data/insert. Esse
processo pode levar um bom tempo para ser finalizado.
