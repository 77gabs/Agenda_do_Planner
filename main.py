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
    bt_login.place(width=100, height=30, x=350, y=325)

    bt_cadastro = Button(janelaInicial, bd=0, bg='white', image=img_botaocadastro,command=lambda: [janelaInicial.destroy(), telCadastrar()])
    bt_cadastro.place(width=100, height=30, x=350, y=265)
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
          elif not emailsDisponiveis(email):
              messagebox.showerror(title='ATENÇÃO', message='Este email já está cadastrado!')
              return False
          elif not (4 < len(senha) < 20):
              messagebox.showerror(title='ATENÇÃO!', message='Tamanho mínimo da Senha é 4 caracteres e máximo de 20')
              return False
          elif not (8 < len(telefone) < 14):
              messagebox.showerror(title='ATENÇÃO!', message='Tamanho mínimo do telefone é 8 algarismos e máximo de 14')
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
    def emailsDisponiveis(NomeUsuario):
        with conexao:
            cursor = conexao.cursor()
            query = "SELECT nome FROM usuario WHERE nome == ?"
            cursor.execute(query, [NomeUsuario])
            user = cursor.fetchall()
            return False if user else True
    def emailsDisponiveis(NomeUsuario):
        with conexao:
            cursor = conexao.cursor()
            query = "SELECT nome FROM usuario WHERE nome == ?"
            cursor.execute(query, [NomeUsuario])
            user = cursor.fetchall()
            return False if user else True
    botaovoltar = Button(janelaCadastro,bd=0,image=imagem_B_VOLTAR,command=lambda: [janelaCadastro.destroy(), tela_inicio()])
    botaovoltar.place(width=70, height=50, x=10, y=10)
    # Criação dos botões
    bt_concluir = Button(janelaCadastro,bd=0,image=img_botaoconcluir,command=lambda: [janelaCadastro.destroy(), Agendamentos2022()]if cadastroUsuarios(entryEmail.get(), EntrySenha.get(), EntryTelefone.get()) else [])
    bt_concluir.place(width=120, height=28, x=340, y=328)
    janelaCadastro.mainloop()

#tela Login
def tela_login():
    janelaLogin = Tk()
    janelaLogin.title(" ")
    janelaLogin.geometry("800x400")
    janelaLogin.resizable(width=False, height=False)
    img_telalogin = PhotoImage(file='interface/telas/telLogin.png')
    imagem_B_VOLTAR = PhotoImage(file='interface/botoes/botaoVoltar.png')
    img_botaoinicia = PhotoImage(file='interface/botoes/botaoEntrar.png')
    img_btesquece = PhotoImage(file='interface/botoes/botaoEsqueceuSenha.png')
    lab_fundo = Label(janelaLogin, image=img_telalogin)
    lab_fundo.pack()
    # Configurando entrada de dados
    entryEmail = Entry(janelaLogin, bd=2, bg='black',fg='white', justify=CENTER)
    entryEmail.place(width=196, height=37, x=300, y=159)

    EntrySenha = Entry(janelaLogin, show='*', bd=2, bg='black', fg='white', justify=CENTER)
    EntrySenha.place(width=196, height=37, x=300, y=225)
    # Botões
    botaovoltar = Button(janelaLogin, bd=0, bg='black', image=imagem_B_VOLTAR,command=lambda: [janelaLogin.destroy(), tela_inicio()])
    botaovoltar.place(width=70, height=50, x=10, y=10)

    botaoIniciarCS = Button(janelaLogin, bd=0, bg='white', image=img_botaoinicia, command=lambda: [janelaLogin.destroy(), Agendamentos2022()]if login_valido(entryEmail.get(), EntrySenha.get()) else [loginError()])
    botaoIniciarCS.place(width=125, height=36, x=338, y=283)

    bt_esquecesenha = Button(janelaLogin, bd=0, bg='black', image=img_btesquece, command=lambda: [janelaLogin.destroy(), EsqueceuSenha()])
    bt_esquecesenha.place(width=135, height=20, x=330, y=326)

    janelaLogin.mainloop()

def Agendamentos2022():
    JanelaAgendametos = Tk()
    JanelaAgendametos.title(" ")
    JanelaAgendametos.geometry("800x400")
    JanelaAgendametos.resizable(width=FALSE, height=FALSE)

    ImagemCima = PhotoImage(file='interface/telas/telaMenuAgendamentos.png')
    ImagemEsquerda = PhotoImage(file='interface/telas/telAgendamentos.png')
    imagem_B_VOLTAR = PhotoImage(file='interface/botoes/botaoDeslogar.png')

    L_Cima = Label(JanelaAgendametos, image=ImagemCima)
    L_Cima.pack()
    L_Esquerda = Label(JanelaAgendametos, image=ImagemEsquerda)
    L_Esquerda.pack(side=LEFT)
    # Configurando Frames 
    direita = Frame(JanelaAgendametos, width=577, height=500,bd=1, bg=cor0, relief="raise")
    direita.pack(padx=1, pady=0)
    #Entrada de dados
    entryNome = Entry(JanelaAgendametos, bd=2, bg='black',fg='white', justify=CENTER)
    entryNome.place(width=220, height=36, x=12, y=68)

    entryData = DateEntry(JanelaAgendametos, width=21, background='darkblue',foreground='white', borderwidth=4, year=2022)
    entryData.place(x=50, y=130)

    entryDescricao = Text(JanelaAgendametos, bd=2, bg='black', fg='white')
    entryDescricao.place(width=240, height=140, x=12, y=185)

    # adicoionar Agendamentos
    def criarAgends():
        global UserAtualLYGV
        nome = entryNome.get()
        dia = entryData.get()
        descricao = entryDescricao.get(1.0, 'end')
        id = UserAtualLYGV.recuperar_id()
        lista = [nome, dia, descricao, id]

        if nome=='':
            messagebox.showerror('Atenção!', 'Nome de agendamento não pode ser vazio')
        else:
            agendamento.inserir_info(lista)
            messagebox.showinfo('Feito!', 'Dados adicionados com sucesso.')

            entryNome.delete(0, 'end')
            entryData.delete(0, 'end')
            entryDescricao.delete(1.0, 'end')
        for widget in direita.winfo_children():
            widget.destroy()

        MostrarDados()
# Atualizar agendamentos
    def atualizar():
        try:
            tttDados = maioOi.focus()
            tttdicionario = maioOi.item(tttDados)
            tttLista = tttdicionario['values']

            valor_id = tttLista[0]

            entryNome.delete(0, 'end')
            entryData.delete(0, 'end')
            entryDescricao.delete(1.0, 'end')

            entryNome.insert(0, tttLista[1])
            entryData.insert(0, tttLista[2])
            entryDescricao.insert(1.0, tttLista[3])

            def update():
                nome = entryNome.get()
                dia = entryData.get()
                descricao = entryDescricao.get(1.0, 'end')

                lista = [nome, dia, descricao, valor_id]

                if nome == '':
                    messagebox.showerror('Atenção!', 'Nome de agendamento não pode ser vazio.')
                else:
                    agendamento.atualizar_info(lista)
                    messagebox.showinfo('Feito!', 'Dados modificados com sucesso.')

                    entryNome.delete(0, 'end')
                    entryData.delete(0, 'end')
                    entryDescricao.delete(1.0, 'end')

                for widget in direita.winfo_children():
                    widget.destroy()

                MostrarDados()

            # Botão para confirmar
            b_confirmar = Button(JanelaAgendametos, command=update,text='Confirmar', bg=cor1)
            b_confirmar.place(width=75, height=25, x=85, y=328)

        except IndexError:
            messagebox.showerror('Atenção!', 'Selecione um dos dados na tabela, para fazer modificações.')

    # função deletar eventos
    def deletar():
      #TRY AQUII
        try:
            tttDados = maioOi.focus()
            tttdicionario = maioOi.item(tttDados)
            tttLista = tttdicionario['values']

            valor_id = [tttLista[0]]

            agendamento.deletar_info(valor_id)
            messagebox.showinfo('Feito!', 'Dados apagados com exeto.')

            for widget in direita.winfo_children():
                widget.destroy()

            MostrarDados()
        #EXCEPT AQUII
        except IndexError:
            messagebox.showerror(
                'Atenção!', 'Selecione um dos dados na tabela, para fazer ações.')

    def MostrarDados():
        global maioOi
        global UserAtualLYGV
        id = UserAtualLYGV.recuperar_id()
        lista = agendamento.mostrar_info(id)
        # Lista para banco de dados
        tabela_header = ['Nº', 'Nome', 'Data', 'Descrição']
        # Criação de tabelas
        maioOi = ttk.Treeview(direita, height=17, selectmode="extended",columns=tabela_header, show="headings")
        # Vertical scrollbar
        vsb = ttk.Scrollbar(direita, orient="vertical", command=maioOi.xview)
        maioOi.configure(yscrollcommand=vsb.set)
        maioOi.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')

        direita.grid_rowconfigure(0, weight=12)

        hd = ['nw', 'nw', 'center', 'nw']
        h = [30, 140, 120, 280]
        n = 0

        for col in tabela_header:
            maioOi.heading(col, text=col.title(), anchor=CENTER)
            maioOi.column(col, width=h[n], anchor=hd[n])
          
            n += 1

        for item in lista:
            maioOi.insert('', 'end', values=item)
          
    # Criação dos botões
    botaovoltar = Button(JanelaAgendametos, bg='black', bd=0, image=imagem_B_VOLTAR,command=lambda: [JanelaAgendametos.destroy(), tela_inicio()])
    botaovoltar.place(width=95, height=40, x=700, y=4)
    
    bt_inserir = Button(JanelaAgendametos, text='Criar',bd=0, bg='blue', command=criarAgends)
    bt_inserir.place(width=80, height=25, x=5, y=358)

    bt_atualizar = Button(JanelaAgendametos, text='Modificar',bg='green', command=atualizar)
    bt_atualizar.place(width=80, height=25, x=100, y=358)

    bt_deletar = Button(JanelaAgendametos, bd=0,text='Deletar', bg='red', command=deletar)
    bt_deletar.place(width=80, height=25, x=195, y=358)
    # função deletar eventos
    def deletar():
      #TRY AQUII
        try:
            tttDados = maioOi.focus()
            tttdicionario = maioOi.item(tttDados)
            tttLista = tttdicionario['values']

            valor_id = [tttLista[0]]

            agendamento.deletar_info(valor_id)
            messagebox.showinfo('Feito!', 'Dados apagados com exeto.')

            for widget in direita.winfo_children():
                widget.destroy()

            MostrarDados()
        #EXCEPT AQUII
        except IndexError:
            messagebox.showerror(
                'Atenção!', 'Selecione um dos dados na tabela, para fazer ações.')



    # Chamando a função MostrarDados
    MostrarDados()
    JanelaAgendametos.mainloop()

def login_valido(NomeUsuario, senha):
    global UserAtualLYGV
    if NomeUsuario and senha:
        if recuperacaoDAsenha(NomeUsuario) != senha:
            return False
        else:
            user = ResgatarUsuario(NomeUsuario)
           
            UserAtualLYGV = usuario(user[0][1], user[0][2], user[0][3])
            return True
    else:
        return False
      
#recuperar senha
def recuperacaoDAsenha(NomeUsuario):
    with conexao:
        cursor = conexao.cursor()
        query = "SELECT senha FROM usuario WHERE nome == ?"
        cursor.execute(query, [NomeUsuario])
        senha_user = cursor.fetchall()
    if senha_user:
        return senha_user[0][0]

tela_inicio()