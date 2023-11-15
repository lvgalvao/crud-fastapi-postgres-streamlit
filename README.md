# CRUD FASTAPI POSTGRES STREAMLIT

Você sabe o que é CRUD?

[Imagem CRUD](assets/crud.jpeg)

A BlackFriday ta chegando. Você sabe como que o Iphone fica mais barato? Você sabe como que o vídeo game é cadastrado? Você sabia que quando abre o seu navegador, nada mais é do que o seu browser fazendo um SELECT no banco do Mercado Livre 🤯

Você precisa conhecer o CRUD.

O CRUD gerencia todo o fluxo de cadastro, alteração e remoção de produtos, passando por API, servidor, banco de dados e retornando ao browser. Ou seja, a maioria dos dados da sua query "SELECT * FROM" vêm de sistemas CRUD.

Há quatro ações principais:

Criação (Create) - INSERT INTO

Aqui, um produto é inserido no sistema, geralmente através de um formulário no navegador. Os dados coletados são enviados ao servidor, onde são processados e armazenados no banco de dados. Esta etapa define a estrutura e o armazenamento dos dados.

Leitura (Read) - SELECT * FROM

Após o armazenamento, visualizamos o produto no banco de dados. Realizamos consultas para extrair informações, fundamentais para apresentar os dados no navegador, como em listas de produtos ou dashboards. A eficiência nesta etapa impacta a rapidez e precisão na recuperação e exibição dos dados.

Atualização (Update) - UPDATE SET

Mudanças são realizadas através de interfaces de edição no navegador, e as alterações são atualizadas no banco de dados. Essas mudanças são então propagadas para o banco de dados, garantindo que as informações sejam atualizadas em tempo real.

Remoção (Delete) - DELETE WHERE

Esta etapa remove permanentemente dados do banco de dados, exigindo cautela, principalmente para não esquecer o WHERE.

Compreender o CRUD vai além de manipular dados; é sobre melhorar a interação com colegas de desenvolvimento.

## Instalação via docker

```bash
docker-compose up -d --build
```

### Uso

Frontend:
Acesse o endereço http://localhost:8501

### Documentação

Backend:
Acesse o endereço http://localhost:8000/docs

## Nossa estrutura de pastas e arquivos

```bash
├── README.md # arquivo com a documentação do projeto
├── backend # pasta do backend (FastAPI, SQLAlchemy, Uvicorn, Pydantic)
├── frontend # pasta do frontend (Streamlit, Requests, Pandas)
├── docker-compose.yml # arquivo de configuração do docker-compose (backend, frontend, postgres)
├── poetry.lock # arquivo de lock do poetry
└── pyproject.toml # arquivo de configuração do poetry
```

## Nosso Backend

Nosso backend vai ser uma API, que será responsável por fazer a comunicação entre o nosso frontend com o banco de dados. Vamos detalhar cada uma das pastas e arquivos do nosso backend.

### FastAPI

O FastAPI é um framework web para construir APIs com Python. Ele é baseado no Starlette, que é um framework assíncrono para construir APIs. O FastAPI é um framework que está crescendo muito, e que tem uma curva de aprendizado muito baixa, pois ele é muito parecido com o Flask.

### Uvicorn

O Uvicorn é um servidor web assíncrono, que é baseado no ASGI, que é uma especificação para servidores web assíncronos. O Uvicorn é o servidor web recomendado pelo FastAPI, e é o servidor que vamos utilizar nesse projeto.

### SQLAlchemy

O SQLAlchemy é uma biblioteca para fazer a comunicação com o banco de dados. Ele é um ORM (Object Relational Mapper), que é uma técnica de mapeamento objeto-relacional que permite fazer a comunicação com o banco de dados utilizando objetos.

Uma das principais vantagens de trabalhar com o SQLAlchemy é que ele é compatível com vários bancos de dados, como MySQL, PostgreSQL, SQLite, Oracle, Microsoft SQL Server, Firebird, Sybase e até mesmo o Microsoft Access.

Além disso, ele realiza a sanitização dos dados, evitando ataques de SQL Injection.

(imagem)[assets/sqlinjection.jpeg]

Outro ponto, é que você pode trabalhar com métodos nativos do Python, como por exemplo o filter, que é muito utilizado para fazer filtros em listas. Isso facilita muito a nossa vida, pois não precisamos aprender uma nova linguagem para fazer a comunicação com o banco de dados. Quem tiver familidade com Pandas, vai se sentir em casa.

### Pydantic

O Pydantic é uma biblioteca para fazer a validação de dados. Ele é utilizado pelo FastAPI para fazer a validação dos dados que são recebidos na API, e também para definir os tipos de dados que são retornados pela API.

## Nossa estrutura de pastas e arquivos

```bash
├── backend
│   ├── Dockerfile # arquivo de configuração do Docker
│   ├── crud.py # arquivo com as funções de CRUD utilizando o SQL Alchemy ORM
│   ├── database.py # arquivo com a configuração do banco de dados utilizando o SQL Alchemy 
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
│   ├── router.py
│   └── schemas.py
```

## Arquivo `schemas.py`

O arquivo `schemas.py` é responsável por definir os schemas do Pydantic, que são as classes que definem os tipos de dados que serão utilizados na API. Esses schemas são utilizados para fazer a validação dos dados que são recebidos na API, e também para definir os tipos de dados que são retornados pela API.

O pydantic é a principal biblioteca para validação de dados em Python. Ela é utilizada pelo FastAPI para fazer a validação dos dados recebidos na API, e também para definir os tipos de dados que são retornados pela API.

Além disso, ela possui uma integração muito boa com o SQLAlchemy, que é a biblioteca que utilizamos para fazer a comunicação com o banco de dados.

Outra vantagem são os seus tipos pré-definidos, que facilitam muito a nossa vida. Por exemplo, se você quer definir um campo que aceita apenas números positivos, você pode utilizar o PositiveInt. Se você quer definir um campo que aceita apenas determinadas categorias, você pode utilizar o construtor constrains.

### AWS ECS

Além disso, nesse projeto vamos apresentar como colocar em produção um projeto utilizando containers Docker, utilizando o AWS ECS (Amazon Elastic Container Service).

Se você quer ter toda a facilidade do Docker, garantir que o seu ambiente de desenvolvimento e de produção são idênticos, e ainda ter a possibilidade de escalar a sua aplicação, esse projeto é para você.

A AWS ECS é um serviço de orquestração de containers, que permite que você execute containers Docker de forma escalável e altamente disponível. Com ele, você não precisa se preocupar com a infraestrutura, pois a AWS cuida de tudo para você.

### AMAZON ECS

É um serviço de orquestração de containers, que permite que você execute containers Docker de forma escalável e altamente disponível. A vantagem principal é que você não precisa se preocupar com a orquestração dos containers (Kubernetes) mas tenha todas as vantagens de utilizar containers Docker.

### AMAZON ECS FARGATE

O ECS Fargate é um serviço que permite que você execute containers Docker sem precisar gerenciar servidores. Ou seja, todo o gerenciamento de servidores, balanceamento de carga, auto scaling, etc, é feito pela AWS. É um serviço ainda mais gerenciado que o ECS, pois você não precisa se preocupar com a infraestrutura.

### Conceitos

[Imagem arquitetura](assets/arquitetura.png)

#### Cluster

Um cluster é um grupo de instâncias EC2 (máquinas) que executam as suas tarefas. Ou seja, as máquinas onde os meus containers vão ser executados.

#### Task Definition

Uma task definition é um arquivo de configuração (com a formatação JSON) que define como a sua aplicação vai ser executada. Nesse arquivo você define qual imagem Docker vai ser utilizada, qual o poder computacional necessário, qual o volume que vai ser utilizado, etc.

#### Task

Uma task é uma instância de uma task definition. Ou seja, é uma execução da sua aplicação. Por exemplo, se você tem uma task definition que define que a sua aplicação vai ser executada com 2 instâncias, você terá 2 tasks executando a sua aplicação. Aplicado ao Airflow que vimos no Workshop 02, podemos subir mais de uma instância do Airflow, para garantir que a nossa aplicação vai estar sempre disponível. Além disso, podemos configurar para subir mais instâncias quando a CPU estiver alta, por exemplo.

#### Service

Um service é um grupo de tasks que são executadas juntas. Por exemplo, se você tem uma task definition que define que a sua aplicação vai ser executada com 2 instâncias, você terá 2 tasks executando a sua aplicação. Essas 2 tasks formam um service. Se alguma tarefa falhar, o service vai garantir que ela vai ser executada novamente. O service também pode ser utilizado para balancear a carga entre as tasks.

