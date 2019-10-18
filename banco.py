import sqlite3

conexao = None
proxEstoriaID = 0
proxTarefaID = 0
proxUsuarioID = 0
proxProjetoID = 0

tabelaEstorias = """CREATE TABLE IF NOT EXISTS estorias (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					id_projeto INTEGER,
					nome TEXT,
					descricao TEXT,
					story_points INTEGER);"""

tabelaTarefas = """CREATE TABLE IF NOT EXISTS tarefas (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					id_estoria INTEGER,
					nome TEXT,
					descricao TEXT,
					done BOOLEAN);"""

tabelaUsuarios = """CREATE TABLE IF NOT EXISTS usuarios (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					nome TEXT UNIQUE,
                    senha TEXT)"""

tabelaProjetos = """CREATE TABLE IF NOT EXISTS projetos (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					nome TEXT)"""

tabelaUsuariosProjetos = """CREATE TABLE IF NOT EXISTS usuarios_projetos (
							id_usuario INTEGER ,
							id_projeto INTEGER ,
                            PRIMARY KEY (id_usuario, id_projeto))"""


def createTables():
    global conexao

    c = conexao.cursor()

    c.execute(tabelaEstorias)
    c.execute(tabelaTarefas)
    c.execute(tabelaUsuarios)
    c.execute(tabelaProjetos)
    c.execute(tabelaUsuariosProjetos)

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


def selectAll(tabela):

    command = "SELECT * FROM {a};"
    command = command.format(a=tabela)
    return executeQuery(command)



def selectAllbyID(tabela, id):

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
    proxProjetoID = countQuery('projetos') + 1


def insertEstoria(id_projeto, nome, descricao, story_points):
    global proxEstoriaID

    command = "INSERT INTO estorias(id_projeto,nome, descricao, story_points) VALUES ({a}, '{b}', '{c}', {d});"
    command = command.format(a=id_projeto, b=nome, c=descricao, d=story_points)
    executeNonQuery(command)

    proxEstoriaID = proxEstoriaID + 1


def updateEstoria(id, nome, descricao, story_points):

    command = "UPDATE estorias SET nome = '{a}', descricao = '{b}', story_points = {c} WHERE id = {d};"
    command = command.format(a=nome, b=descricao, c=story_points, d=id)
    executeNonQuery(command)


def insertTarefa(id_estoria, nome, descricao, done, comments):
    global proxTarefaID

    if id_equipe is None:
        id_equipe = "null"
    if comments is None:
        comments = ""
		
    command = "INSERT INTO tarefas(id_estoria, nome, descricao, comments, done) VALUES ({a}, '{b}', '{c}', '{d}', {e});"
    command = command.format(a=id_estoria, b=nome, c=descricao, d=comments, e=done)
    executeNonQuery(command)

    proxTarefaID = proxTarefaID + 1


def updateTarefa(id, id_estoria, nome, descricao, done, comments):

	if id_equipe is None:
		id_equipe = "null"
	if comments is None:
		comments = ""

	command = "UPDATE tarefas SET id_estoria = {a}, nome = '{b}', descricao = '{c}', comments = '{d}', done = {e} WHERE id = {f};"
	command = command.format(a=id_estoria, b=nome, c=descricao, d=comments, e=done, f=id)
	executeNonQuery(command)


def insertUsuario(nome, senha):
    global proxUsuarioID

    command = "INSERT INTO usuarios(nome, senha) VALUES ('{a}', '{b}');"
    command = command.format(a=nome, b=senha)
    executeNonQuery(command)

    proxUsuarioID = proxUsuarioID + 1


def updateUsuario(id, nome):

    command = "UPDATE usuarios SET nome = '{a}' WHERE id = {b};"
    command = command.format(a=nome, b=id)
    executeNonQuery(command)


def insertProjeto(nome):
    global proxProjetoID

    command = "INSERT INTO projetos(nome) VALUES ('{a}');"
    command = command.format(a=nome)
    executeNonQuery(command)

    proxProjetoID += 1


def updateProjeto(id, nome):

    command = "UPDATE projetos SET nome = '{a}' WHERE id = {b};"
    command = command.format(a=nome, b=id)
    executeNonQuery(command)


def getById(tabela, nome):
    command = "SELECT id FROM {a} WHERE nome = '{b}';"
    command = command.format(a=tabela, b=nome)
    print(command)
    return executeQuery(command)


def consultaEstoriasProjeto(id_projeto):

	command = "SELECT * FROM estorias e WHERE e.id_projeto = {a};"
	command = command.format(a=id_projeto)
	return executeQuery(command)

def consultaTarefasEstorias(id_estoria):
	command = "SELECT * FROM tarefas t WHERE t.id_estoria = {a};"
	command = command.format(a=id_estoria)
	return executeQuery(command)



def consultaProjetosUsuario(id_usuario):

	command = "SELECT p.* FROM projetos p JOIN usuarios_projetos up ON p.id = up.id_projeto WHERE up.id_usuario = {a};"
	command = command.format(a=id_usuario)
	return executeQuery(command)


def confirmaLogin(nome, senha):

    command = "SELECT * FROM usuarios WHERE nome = '{a}';"
    command = command.format(a=nome)
    user = executeQuery(command)

    if len(user) == 0:
        return False

    if user[0][2] == senha:
        return True
    else:
        return False