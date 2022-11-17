#SQLite
import sqlite3 as lite
#conexão
conexao = lite.connect('Bancodedados.db')

class usuario:
  def __init__(self,nome,senha,telefone):
    self.nome = nome
    self.__senha = senha
    self.__backup = telefone
  def recuperar_id(self):
    with conexao:
      cursor = conexao.cursor()
      query = "SELECT id FROM usuario WHERE nome == ?"
      cursor.execute(query, [self.nome])
      id_usuario = cursor.fetchall()
    return id_usuario[0][0]

print("Aparentemente não está rodando!!!")