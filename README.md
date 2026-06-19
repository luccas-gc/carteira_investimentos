# Carteira de Investimentos API

API desenvolvida em Python para gerenciar uma carteira de investimentos, permitindo o cadastro de ativos e o registro de aportes.

O projeto foi criado com o objetivo de praticar conceitos de desenvolvimento backend utilizando Python, FastAPI, SQLAlchemy Assíncrono e modelagem de banco de dados.

## Tecnologias Utilizadas

* Python 3
* FastAPI
* SQLAlchemy Async
* Pydantic
* SQLite (atualmente)
* Uvicorn

## Funcionalidades e Rotas
### Ativos

* POST: /ativo -> **Cadastrar um novo ativo**
* GET: /ativo -> **Consultar todos os ativos cadastrados**
* GET: /ativo/{codigo} -> **Consultar um ativo pelo código**

### Aportes
* POST: /aporte/criar_aporte -> **Registrar aportes em ativos existentes e atualiza automaticamente a quantidade daquele ativo**
* GET: /aporte/ -> **Consultar todo o histórico de aportes**
* GET: /aporte/{codigo} -> **Consultar o histórico de aportes de um ativo específico**

### Exemplo de Ativo JSON
```bash
{
    "nome": "PETROBRAS",
    "tipo": "AÇÃO",
    "codigo": "PETR4",
    "valor_unitario": 49.65,
    "quantidade": 10
}
```

## Estrutura do Projeto
```text
src/
├── database/
│   └── databaseConfig.py
├── models/
│   ├── ativo.py
│   └── aporte.py
├── schemas/
│   ├── ativo_schema.py
│   └── aporte_request_schema.py
├── services/
│   ├── ativo_service.py
│   └── aporte_service.py
└── routes/
```

## Executando o Projeto

Clone o repositório:

```bash
git clone https://github.com/luccas-gc/carteira_investimentos.git
```

Acesse a pasta:

```bash
cd carteira_investimentos
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
uvicorn src.main:app --reload
```

## Documentação da API

Após iniciar a aplicação, a documentação interativa estará disponível em seu localhost, exemplo:

```text
http://localhost:8000/docs
```

## Aprendizado

Com esse projeto, foi possível adquirir conhecimentos em:

* Desenvolvimento de APIs REST
* Programação assíncrona em Python
* SQLAlchemy ORM
* Relacionamentos entre tabelas
* Organização de projetos backend
* Boas práticas de arquitetura em APIs

## Possíveis Melhorias Futuras

* Autenticação de usuários
* Integração com banco PostgreSQL no lugar de SQLite
* Atualização de preços reais dos ativos
* Cálculo de patrimônio da carteira