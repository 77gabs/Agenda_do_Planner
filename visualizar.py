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

class agendamento:
  def __init__(self,nome,data,des,id_usuario):
    self.nome = nome
    self.data = data
    self.descricao = des
    self.__id_user = id_usuario
  #adicionar informações
  def inserir_info(lgyv):
    with conexao:
      cursor = conexao.cursor()
      query = "INSERT INTO agendamento (nome, dia_agendamento, descricao,id_user) VALUES (?, ?, ?, ?)"
      cursor.execute(query, lgyv)
  # Visualizar informações
  def mostrar_info(id_usuario):
    lista = []
    with conexao:
          cursor = conexao.cursor()
          query = "SELECT * FROM agendamento WHERE id_user=?"
          cursor.execute(query,[id_usuario])
          informacao = cursor.fetchall()
          for lgyv in informacao: 
              lista.append(lgyv)
    return lista
  # Atualizar Informações
  def atualizar_info(lgyv):
      with conexao:
          cursor = conexao.cursor()
          query = "UPDATE agendamento SET nome=?, dia_agendamento=?, descricao=? WHERE id=?"
          cursor.execute(query, lgyv) 
  # Deletar Informações
  def deletar_info(lgyv):
      with conexao:
          cursor = conexao.cursor()
          query = "DELETE FROM agendamento WHERE id=?"
          cursor.execute(query, lgyv)