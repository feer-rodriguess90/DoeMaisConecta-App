from flet import *
import sqlite3

#Connectando ao banco de dados
conexao = sqlite3.connect("dados.db", check_same_thread=False)
cursor = conexao.cursor()

#Criar uma tabela no banco de dados
def tabela_base():
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT NOT NULL, contato TEXT)
    '''
    )

class App(UserControl):
    def __init__(self):
        super().__init__()

        self.todos_doadores = Column(auto_scroll=True)
        self.adicionar_doador = TextField(label='Nome do doador')
        self.adicionar_contato = TextField(label='Contato')
        self.editar_nome = TextField(label='Editar Nome')
        self.editar_contato = TextField(label='Editar Contato')

    # (DELETE) Função deletar dado
    def deletar(self, id_user, alerta_dialogo):
        print(f"Deletando ID: {id_user}") #depuração
        cursor.execute("DELETE FROM clientes WHERE id = ?", [id_user])
        conexao.commit()
        alerta_dialogo.open = False

        #Chamar a função de renderizar dados
        self.todos_doadores.controls.clear()
        self.renderizar_todos()
        self.page.update()

    # (UPDATE) Função atualizar dado
    def atualizar(self, id_user, nome, contato, alerta_dialogo):
        print(f"Atualizando o doador com ID: {id_user}, Nome: {nome}, Contato: {contato}")  # Para depuração
        cursor.execute("UPDATE clientes SET nome = ?, contato = ? WHERE id = ?", (nome, contato, id_user))
        conexao.commit()

        # Fechar o alerta após atualizar
        alerta_dialogo.open = False

        self.todos_doadores.controls.clear()
        self.renderizar_todos()
        self.page.update()

    #Função para abrir as ações
    def abrir_acoes(self, e):
        # Pegando as informações do item clicado
        try:
            parts = e.control.subtitle.value.split(" | ")
            id_user = parts[0].replace("ID: ", "")
            nome = parts[1].replace("Doador: ", "") if len(parts) > 1 else ""
            contato = parts[2].replace("Contato: ", "") if len(parts) > 2 else ""
        except IndexError:
            # Caso a string não tenha os elementos esperados, define como vazio
            id_user, nome, contato = "", "", ""

        # Verificando se as variáveis estão preenchidas corretamente
        print(f"ID: {id_user}, Nome: {nome}, Contato: {contato}")  # Para depuração

        # Preencher os campos de edição com as informações atuais
        self.editar_nome.value = nome
        self.editar_contato.value = contato
        self.update()

        alerta_dialogo = AlertDialog(
            title=Text(f"Editar ID: {id_user}"),
            content=Column(  # Dois campos de edição no conteúdo do alerta
                controls=[self.editar_nome, self.editar_contato]
            ),

            #Botão de Ação
            actions=[
                ElevatedButton(
                    'Deletar',
                    color='white', bgcolor='red',
                    on_click= lambda e:self.deletar(id_user, alerta_dialogo)
                ),
                ElevatedButton(
                    'Atualizar', 
                    on_click=lambda e: self.atualizar(id_user, self.editar_nome.value, self.editar_contato.value, alerta_dialogo)
                )
            ],
            actions_alignment='spaceBetween'
        )

        self.page.dialog = alerta_dialogo
        alerta_dialogo.open = True 

        #atualizar a página
        self.page.update()


    #(READ) Mostrar todos dados do banco de dados 
    def renderizar_todos(self):
        cursor.execute("SELECT * FROM clientes")
        conexao.commit()

        meus_dados = cursor.fetchall()

        # Se não houver dados, exibe um texto informativo
        if not meus_dados:
            self.todos_doadores.controls.append(Text("Nenhum doador encontrado.", size=14))
        
        for dado in meus_dados:
            self.todos_doadores.controls.append(
                ListTile(
                    subtitle=Text(f"ID: {dado[0]} | Doador: {dado[1]} | Contato: {dado[2]}"),  # ID e Contato
                    on_click=self.abrir_acoes
                )
            )
        self.update()
        

    def ciclo(self):
        self.renderizar_todos()

    #(CREATE) Criar um dado dentro do banco de dados 
    def adicionar_novo_doador(self, e):
        cursor.execute("INSERT INTO clientes (nome, contato) VALUES (?, ?)", 
                       [self.adicionar_doador.value, self.adicionar_contato.value])
        conexao.commit()

        self.todos_doadores.controls.clear()
        self.renderizar_todos()
        self.page.update()


    def build(self):
        return Column([
            Text("DOE + CONECTA", size=25, weight='bold', color="white"),
            Text("Adicionar doador", size=20),
            self.adicionar_doador,
            self.adicionar_contato,
            ElevatedButton(
                'Adicionar',
                on_click=self.adicionar_novo_doador,
            ),
            self.todos_doadores
        ],
        alignment="center",  
        horizontal_alignment="center",  
    )


def main(page:Page):
    tabela_base()
    page.update()
    minha_aplicacao = App()

    page.bgcolor = colors.TRANSPARENT
    page.decoration = BoxDecoration(
        image=DecorationImage(
            src="assets/DoeMais.png",
            fit=ImageFit.COVER,
            opacity=0.9,
        )
    )

    page.window.height = 700
    page.window.width = 350         
    
    page.add(
        minha_aplicacao, 
    )


app(target=main)