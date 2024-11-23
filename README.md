# 🩸 Doe+Conecta: Aplicativo para Doação de Sangue
### Doação De Sangue Na Palma Da Mão <br>
Tecnologia em prol da vida: um app para otimizar o processo de conexão entre Doadores e Receptores

O **Doe+Conecta** é um aplicativo mobile inovador desenvolvido para facilitar a doação de sangue e *conectar doadores e receptores* de maneira mais eficiente. A doação de sangue é um ato de solidariedade crucial para salvar vidas, mas enfrenta desafios, como a manutenção de estoques adequados nos bancos de sangue. Este aplicativo visa otimizar esse processo, oferecendo diversas funcionalidades que tornam a doação mais simples e acessível.

### Funcionalidades Principais:
- **Conexão entre doadores e receptores:** O aplicativo conecta doadores a pessoas que necessitam de sangue, facilitando o processo de doação.
- **Integração com redes sociais:** Promove o engajamento ativo da comunidade, incentivando mais pessoas a se tornarem doadoras.
- **Monitoramento de saúde:** Os doadores podem acompanhar sua saúde, com acesso a informações sobre histórico médico, garantindo um suporte personalizado.
- **Apoio aos bancos de sangue e hospitais:** O aplicativo atende às necessidades dos doadores e dos estabelecimentos de saúde, ajudando na gestão eficiente dos estoques de sangue.

O **Doe+Conecta** tem o objetivo de não só facilitar a doação, mas também de construir uma rede de solidariedade e aumentar a conscientização sobre a importância desse gesto vital.

##  Estrutura da Tabela Doadores
A tabela `Doadores` é responsável por armazenar os seguintes dados:

- **id:** Campo único para identificar cada doador, configurado como chave primária (PK) e autoincrementável, ou seja, o valor será gerado automaticamente a cada novo registro.
- **nome:** Campo de texto para armazenar o nome do doador. É obrigatório (NOT NULL).
- **contato:** Campo de texto para armazenar o contato do doador (telefone ou e-mail). Também é obrigatório (NOT NULL).

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

## 🤝🏽 Colaboradores 

- Álvaro Silva Garcia
- Bryan Cardoso Da Silva
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
