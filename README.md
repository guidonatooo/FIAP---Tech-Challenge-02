# 📊 Tech Challenge 2 – Pipeline de Dados da B3 (FIAP) ##

Este projeto tem como objetivo construir um pipeline de dados **100% serverless na AWS**, realizando a extração, transformação, catalogação e análise dos dados de pregão da B3 (Bolsa de Valores Brasileira), conforme os requisitos do **Tech Challenge 02 da FIAP**.

## 🎯 Objetivo

Automatizar a coleta e o processamento dos dados de negociação da B3, aplicando boas práticas de arquitetura em nuvem, engenharia de dados e serviços AWS como S3, Lambda, Glue e Athena.

---

## 📌 Arquitetura Implementada

![Diagrama do Pipeline](https://i.postimg.cc/rstjXL9K/Capturar.jpg)

### 🔄 Fluxo de Dados

1. **🧾 Extração (Site B3)**
   - Scripts em Python executados via **AWS Cloud9** com `Selenium` para capturar os arquivos de pregão.
   - Conversão do CSV original para **formato Parquet**, com particionamento por data.

2. **☁️ Armazenamento (Amazon S3)**
   - Arquivos brutos salvos na pasta `raw/` do bucket.
   - Após o upload, um evento no S3 aciona automaticamente uma função Lambda.

3. **⚙️ Processamento (AWS Lambda + Glue Studio)**
   - A **Lambda** inicia um **Job visual no AWS Glue Studio**.
   - O Glue lê os dados via **Glue Data Catalog**, realiza:
     - Renomeação de colunas
     - Cálculo de campos de data
     - Agregações por tipo de ativo
   - Dados finais salvos nas pastas `refined/` e `aggregated/`.

4. **🔍 Análise (Glue Catalog + Athena)**
   - Os dados são catalogados automaticamente pelo **Glue Crawler**.
   - Disponibilizados para consulta via **Amazon Athena**, usando SQL.

---

## 🧪 Tecnologias Utilizadas

- **Linguagem:** Python 3.9+
- **Bibliotecas:** `selenium`, `pandas`, `pyarrow`, `boto3`
- **Serviços AWS:**
  - Amazon S3 (Data Lake)
  - AWS Cloud9 (ambiente de desenvolvimento)
  - AWS Lambda (orquestração)
  - AWS Glue Studio (ETL visual)
  - AWS Glue Crawler & Data Catalog
  - Amazon Athena (análise SQL)

---

## 🗂️ Estrutura do Projeto

```bash
FIAP---Tech-challenge-02/
├── README.md
├── fiap-tech-challenge-2/
│   ├── __pycache__
│   ├── downloads_b3
│   |    └── IBOVDia_25-07-25.csv
│   ├── output/data=25-07-25
│   |    └── conversao_parquet
│   |    └── pregao.parquet
│   ├── conversao_parquet.py
│   ├── diagnostico.py
|   ├── diagrama.jpg
│   ├── scraper_b3.py
└── └── send_aws.py

