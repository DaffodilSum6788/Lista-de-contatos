from tkinter import *
from tkinter import ttk
import mysql.connector

#funções do CRUD

# estabelece uma conexão com o banco de dados
conexaosql = mysql.connector.connect(
    host='localhost',
    user='root',
    password='VHgfpmK27Vtq7j',
    database='lista_de_contatos',
)

#estabelece um cursor
cursor = conexaosql.cursor()

#criar um novo contato (pede as variáveis e insere)

def create():
    
    nome = nome_inserido.get()
    telefone = telefone_inserido.get()
    email = email_inserido.get()
    data_de_nascimento = data_inserida.get()
    notas = notas_inseridas.get()

    comando_create = f'INSERT INTO contatos (nome, telefone, email, data_de_nascimento, notas) VALUES ("{nome}", "{telefone}", "{email}", "{data_de_nascimento}", "{notas}")'

    cursor.execute(comando_create)

    conexaosql.commit()



#Ler as informações da tabela

def read():
    comando_edit = f'SELECT * FROM contatos'
    cursor.execute(comando_edit)
    resultado = cursor.fetchall()
    print(resultado)

#Alterar alguma informação

def update():
    nome = ""
    
    comando_update = f'UPDATE contatos SET = WHERE nome = "{nome}"'
    cursor.execute(comando_update)
    conexaosql.commit()

#Apagar um contato

def delete():
    nome = nome_inserido.get()

    comando_delete = f'DELETE FROM contatos WHERE nome = "{nome}"'
    cursor.execute(comando_delete)
    conexaosql.commit()


#Funções da interface gráfica (TKinter)


#Criar a interface gráfica
janela = Tk()
janela.title("Lista de Contatos")

#separar frames
frame_esquerda = Frame(janela, height=250, width=200)
frame_esquerda.grid(column=0, row=1)

frame_tabela = Frame(janela, height=250, width=500)
frame_tabela.grid(column=1, row=1)

frame_botoes = Frame(frame_esquerda, height = 50, width=200)
frame_botoes.grid(column=0, row=0)

frame_dados = Frame(frame_esquerda, height=200, width=200)
frame_dados.grid(column=0, row=1)

#Texto de instruções
instrucoes = Label(janela, text="Clique no botão 'Criar Contato' para criar um novo contato.")
instrucoes.grid(column=0, row=0)

#Botões de criar, buscar, editar e apagar contatos
botao_create = Button(frame_botoes, text="Criar Contato", relief=RAISED, command = create)
botao_create.grid(column=0, row=1)

botao_read = Button(frame_botoes, text="Buscar Contato", relief=RAISED, command=read)
botao_read.grid(column=1, row=1)

botao_update = Button(frame_botoes, text="Editar Contato", relief=RAISED)
botao_update.grid(column=2, row=1)

botao_delete = Button(frame_botoes, text="Apagar Contato", relief=RAISED, command=delete)
botao_delete.grid(column=3, row=1)

#Nomes das caixas de texto
label_nome = Label(frame_dados, text= "Nome")
label_nome.grid(column=0, row=0)

label_telefone = Label(frame_dados, text= "Telefone")
label_telefone.grid(column=0, row=1)

label_email = Label(frame_dados, text= "Email")
label_email.grid(column=0, row=2)

label_data = Label(frame_dados, text= "Data")
label_data.grid(column=0, row=3)

label_notas = Label(frame_dados, text= "Notas")
label_notas.grid(column=0, row=4)

#declarar variáveis dos contatos
nome_inserido = StringVar()

telefone_inserido = StringVar()

email_inserido = StringVar()

data_inserida = StringVar()

notas_inseridas = StringVar()

#Caixas de texto para inserir os dados
entrada_nome = Entry(frame_dados, textvariable= nome_inserido)
entrada_nome.grid(column=1, row=0)

entrada_telefone = Entry(frame_dados, textvariable= telefone_inserido)
entrada_telefone.grid(column=1, row=1)

entrada_email = Entry(frame_dados, textvariable= email_inserido)
entrada_email.grid(column=1, row=2)

entrada_data = Entry(frame_dados, textvariable= data_inserida)
entrada_data.grid(column=1, row=3)

entrada_notas = Entry(frame_dados, textvariable= notas_inseridas)
entrada_notas.grid(column=1, row=4)

#tabela dos contatos
tabela = ttk.Treeview(frame_tabela, columns = ('Nome', 'Telefone', 'Email', 'Data_nasc', 'Notas'), show = 'headings')
tabela.heading('Nome', text= 'Nome')
tabela.heading('Telefone', text= 'Telefone')
tabela.heading('Email', text= 'E-mail')
tabela.heading('Data_nasc', text= 'Data de Nascimento')
tabela.heading('Notas', text= 'Notas')
tabela.grid(column=0, row=0)

primeiro_read = f'SELECT nome, telefone, email, data_de_nascimento, notas FROM contatos'
cursor.execute(primeiro_read)
resultado = cursor.fetchall()

contador = 0
for valor in resultado:
    tabela.insert(parent= '', index='end', values=(valor[0], valor[1], valor[2], valor[3], valor[4]))
    cont =+ 1

#Função de atualizar tabela
def atualizar_tabela():

    for dado in tabela:
        tabela.delete(dado)
    ler_todos = f'SELECT nome, telefone, email, data_de_nascimento, notas FROM contatos'
    cursor.execute(ler_todos)
    resultado = cursor.fetchall()

    global cont
    cont = 0
    for valor in resultado:
        tabela.insert(parent= '', index='end', values=(valor[0], valor[1], valor[2], valor[3], valor[4]))
        cont =+ 1

#Botão de atualizar os contatos
botão_atualizar = Button(frame_dados, text="Atualizar Lista", relief=RAISED, command=atualizar_tabela)
botão_atualizar.grid(column=0, row=5)

janela.mainloop()

#fecha as conexões
cursor.close()
conexaosql.close()

#Tentar colocar a criação de contatos na mesma janela que a tabela
#Criar contatos com entry, usando a função create
#Adicionar read, update e delete
