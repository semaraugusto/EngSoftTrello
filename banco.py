import sqlite3

conexao = None
proxEstoriaID = 0
proxTarefaID = 0
proxUsuarioID = 0
proxEquipeID = 0

tabelaEstorias = """CREATE TABLE IF NOT EXISTS estorias (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					nome TEXT,
					descricao TEXT,
					story_points INTEGER);"""

tabelaTarefas = """CREATE TABLE IF NOT EXISTS tarefas (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					id_estoria INTEGER,
					nome TEXT,
					descricao TEXT);"""

tabelaUsuarios = """CREATE TABLE IF NOT EXISTS usuarios (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					id_equipe INTEGER,
					nome TEXT)"""

tabelaEquipes = """CREATE TABLE IF NOT EXISTS equipes (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					nome TEXT,
					descricao TEXT)"""


def createTables():
    global conexao

    c = conexao.cursor()

    c.execute(tabelaEstorias)
    c.execute(tabelaTarefas)
    c.execute(tabelaUsuarios)
    c.execute(tabelaEquipes)

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


def selectAll(tabela, id):

    command = "SELECT * FROM {a} WHERE id = {b};"
    command = command.format(a=tabela, b=id)
    return executeQuery(command)


def deleteByID(tabela, id):

    command = "DELETE FROM {a} WHERE id = {b};"
    command = command.format(a=tabela, b=id)
    executeNonQuery(command)


def inicializaBanco():
    global conexao, proxEstoriaID, proxTarefaID, proxUsuarioID, proxEquipeID

    conexao = sqlite3.connect('engsoft.db')
    createTables()

    proxEstoriaID = countQuery('estorias') + 1
    proxTarefaID = countQuery('tarefas') + 1
    proxUsuarioID = countQuery('usuarios') + 1
    proxEquipeID = countQuery('equipes') + 1


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


def insertUsuario(id_equipe, nome):
    global proxUsuarioID

    command = "INSERT INTO usuarios(id_equipe, nome) VALUES ({a}, '{b}');"
    command = command.format(a=id_equipe, b=nome)
    executeNonQuery(command)

    proxUsuarioID = proxUsuarioID + 1


def updateUsuario(id, id_equipe, nome):

    command = "UPDATE usuarios SET id_equipe = {a}, nome = '{b}' WHERE id = {c};"
    command = command.format(a=id_equipe, b=nome, c=id)
    executeNonQuery(command)


def insertTarefa(nome, descricao):
    global proxEquipeID

    command = "INSERT INTO equipes(nome, descricao) VALUES ('{a}', '{b}');"
    command = command.format(a=nome, b=descricao)
    executeNonQuery(command)

    proxEquipeID = proxEquipeID + 1


def updateTarefa(id, nome, descricao):

    command = "UPDATE equipes SET nome = '{a}', descricao = '{b}' WHERE id = {c};"
    command = command.format(a=nome, b=descricao, c=id)
    executeNonQuery(command)
