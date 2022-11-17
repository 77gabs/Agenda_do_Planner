from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import sqlite3 as lite
from visualizar import *
import os
if not os.path.isfile("Bancodedados.db"):
    os.system("python banco.py")

def tela_inicio():
    janelaInicial = Tk()
    janelaInicial.title("Planner LGYV")
    janelaInicial.geometry("800x400")
    janelaInicial.resizable(width=False, height=False)
    img_telainicial = PhotoImage(file='interface/telas/telInicio.png')
    img_botaologin = PhotoImage(file='interface/botoes/botaoLogin.png')
    img_botaocadastro = PhotoImage(file='interface/botoes/botaoCadastro.png')
    lab_fundo = Label(janelaInicial, image=img_telainicial)
    lab_fundo.pack()
    # Criação de botões
    bt_login = Button(janelaInicial, bd=0, bg='white', image=img_botaologin,command=lambda: [janelaInicial.destroy(), tela_login()])
    bt_login.place(width=100, height=30, x=448, y=345)

    bt_cadastro = Button(janelaInicial, bd=0, bg='white', image=img_botaocadastro,command=lambda: [janelaInicial.destroy(), telCadastrar()])
    bt_cadastro.place(width=100, height=30, x=253, y=345)
    janelaInicial.mainloop()

def telCadastrar():
    janelaCadastro = Tk()
    janelaCadastro.title(" ")
    janelaCadastro.geometry("800x400")
    janelaCadastro.resizable(width=FALSE, height=FALSE)
    img_telacadastro = PhotoImage(file='interface/telas/telCadastro.png')
    imagem_B_VOLTAR = PhotoImage(file='interface/botoes/botaoVoltar.png')
    img_botaoconcluir = PhotoImage(file='interface/botoes/botaoCadastrar.png')
    lab_fundo = Label(janelaCadastro, image=img_telacadastro)
    lab_fundo.pack()

    # Configurando entrada de dados
    entryNome = Entry(janelaCadastro, bd=2, bg='black',fg='white', justify=CENTER)
    entryNome.place(width=160, height=30, x=320, y=120)

    entryEmail = Entry(janelaCadastro,  bd=2, bg='black',fg='white', justify=CENTER)
    entryEmail.place(width=160, height=30, x=320, y=223)

    EntrySenha = Entry(janelaCadastro, show='*', bg='black', bd=2, fg='white', justify=CENTER)
    EntrySenha.place(width=160, height=30, x=320, y=275)

    EntryTelefone = Entry(janelaCadastro, bd=2, bg='black',fg='white', justify=CENTER)
    EntryTelefone.place(width=160, height=30, x=320, y=170)
    def cadastroUsuarios(email, senha, telefone):
    if email and senha and telefone:
        if not (11 < len(email) < 40):
            messagebox.showerror(title='ATENÇÃO!', message='Tamanho mínimo do email é 11 caracteres e máximo de 40')
            return False
        elif not nomesDisponivel(email):
            messagebox.showerror(title='ATENÇÃO', message='Este email já está cadastrado!')
            return False
        elif not (4 < len(senha) < 20):
            messagebox.showerror(title='ATENÇÃO!', message='Tamanho mínimo da Senha é 4 caracteres e máximo de 20')
            return False
        elif not (9 < len(telefone) < 15):
            messagebox.showerror(title='ATENÇÃO!', message='Tamanho mínimo do telefone é 5 algarismos e máximo de 20')
            return False
        else:
            global UserAtualLYGV
            with conexao:
                i = [email, senha, telefone]
                cursor = conexao.cursor()
                query = "INSERT INTO usuario (nome, senha, backup) VALUES (?, ?, ?)"
                cursor.execute(query, i)
            UserAtualLYGV = usuario(email, senha, telefone)
            return True
    else:
        messagebox.showerror(title='ERRO', message='Dados não podem ser vazios')
        return False
          
    janelaCadastro.mainloop()
tela_inicio()


