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

#Função de atualizar tabela
def atualizar_tabela():

    entrada_nome.delete(0,END)
    entrada_telefone.delete(0,END)
    entrada_email.delete(0,END)
    entrada_data.delete(0,END)
    entrada_notas.delete(0,END)

    for dado in tabela.get_children():
        tabela.delete(dado)

    ler_todos = f'SELECT nome, telefone, email, data_de_nascimento, notas FROM contatos ORDER BY nome'
    cursor.execute(ler_todos)
    resultado = cursor.fetchall()

    for valor in resultado:
        tabela.insert(parent= '', index='end', values=valor)

#Alterar alguma informação

def update():
    nome = nome_inserido.get()
    telefone = telefone_inserido.get()
    email = email_inserido.get()
    data_de_nascimento = data_inserida.get()
    notas = notas_inseridas.get()
    
    comando_update = f'UPDATE contatos SET telefone= "{telefone}", email= "{email}", data_de_nascimento= "{data_de_nascimento}", notas= "{notas}" WHERE nome = "{nome}"'
    cursor.execute(comando_update)
    conexaosql.commit()

#Apagar um contato

def delete():
    nome = nome_inserido.get()

    comando_delete = f'DELETE FROM contatos WHERE nome = "{nome}"'
    cursor.execute(comando_delete)
    conexaosql.commit()

#Funções de busca
def buscar_nome():
    nome = nome_inserido.get()

    for dado in tabela.get_children():
        tabela.delete(dado)
    comando_busca_nome = f'SELECT nome, telefone, email, data_de_nascimento, notas FROM contatos WHERE nome LIKE "%{nome}%" ORDER BY nome'
    cursor.execute (comando_busca_nome)
    resultado = cursor.fetchall()

    for valor in resultado:
        tabela.insert(parent= '', index='end', values=valor)

def buscar_telefone():
    telefone = telefone_inserido.get()

    for dado in tabela.get_children():
        tabela.delete(dado)
    comando_busca_telefone = f'SELECT nome, telefone, email, data_de_nascimento, notas FROM contatos WHERE telefone LIKE "%{telefone}%" ORDER BY nome'
    cursor.execute (comando_busca_telefone)
    resultado = cursor.fetchall()

    for valor in resultado:
        tabela.insert(parent= '', index='end', values=valor)

def buscar_email():
    email = email_inserido.get()

    for dado in tabela.get_children():
        tabela.delete(dado)
    comando_busca_email = f'SELECT nome, telefone, email, data_de_nascimento, notas FROM contatos WHERE email LIKE "%{email}%" ORDER BY nome'
    cursor.execute (comando_busca_email)
    resultado = cursor.fetchall()

    for valor in resultado:
        tabela.insert(parent= '', index='end', values=valor)

def buscar_data():
    data = data_inserida.get()

    for dado in tabela.get_children():
        tabela.delete(dado)
    comando_busca_data = f'SELECT nome, telefone, email, data_de_nascimento, notas FROM contatos WHERE data_de_nascimento LIKE "%{data}%" ORDER BY nome'
    cursor.execute (comando_busca_data)
    resultado = cursor.fetchall()

    for valor in resultado:
        tabela.insert(parent= '', index='end', values=valor)

def buscar_notas():
    notas = notas_inseridas.get()

    for dado in tabela.get_children():
        tabela.delete(dado)
    comando_busca_notas = f'SELECT nome, telefone, email, data_de_nascimento, notas FROM contatos WHERE notas LIKE "%{notas}%" ORDER BY nome'
    cursor.execute (comando_busca_notas)
    resultado = cursor.fetchall()

    for valor in resultado:
        tabela.insert(parent= '', index='end', values=valor)

#Funções da interface gráfica (TKinter)


#Criar a interface gráfica
janela = Tk()
janela.title("Lista de Contatos")

#separar frames
frame_esquerda = Frame(janela, height=250, width=200)
frame_esquerda.grid(column=0, row=1)

frame_tabela = Frame(janela, height=250, width=500)
frame_tabela.grid(column=1, row=1)

frame_botoes_crud = Frame(frame_esquerda, height = 50, width=200)
frame_botoes_crud.grid(column=0, row=0)

frame_dados = Frame(frame_esquerda, height=200, width=200)
frame_dados.grid(column=0, row=1)

frame_botoes_busca = Frame(frame_esquerda, height=50, width=200)
frame_botoes_busca.grid(column=0, row=2)

#Texto de instruções
instrucoes = Label(janela, text="Clique no botão 'Criar Contato' para criar um novo contato.")
instrucoes.grid(column=0, row=0)

#Botões de criar, atualizar, editar e apagar contatos
botao_create = Button(frame_botoes_crud, text="Criar Contato", relief=RAISED, command = create)
botao_create.grid(column=0, row=1)

botao_read = Button(frame_botoes_crud, text="Atualizar Tabela", relief=RAISED, command=atualizar_tabela)
botao_read.grid(column=1, row=1)

botao_update = Button(frame_botoes_crud, text="Editar Contato", relief=RAISED, command=update)
botao_update.grid(column=2, row=1)

botao_delete = Button(frame_botoes_crud, text="Apagar Contato", relief=RAISED, command=delete)
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
tabela.column('Nome', width=150)
tabela.heading('Nome', text= 'Nome')
tabela.column('Telefone', anchor=CENTER, width=100)
tabela.heading('Telefone', text= 'Telefone')
tabela.column('Email', width=200)
tabela.heading('Email', text= 'E-mail')
tabela.column('Data_nasc', anchor=CENTER, width=125)
tabela.heading('Data_nasc', text= 'Data de Nascimento')
tabela.column('Notas', anchor=CENTER, width=275)
tabela.heading('Notas', text= 'Notas')

tabela.grid(column=0, row=0)

#Inserir o contato selecionado nas caixas de texto
def selecionar_item(a):

    #remover qualquer texto que já estava nas entradas
    entrada_nome.delete(0,END)
    entrada_telefone.delete(0,END)
    entrada_email.delete(0,END)
    entrada_data.delete(0,END)
    entrada_notas.delete(0,END)

    #inserir dados selecionados
    item_selecionado = tabela.selection()
    entrada_nome.insert(0, tabela.item(item_selecionado)['values'][0])
    entrada_telefone.insert(0, tabela.item(item_selecionado)['values'][1])
    entrada_email.insert(0, tabela.item(item_selecionado)['values'][2])
    entrada_data.insert(0, tabela.item(item_selecionado)['values'][3])
    entrada_notas.insert(0, tabela.item(item_selecionado)['values'][4])

#vincular a seleção de texto à função de selecionar item
tabela.bind("<<TreeviewSelect>>", selecionar_item)

#Inserir o banco de dados na tabela pela primeira vez
primeiro_read = f'SELECT nome, telefone, email, data_de_nascimento, notas FROM contatos ORDER BY nome'
cursor.execute(primeiro_read)
resultado = cursor.fetchall()
''
for valor in resultado:
    tabela.insert(parent= '', index='end', values=valor)

#Botões de buscar
botao_buscar_nome = Button(frame_botoes_busca, text="Buscar Nome", relief=RAISED, command=buscar_nome)
botao_buscar_nome.grid(column=0, row=0)

botao_buscar_telefone = Button(frame_botoes_busca, text="Buscar Telefone", relief=RAISED, command=buscar_telefone)
botao_buscar_telefone.grid(column=1, row=0)

botao_buscar_email = Button(frame_botoes_busca, text="Buscar E-mail", relief=RAISED, command=buscar_email)
botao_buscar_email.grid(column=2, row=0)

botao_buscar_data = Button(frame_botoes_busca, text="Buscar Data de Nasc.", relief=RAISED, command=buscar_data)
botao_buscar_data.grid(column=3, row=0)

botao_buscar_notas = Button(frame_botoes_busca, text="Buscar Notas", relief=RAISED, command=buscar_notas)
botao_buscar_notas.grid(column=4, row=0)

janela.mainloop()

#fecha as conexões
cursor.close()
conexaosql.close()
