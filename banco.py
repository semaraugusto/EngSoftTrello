import sqlite3

conexao = None
proxEstoriaID = 0
proxTarefaID = 0

tabelaEstorias = """CREATE TABLE IF NOT EXISTS estorias (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					nome TEXT,
					descricao TEXT,
					story_points INTEGER);"""

tabelaTarefas =  """CREATE TABLE IF NOT EXISTS tarefas (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					id_estoria INTEGER,
					nome TEXT,
					descricao TEXT);"""

def createTables():
	global conexao

	c = conexao.cursor()

	c.execute(tabelaEstorias)
	c.execute(tabelaTarefas)
	
	conexao.commit()
	c.close()


def executeNonQuery(command):
	global conexao

	c = conexao.cursor()

	c.execute(command)

	conexao.commit()
	c.close()


def executeQuery(command):
	global conexao
	result = []

	c = conexao.cursor()
	c.execute(command)

	for linha in c:
		result.append(linha)

	c.close()
	return result


def countQuery(tabela):
	global conexao

	command = "SELECT COUNT(*) FROM {a};"
	command = command.format(a=tabela)
	
	c = conexao.cursor()
	c.execute(command)

	for linha in c:
		ret = linha[0]

	return int(ret)


def selectAllQuery(tabela, id):

	command = "SELECT * FROM {a} WHERE id = {b};"
	command = command.format(a=tabela, b=id)
	return executeQuery(command)

def deleteByIDQuery(tabela, id):

	command = "DELETE FROM {a} WHERE id = {b};"
	command = command.format(a=tabela, b=id)
	executeNonQuery(command)


def inicializaBanco():
	global conexao, proxEstoriaID

	conexao = sqlite3.connect('engsoft.db')
	createTables()

	proxEstoriaID = countQuery('estorias') + 1
	proxTarefaID = countQuery('tarefas') + 1


def insertEstoria(nome, descricao, story_points):
	global proxEstoriaID

	command = "INSERT INTO estorias(nome, descricao, story_points) VALUES ('{a}', '{b}', {c});"
	command = command.format(a=nome, b=descricao, c=story_points)
	executeNonQuery(command)

	proxEstoriaID = proxEstoriaID + 1


def updateEstoria(id, nome, descricao, story_points):

	command = "UPDATE estorias SET nome = '{a}', descricao = '{b}', story_points = {c} WHERE id = {d};"
	command = command.format(a=nome, b=descricao, c=story_points, d=id)
	executeNonQuery(command)


def insertTarefa(id_estoria, nome, descricao):
	global proxTarefaID

	command = "INSERT INTO tarefas(id_estoria, nome, descricao) VALUES ({a}, '{b}', '{c}');"
	command = command.format(a=id_estoria, b=nome, c=descricao)
	executeNonQuery(command)

	proxTarefaID = proxTarefaID + 1


def updateTarefa(id, id_estoria, nome, descricao):

	command = "UPDATE tarefas SET id_estoria = {a}, nome = '{b}', descricao = '{c}' WHERE id = {d};"
	command = command.format(a=id_estoria, b=nome, c=descricao, d=id)
	executeNonQuery(command)