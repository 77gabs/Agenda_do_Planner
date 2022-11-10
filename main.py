from tkinter import *
import sqlite3
from pandas import *

# #Criando o Banco de Dados:
conexao = sqlite3.connect('clientes.db')
cor1 = '#B0C4DE'
#arquivo = open('clientes.xlsx', '+a')
# # Criando o cursor:
c = conexao.cursor()


# # Criando a tabela:
c.execute("""CREATE TABLE IF NOT EXISTS  clientes (
     nome text,
     sobrenome text,
    email text,
    telefone text
     )""")