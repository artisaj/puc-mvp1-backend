# API - Controle de Corrida de Kart (MVP)

API REST desenvolvida em Python com Flask para cadastro de pilotos, simulação de corridas de kart e consulta de histórico. O projeto foi organizado em camadas para separar rotas, controladores, regras de negócio e persistência em SQLite.

## Objetivo

Este backend foi criado como parte de um MVP de sistema web para a disciplina de Desenvolvimento Full Stack Básico. A API segue o estilo REST e disponibiliza operações para:

- cadastrar pilotos
- listar pilotos cadastrados
- consultar um piloto por identificador
- remover pilotos
- simular corridas automaticamente
- consultar o histórico de corridas

## Tecnologias

- Python 3.11+
- Flask
- SQLite
- Flasgger para Swagger UI
- Flask-Cors

## Estrutura do projeto

- `app/controllers`: tratamento da requisição e composição das respostas HTTP
- `app/models`: acesso e manipulação dos dados no SQLite
- `app/routes`: definição dos endpoints da API
- `app/services`: regras de negócio da simulação de corridas
- `app/database`: conexão com o banco e criação das tabelas
- `run.py`: ponto de entrada da aplicação

## Banco de dados

O banco utilizado é SQLite e o arquivo é criado automaticamente como `kart.db`. Atualmente a aplicação utiliza duas tabelas:

- `pilotos`: armazena os dados cadastrais dos pilotos
- `corridas`: armazena a data da corrida e o ranking gerado pela simulação

## Instalação

1. Entre na pasta do backend.
2. Crie um ambiente virtual:

```powershell
python -m venv .venv
```

3. Ative o ambiente virtual:

```powershell
.venv\Scripts\Activate.ps1
```

4. Instale as dependências:

```powershell
pip install -r requirements.txt
```

## Execução

Execução manual:

```powershell
python run.py
```

## Endereços da aplicação

- API: `http://127.0.0.1:5000`
- Healthcheck: `GET /`
- Swagger UI: `http://127.0.0.1:5000/apidocs`

## Rotas da API

- `POST /api/pilotos`: cadastra um novo piloto
- `GET /api/pilotos`: lista todos os pilotos
- `GET /api/pilotos/{id}`: busca um piloto por id
- `DELETE /api/pilotos/{id}`: remove um piloto por id
- `POST /api/corridas/simular`: executa uma simulação de corrida e salva o resultado
- `GET /api/corridas`: lista o histórico de corridas simuladas

## Documentação Swagger

A documentação interativa da API está disponível em `/apidocs`. Nela é possível visualizar:

- descrição de cada endpoint
- método HTTP utilizado
- estrutura de requisição
- estrutura de resposta
- códigos de status esperados

## Observações

- A simulação de corrida exige pelo menos dois pilotos cadastrados.
- O resultado da corrida é gerado automaticamente com tempos aleatórios e ordenação por ranking.
