import unittest
import estorias
import time
import banco
from sqlite3 import OperationalError
import security
import interface
import tkinter as tk
import LoginScreen
import ProjectScreen

class TestMethods(unittest.TestCase):


	def setUp(self):
		pass





	# Teste10  COMENTAR TESTE 4
	# Comentar o comando createTables() do arquivo banco.py linha 132
	
	def test_createTables(self):
		with self.assertRaises(OperationalError):
			banco.inicializaBanco()				

		banco.createTables()
		banco.inicializaBanco()


	# Teste1
	def test_changeDescricao_estoria(self):
		a = estorias.Estoria("teste1","rodolfo",50)
		self.assertFalse("rodolfa" == a.descricao)
		self.assertTrue("rodolfo" == a.descricao)
		a.changeDescricao("rodolfa")
		self.assertFalse("rodolfo" == a.descricao)
		self.assertTrue("rodolfa" == a.descricao)

	# Teste2
	def test_changeName_estoria(self):
		b = estorias.Estoria("teste2","irrelevante",50)
		self.assertFalse("teste1" == b.nome)
		self.assertTrue("teste2" == b.nome)
		b.changeName("teste3")
		self.assertFalse("teste2" == b.nome)
		self.assertTrue("teste3" == b.nome)
	# Teste3
	def test_changeStoryPoints_estoria(self):

		c = estorias.Estoria("irrelevante","irrelevante",20)
		self.assertTrue(-1 == c.story_points)
		c.changeSP(24)
		self.assertEqual(24,c.story_points)


	# Teste4
	# Precisa comentar a funcao inicializaBanco na LoginScreen.py linha 23
	# Banco testado vazio
	def test_inicializaBanco(self):
		with self.assertRaises(AttributeError):
			lista = banco.executeQuery("SELECT * FROM tarefas;")

		banco.inicializaBanco()

		with self.assertRaises(AssertionError):
			with self.assertRaises(AttributeError):
				lista = banco.executeQuery("SELECT * FROM tarefas;")


	#Banco vazio
	#Teste5
	def test_inicializaID_banco(self):
		banco.inicializaBanco()
		self.assertEqual(banco.proxEstoriaID,1)
		self.assertEqual(banco.proxTarefaID,1)
		self.assertEqual(banco.proxUsuarioID,1)

	#Teste6
	def test_insertEstoria(self):
		banco.insertEstoria(27,"estoriaTeste","descricaoTeste",20)
		lista = banco.executeQuery("SELECT id_projeto,nome,descricao,story_points FROM estorias WHERE id_projeto = 27;")
		self.assertTrue(lista[0][0] == 27)
		self.assertTrue(lista[0][1] == "estoriaTeste")
		self.assertTrue(lista[0][2] == "descricaoTeste")
		self.assertTrue(lista[0][3] == 20)

	#Teste7
	def test_updateEstoria(self):

		banco.updateEstoria(1,"estoriaTesteModificado","descricaoTesteModificada",21)
		lista = banco.executeQuery("SELECT id_projeto,nome,descricao,story_points FROM estorias WHERE id_projeto = 27;")
		self.assertTrue(lista[0][0] == 27)
		self.assertTrue(lista[0][1] == "estoriaTesteModificado")
		self.assertTrue(lista[0][2] == "descricaoTesteModificada")
		self.assertTrue(lista[0][3] == 21)


	#Teste8
	def test_insertTarefa(self):
		banco.insertTarefa(35,"tarefaTeste","descricaoTeste",False)
		lista = banco.executeQuery("SELECT id_estoria,nome,descricao,done FROM tarefas WHERE id_estoria = 35;")
		self.assertTrue(lista[0][0] == 35)
		self.assertTrue(lista[0][1] == "tarefaTeste")
		self.assertTrue(lista[0][2] == "descricaoTeste")
		self.assertTrue(lista[0][3] == 0)

	#Teste9
	def test_updateTarefa(self):
		banco.updateTarefa(1,35,"tarefaTesteModificada","descricaoTesteModificada",True)
		lista = banco.executeQuery("SELECT * FROM tarefas WHERE id_estoria = 35;")
		self.assertTrue(lista[0][1] == 35)
		self.assertTrue(lista[0][2] == "tarefaTesteModificada")
		self.assertTrue(lista[0][3] == "descricaoTesteModificada")
		self.assertTrue(lista[0][4] == 1)

	#Teste11 - checar se as 3 telas foram previamente carregadas na 
	# inicializacao do programa e se eleas sao distintas
	def test_frameLoading(self):
		app = interface.Application()
		self.assertEqual(len(app.frames),3)

	#Teste12 - checar a inicializacao do projeto
	def test_projectsNameAndIDInitialization(self):
		page = ProjectScreen.ProjectPage(0,0)
		page.initializeProject(0,12,"projetoTeste")
		self.assertFalse(page.project_name == "projetoTestes")
		self.assertTrue(page.project_name == "projetoTeste")
		self.assertEqual(page.project_id, 12)
		self.assertFalse(page.project_id == 10)

	#Teste13
	def test_projectsLoadingStories(self):

		banco.insertEstoria(25,"estoriaTeste1","descricaoTeste",2)
		banco.insertEstoria(25,"estoriaTeste2","descricaoTeste",4)
		banco.insertEstoria(24,"estoriaTeste3","descricaoTeste",8)
		page = ProjectScreen.ProjectPage(0,0)
		page.initializeProject(0,25,"projetoTeste")
		self.assertEqual(page.testeEstorias[0][2],"estoriaTeste1")
		self.assertEqual(page.testeEstorias[1][2],"estoriaTeste2")
		self.assertEqual(len(page.testeEstorias),2)

	#Teste14
	def test_projectsLoadingTasks(self):
		banco.insertTarefa(1,"tarefaTeste1","descricaoTeste1",False)
		banco.insertTarefa(2,"tarefaTeste2","descricaoTeste2",False)
		banco.insertTarefa(2,"tarefaTeste3","descricaoTeste3",False)
		page = ProjectScreen.ProjectPage(0,0)
		page.initializeProject(0,25,"projetoTeste")
		self.assertEqual(str(page.testeTarefas[0][2]),"tarefaTeste2")
		self.assertEqual(str(page.testeTarefas[1][2]),"tarefaTeste3")

if __name__ == '__main__':
	unittest.main()