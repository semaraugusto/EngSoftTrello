import sqlite3

conexao = None
proxEstoriaID = 0

tabelaEstorias = """CREATE TABLE IF NOT EXISTS estorias (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					nome TEXT,
					descricao TEXT,
					story_points INTEGER);"""

def createTables():
	global conexao

	c = conexao.cursor()

	c.execute(tabelaEstorias)
	
	conexao.commit()
	c.close()


def executeNonQuery(command):
	global conexao

	c = conexao.cursor()

	c.execute(command)

	conexao.commit()
	c.close()


def countQuery(tabela):
	global conexao

	command = "SELECT COUNT(*) FROM {a};"
	command = command.format(a=tabela)
	
	c = conexao.cursor()
	c.execute(command)

	for linha in c:
		ret = linha[0]

	return int(ret)


def inicializaBanco():
	global conexao, proxEstoriaID

	conexao = sqlite3.connect('engsoft.db')
	createTables()

	proxEstoriaID = countQuery('estorias') + 1


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
