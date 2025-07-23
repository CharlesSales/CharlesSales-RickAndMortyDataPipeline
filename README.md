# RickAndMortyDataPipeline

Este projeto implementa um pipeline de Engenharia de Dados para extrair, transformar e carregar dados da API pública do universo Rick and Morty. Ele coleta informações sobre personagens, episódios e localizações, transforma os dados em formatos estruturados e os armazena em diferentes formatos (Parquet, CSV, JSON e banco de dados).

---

## 📊 Funcionalidades

- 🔁 Extração paginada de dados da API Rick and Morty
- 🔄 Transformação e limpeza dos dados brutos
- 💾 Armazenamento em formatos: CSV, Parquet, JSON
- 🗄️ Salvamento em banco de dados (SQLite ou outro)
- 🧱 Estrutura modular seguindo o padrão ETL

---

## 🗂️ Estrutura do Projeto

rick-and-morty-etl/

├── data/

| ├── raw/ # Dados brutos em JSON

| ├── export/ # Dados tratados em csv

| └── processed/ # Dados tratados em Parquet

├── extract/ # Scripts de extração da API

├── transform/ # Scripts de transformação

├── load/ # Scripts para salvar os dados

├── pipeline/ # Script principal para orquestração

├── .env

└── README.md


---

🛠️ Tecnologias utilizadas
Python

Requests

Pandas

Dotenv

PyArrow

PostgreSQL

📌 Autor
Charles Henrique 
LinkedIn • GitHub
