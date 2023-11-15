# CRUD FASTAPI POSTGRES STREAMLIT

## Objetivo

Esse projeto tem dois objetivos:

### CRUD

O primeiro objetivo é um complemento do Workshop 02 de deploy criando um CRUD com FastAPI, Postgres e Streamlit.

Vamos criar um sistema de cadastro de produtos, com as operações de CRUD (Create, Read, Update e Delete), utilizando a API desenvolvida no Workshop 02, e criar uma interface para consumir essa API utilizando o Streamlit.

### AWS ECS

Além disso, nesse projeto vamos apresentar como colocar em produção um projeto utilizando containers Docker, utilizando o AWS ECS (Amazon Elastic Container Service).

Se você quer ter toda a facilidade do Docker, garantir que o seu ambiente de desenvolvimento e de produção são idênticos, e ainda ter a possibilidade de escalar a sua aplicação, esse projeto é para você.

A AWS ECS é um serviço de orquestração de containers, que permite que você execute containers Docker de forma escalável e altamente disponível. Com ele, você não precisa se preocupar com a infraestrutura, pois a AWS cuida de tudo para você.

## Instalação via docker

```bash
docker-compose up -d --build
```

## Uso

Frontend:
Acesse o endereço http://localhost:8501

## Documentação

Backend:
Acesse o endereço http://localhost:8000/docs

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

