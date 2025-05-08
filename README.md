# 🩸 Doe+Conecta: Aplicativo para Doação de Sangue
### Doação De Sangue Na Palma Da Mão <br>
Tecnologia em prol da vida: um app para otimizar o processo de conexão entre Doadores e Receptores

O `Doe+Conecta` é um aplicativo mobile inovador desenvolvido para facilitar a doação de sangue e *conectar doadores e receptores* de maneira mais eficiente. A doação de sangue é um ato de solidariedade crucial para salvar vidas, mas enfrenta desafios, como a manutenção de estoques adequados nos bancos de sangue. Este aplicativo visa otimizar esse processo, oferecendo diversas funcionalidades que tornam a doação mais simples e acessível.

### Funcionalidades Principais:
- ***Conexão entre doadores e receptores:*** O aplicativo conecta doadores a pessoas que necessitam de sangue, facilitando o processo de doação.
- ***Integração com redes sociais:*** Promove o engajamento ativo da comunidade, incentivando mais pessoas a se tornarem doadoras.
- ***Monitoramento de saúde:*** Os doadores podem acompanhar sua saúde, com acesso a informações sobre histórico médico, garantindo um suporte personalizado.
- ***Apoio aos bancos de sangue e hospitais:*** O aplicativo atende às necessidades dos doadores e dos estabelecimentos de saúde, ajudando na gestão eficiente dos estoques de sangue.

O `Doe+Conecta` tem o objetivo de não só facilitar a doação, mas também de construir uma rede de solidariedade e aumentar a conscientização sobre a importância desse gesto vital.

##  Estrutura da Tabela Doadores
A tabela `Doadores` é responsável por armazenar os seguintes dados:

- ***id:*** Campo único para identificar cada doador, configurado como chave primária (PK) e autoincrementável, ou seja, o valor será gerado automaticamente a cada novo registro.
- ***nome:*** Campo de texto para armazenar o nome do doador. É obrigatório (NOT NULL).
- ***contato:*** Campo de texto para armazenar o contato do doador (telefone ou e-mail). Também é obrigatório (NOT NULL).

### Script SQL para Criação da Tabela

```
-- Criação da tabela de doadores
CREATE TABLE IF NOT EXISTS Doadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID único do doador (chave primária)
    nome TEXT NOT NULL,                   -- Nome do doador
    contato TEXT NOT NULL                 -- Contato do doador (telefone ou e-mail)
);

```

Esse script pode ser executado no seu sistema de gerenciamento de banco de dados para criar a tabela onde as informações dos doadores serão armazenadas.

## Tela Login

![tela_login](https://github.com/feer-rodriguess90/DoeMaisConecta-App/blob/main/assets/TelaLogin.png)

## Tela Cadastro

![tela_cadastro](https://github.com/feer-rodriguess90/DoeMaisConecta-App/blob/main/assets/TelaCadastro.png)

## Tela Adicionar Doador

![tela_adicionar_doador](https://github.com/feer-rodriguess90/DoeMaisConecta-App/blob/main/assets/TelaAdicionarDoador.png)

## Tela de Opções

A tela de Opções do aplicativo `Doe+Conecta` foi projetada para oferecer ao usuário uma experiência simples e funcional, reunindo recursos essenciais para facilitar e incentivar a doação de sangue. Veja abaixo as funcionalidades disponíveis:

1. ***Encontre Posto de Coleta:***
Essa opção permite ao usuário localizar o ponto de coleta mais próximo de sua residência. Utilizando geolocalização e informações atualizadas, o aplicativo indica hemocentros e bancos de sangue próximos, incluindo endereço e horário de funcionamento.

2. ***Agendamento de Doações:***
Com essa funcionalidade, é possível agendar uma doação de sangue diretamente pelo aplicativo. O usuário escolhe a data, o horário e o local de preferência, garantindo praticidade e organização para o processo de doação.

3. ***Campanha de Doações:***
Aqui, o usuário pode acessar informações sobre campanhas de doação de sangue e ações de conscientização. O aplicativo divulga eventos especiais, como mutirões de doação, além de mensagens educativas sobre a importância de doar sangue regularmente.

4. ***Chat Tira-Dúvidas:***
O aplicativo oferece um canal de comunicação direto com hemocentros e profissionais da área da saúde. Os usuários podem tirar dúvidas sobre requisitos para doação, processos de coleta, cuidados pré e pós-doação, entre outras informações importantes.

![tela_opcoes](https://github.com/feer-rodriguess90/DoeMaisConecta-App/blob/main/assets/TelaOpcoes.png)

## 🛠 Tecnologias Utilizadas

- ***Python:*** Linguagem principal usada para desenvolver a lógica e funcionalidades do aplicativo.
- ***Flet:*** Framework utilizado para criar interfaces modernas e responsivas, com foco em aplicações mobile e desktop.
- ***SQLite3:*** Banco de dados leve integrado para armazenar informações de doadores, campanhas e agendamentos.
- ***Figma:*** Ferramenta usada para criar o design e prototipar as telas do aplicativo. [Acesse aqui o protótipo do Figma](https://www.figma.com/design/UcwYltqQKnXLRBqCrN03q7/Untitled?node-id=0-1&node-type=canvas&t=jofE42Lwpok1l4Xi-0) 

## 🤝🏽 Colaboradores 

- Álvaro Silva Garcia
- Amanda Duarte De Almeida
- Bryan Cardoso Da Silva
- Fernanda Rodrigues Da Cunha
- Flavia Aparecida Lara Cardoso
- Samara Rodrigues Dos Santos Cupertino



## Happy coding! 👩🏽‍💻 
[![linkedin](https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/datavizwithfer/) 
[![medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@DataVizWithFer)

<div align="center">
<img src="https://forthebadge.com/images/badges/built-with-love.svg" />
</div>
