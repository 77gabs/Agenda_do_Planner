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
tela_inicio()