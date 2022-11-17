# Importando SQLite
import sqlite3 as lite

# Criando conexão
conexao = lite.connect('Bancodedados.db')

# Criando tabela Usuário
with conexao:
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuario( " "id INTEGER PRIMARY KEY AUTOINCREMENT," "nome TEXT," "senha TEXT," "backup TEXT)")

# Criando tabela Agendamento
with conexao:
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS agendamento( " "id INTEGER PRIMARY KEY AUTOINCREMENT," "nome TEXT," "data_agendamento DATE," "descricao TEXT," "id_usuario INTEGER" "FOREIGN KEY REFERENCES usuario(id))")