from tkinter import *
import sqlite3
from pandas import *

# #Criando o Banco de Dados:
conexao = sqlite3.connect('clientes.db')
cor1 = '#B0C4DE'
# arquivo = open('clientes.xlsx', '+a')
# # Criando o cursor:
c = conexao.cursor()


# # Criando a tabela:
c.execute("""CREATE TABLE IF NOT EXISTS  clientes (
     nome text,
     sobrenome text,
    email text,
    telefone text
     )""")

# #Commit as mudanças:conexao.commit()

# #Fechar o banco de dados:
conexao.close()

# criação da tela
janela = Tk()
janela.title('Cadastro de Clientes')
janela.configure(background=cor1)
janela. geometry("400x400")

def cadastrar_cliente():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    #Inserir dados na tabela:
    c.execute("INSERT INTO clientes VALUES (:nome,:sobrenome,:email,:telefone)",
              {
                  'nome': entry_nome.get(),
                  'sobrenome': entry_sobrenome.get(),
                  'email': entry_email.get(),
                  'telefone': entry_telefone.get()
              })

 # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada
    entry_nome.delete(0,"end")
    entry_sobrenome.delete(0,"end")
    entry_email.delete(0,"end")
    entry_telefone.delete(0,"end")

#verificar credenciais
credenciais = ['Letícia','1234']

def verificar_senha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin!')
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta ' +credenciais[0])