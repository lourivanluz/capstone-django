# Bug Tracker API

Um serviço Back-End que visa cobrir as necessidades de armazenamento de dados
para uma aplicação de rastreamento de bugs. Tem como objetivo agilizar o processo
de desenvolvimento por facilitar o registro e acompanhamento de erros encontrados
em produção, recursos necessários para a garantia de qualidade de qualquer projeto.

## Funcionalidades Principais

- Listagem de usuários;
  -unica função que é possivel realizar sem estar logado na api, faz uma busca e retorna todos os usuários registrados, com seu email, nome e id, exemplo de retorno:
  	{
		  "id": "f3546313-80c3-413a-9e14-fddf23fc426d",
		  "username": "kenzinho",
		  "email": "kenzinho@hothot.com"
	  }
- Cadastro de usuários;
  - Usuários são cadastrados no banco de dados apenas com seus dados pessoais. Seus projetos e tickets são registrados em processos futuros.
  -para realizar o cadastro é necessario um post:
    {
	    "username": "User Teste",
	    "email": "teste@user.com",
	    "password": "123456"
    }
- Login de usuários
  -login é necessario para acessar e realizar buscas dentro da api
  -para logar é necessario um post:
    {
	    "email": "daniel_mp18@outlook.com",
	    "password": "123456"
    }

- Listagem de projetos que o Usuário logado.
  - mostra uma lista de projetos, apenas os que o usuário logado está constando como participante de fato.
- Criação de projetos:
  - Ao criar um projeto, o usuário é automaticamente cadastrado como participante do mesmo.
  - Exemplo de criação de um projeto:
    {
	    "title": "Projeto Novo",
	    "description": "Um novo projeto"
    }
  - ele retorna o ID do projeto, o titulo, a descrição e também a lista de usuarios deste projeto, que deve ser apenas a pessoa que criou o projeto, exemplo de retorno:
  {
	  "id": "458bd15b-4ccb-4cf0-a767-15242b11c292",
	  "title": "Projeto Novo",
	  "description": "Um novo projeto",
	  "users": [
		  {
			  "id": "f08d8b53-da3f-46c1-8f1e-aaec5ff282fe",
			  "username": "Lourivan Rodrigues",
			  "email": "lourivan-rodrigues@hotmail.com"
		  }
	]
}
- Adição de usuários à projetos:
  - Qualquer usuário no projeto pode adicionar novos usuários.
  - Para adicionar um novo usuário ao projeto é preciso passar o id do projeto na url exemplo
    "api/projects/project_id/"
    substituindo o "project_id" pelo id do projeto.
  - Exemplo de adição de usuário ao projeto:
    {
	    "email": "outro@user.com"
    }
  - O Retorno é do projeto, e seus participantes, exemplo:
    {
	    "id": "458bd15b-4ccb-4cf0-a767-15242b11c292",
	    "title": "Projeto Novo",
	    "description": "Um novo projeto",
	  "users": [
		  {
			  "id": "3934544f-652a-4101-b43e-a05563141853",
			  "username": "Ivan Rowlands de Macedo",
			  "email": "ivan.rowlands.macedo@gmail.com"
		  },
		  {
			  "id": "f08d8b53-da3f-46c1-8f1e-aaec5ff282fe",
			  "username": "Lourivan Rodrigues",
			  "email": "lourivan-rodrigues@hotmail.com"
		  }
	  ]
    }

- Lista de tickets de um projeto
  - Para realizar esta busca é necessario alterar na url colocando o ID do projeto para ter acesso a todos os tickets deste, e para ter acesso a esses tickets você precisa estar logado e fazer parte do projeto, exemplo de url:
  "api/projects/project_id/tickets/" baste alterar onde está project_id para o ID do projeto e receberá a lista de tickets deste.
- Criação de tickets:
  - Qualquer usuário no projeto pode criar tickets;
  - Tickets possuem várias informações importantes, como grau de severidade do erro, passos para a reprodução e a frequência em que ocorre, Exemplo de criação de um ticket:
  {
	  "description": "Problema com alguma coisa",
	  "test_steps": "Fazer assim e assado",
	  "severity": "low",
	  "status": "reported",
	  "category":"flaw",
	  "frequency":"constant"
  }
  assim como na requisição de lista, aqui precisa ser alterada a url "api/projects/project_id/tickets/", e onde está "project_id" você coloca o id do projeto
  Para a criação dos tickets alguns status têm alguns parametros com palavras chaves

  SEVERITY = "low", moderate, critical
  CATEGORY = flaw, improvement, suggestion
  FREQUENCY = constant, periodic, irreproducible
  STATUS_CHOICES = reported, irrelevant, admitted, assignet, done, returned, resolved

  -Retorno da criação de ticket será o id do ticket constando o criador do ticket, com id, nome e email, e o proprio ticket com categoria, como reproduzir o erro, qual o nivel de preocupação com ele, o status, a categoria a frequencia, deadline para resolver que por padrão vem nulo, e quem pegou para resolver esse bug, exemplo deste retorno:
    {
      "id": "1685f3fe-3fa4-4647-80f9-c1f16b9ef41a",
      "author": {
        "id": "f08d8b53-da3f-46c1-8f1e-aaec5ff282fe",
        "username": "Lourivan Rodrigues",
        "email": "lourivan-rodrigues@hotmail.com"
    },
      "category": "flaw",
      "description": "Problema,
      "test_steps": "fazendo assim e assim",
      "severity": "low",
      "frequency": "constant",
      "status": "reported",
      "deadline": null,
      "assigned": []
  }
- Adição de usuários à tickets:
  - Qualquer usuário no projeto pode adicionar colegas de projeto à um ticket;
  - Vários usuários podem ser designados ao mesmo ticket. Para adicionar um usuário a um ticket é necessario alteração de url, api/projects/project_id/tickets/ticket_id/ , onde está "project_id" troca para o ID do projeto e onde está "ticket_id" coloca o id do ticket em questão, exemplo de requisção:
    {
      "email": "ivan.rowlands.macedo@gmail.com"
    }
  exemplo de retorno:
    {
      "id": "1685f3fe-3fa4-4647-80f9-c1f16b9ef41a",
      "author": {
        "id": "f08d8b53-da3f-46c1-8f1e-aaec5ff282fe",
        "username": "Lourivan Rodrigues",
        "email": "lourivan-rodrigues@hotmail.com"
    },
      "category": "flaw",
      "description": "Problema",
      "test_steps": "fazendo assim e assim",
      "severity": "low",
      "frequency": "constant",
      "status": "reported",
      "deadline": null,
      "assigned": [
      {
        "id": "3934544f-652a-4101-b43e-a05563141853",
        "username": "Ivan Rowlands de Macedo",
        "email": "ivan.rowlands.macedo@gmail.com"
      }
    ]
    }
- Alteração de status de tickets:
  - Apenas usários designados à um ticket podem alterar seu status e demais informações, assim como a adição de usuário ao ticket, aqui precisará de uma alteração de url api/projects/project_id/tickets/ticket_id/, onde está "project_id" colocando o id do projeto e onde está "ticket_id" colocando o id do ticket, exemplo de requisição:
    {
      "status": "admitted"
    }
  exemplo de retorno:
  {
	"id": "1685f3fe-3fa4-4647-80f9-c1f16b9ef41a",
	"author": {
		"id": "f08d8b53-da3f-46c1-8f1e-aaec5ff282fe",
		"username": "Lourivan Rodrigues",
		"email": "lourivan-rodrigues@hotmail.com"
	},
	"category": "flaw",
	"description": "Problema",
	"test_steps": "fazendo assim e assim",
	"severity": "low",
	"frequency": "constant",
	"status": "admitted",
	"deadline": null,
	"assigned": [
		{
			"id": "3934544f-652a-4101-b43e-a05563141853",
			"username": "Ivan Rowlands de Macedo",
			"email": "ivan.rowlands.macedo@gmail.com"
		}
	]
}
- Adição de comentários à tickets:
  - Qualquer usuário no projeto pode adicionar comentários à um ticket, para realizar o comentario é necessario alteração na url da requisição api/projects/project_id/tickets/ticket_id/comments onde temos "project_id" é necessario colocar o id do projeto e onde está "ticket_id" o id do ticket em questão, exemplo de requisição:
    {
      "content": "Esse problema é um problemão"
    }
- Listagem de comentários:
  - Qualquer usuário no projeto pode adicionar comentários à um ticket, para ter acesso a lista de comentarios você precisa além de estar logado fazer alteração na url da requisição api/projects/project_id/tickets/ticket_id/comments onde temos "project_id" é necessario colocar o id do projeto e onde está "ticket_id" o id do ticket em questão.
  exemplo de retorno:
    [
      {
        "id": "35dd21d7-7050-4d03-9ec2-4134a1a8c268",
        "timestamp": "2022-06-03T02:28:18.819991Z",
        "content": "Esse problema é um problemão",
        "user": {
          "id": "f08d8b53-da3f-46c1-8f1e-aaec5ff282fe",
          "username": "Lourivan Rodrigues",
          "email": "lourivan-rodrigues@hotmail.com"
        }
      }
    ]

## Funcionalidades Futuras

- Filtragem de tickets por tipo, usuário, data de criação, módulo, status, comentários e qualquer outro dado importante;
- Alterações nos tickets, como designações de usuários e alterações de status, são automaticamente registradas nos comentários;
- Status inicial do ticket fixado em reported;
- Sistema de convite por email, notificando o usuário sobre convites para novos projetos;
- Sistema de log de ações, registrando todos os comentários pertinentes até que o usuário marque-os como lidos.

## Stack Utilizada

**Back-end:** Django, Django REST Framework

**Banco de dados:** PostgreSQL
