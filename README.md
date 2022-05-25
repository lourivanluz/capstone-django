# Bug Tracker API

Um serviço Back-End que visa cobrir as necessidades de armazenamento de dados
para uma aplicação de rastreamento de bugs. Tem como objetivo agilizar o processo
de desenvolvimento por facilitar o registro e acompanhamento de erros encontrados
em produção, recursos necessários para a garantia de qualidade de qualquer projeto.

## Funcionalidades Principais

- Cadastro e login de usuários;
  - Usuários são cadastrados no banco de dados apenas com seus dados pessoais. Seus projetos e permissões são registrados em processos futuros.
- Criação de projetos:
  - Ao criar um projeto, o usuário é automaticamente cadastrado como administrador do mesmo;
  - Administradores também podem conceder essa permissão à outros usuários.
- Adição de usuários à projetos:
  - Apenas administradores podem adicionar usuários à um projeto.
- Criação de tickets:
  - Qualquer usuário pode criar tickets;
  - Tickets possuem várias informações importantes, como grau de severidade do erro, módulo em que foi encontrado, passos para a reprodução e o tempo estimado para resolvê-lo.
- Adição de usuários à tickets:
  - Qualquer usuário pode adicionar colegas de projeto à um ticket;
  - Vários usuários podem ser designados ao mesmo ticket.
- Adição de comentários à tickets:
  - Qualquer usuário pode adicionar comentários à um ticket.
- Alteração de status de tickets:
  - Apenas usários designados à um ticket podem alterar seu status e demais informações.

## Funcionalidades Adicionais

- Filtragem de tickets por tipo, usuário, data de criação, módulo, status, comentários e qualquer outro dado importante;
- Alterações nos tickets, como designações de usuários e alterações de status, são automaticamente registradas nos comentários;
- Sistema de convite por email, notificando o usuário sobre convites para novos projetos;
- Sistema de log de ações, registrando todos os comentários pertinentes até que o usuário marque-os como lidos.

## Stack Utilizada

**Back-end:** Django, Django REST Framework

**Banco de dados:** PostgreSQL
