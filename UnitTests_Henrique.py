import unittest
import banco
from estorias import Estoria
from tarefas import Tarefa
from projetos import Projeto
from usuarios import Usuario
import os

class TestMethods(unittest.TestCase):

	def setUp(self):
		if os.path.exists("engsoft.db"):
			os.remove('engsoft.db')

		banco.inicializaBanco()


	#Teste 0
	def teste_banco_selectAll(self):
		banco.insertEstoria(1, "e1", "d1", 20)
		banco.insertTarefa(1, "t1", "d2", False)
		banco.insertTarefa(1, "t2", "d3", False)
		banco.insertEstoria(2, "e2", "d4", 20)
		banco.insertTarefa(2, "t3", "d5", False)

		estoriasReturned = banco.selectAll("estorias")
		tarefasReturned = banco.selectAll("tarefas")

		estoriasExpected = [(1, 1, 'e1', 'd1', 20), (2, 2, 'e2', 'd4', 20)]
		tarefasExpected = [(1, 1, 't1', 'd2', False), (2, 1, 't2', 'd3', False), (3, 2, 't3', 'd5', False)]

		self.assertTrue(estoriasReturned == estoriasExpected and tarefasReturned == tarefasExpected)

	#Teste 1
	def teste_estorias_insertBanco(self):
		e1 = Estoria("e1", "d1", 1)
		e1.insertBanco()

		returned = banco.selectAll("estorias")
		expected = [(1, 1, 'e1', 'd1', -1)]

		self.assertTrue(returned == expected)

	#Teste 2
	def teste_tarefas_insertBanco(self):
		t1 = Tarefa(1, "t1", "d1", False)
		t1.insertBanco()

		returned = banco.selectAll("tarefas")
		expected = [(1, 1, 't1', 'd1', False)]

		self.assertTrue(returned == expected)

	#Teste 3
	def teste_estorias_getTarefas(self):
		e1 = Estoria("e1", "d1", 1)
		t1 = Tarefa(1, "t1", "d2", False)
		t2 = Tarefa(1, "t2", "d3", False)

		e1.insertBanco()
		t1.insertBanco()
		t2.insertBanco()

		returned = e1.getTarefas()
		expected = [('t1',),('t2',)]

		self.assertTrue(returned == expected)

	#Teste 4
	def teste_tarefas_updateBanco(self):
		t1 = Tarefa(1, "t1", "d2", False)
		t1.insertBanco()

		t1.nome = "T1"
		t1.descricao = "D2"
		t1.done = True
		t1.updateBanco()

		returned = banco.selectAll("tarefas")
		self.assertTrue(returned[0][2] == 'T1' and returned[0][3] == 'D2' and returned[0][4])

	#Teste 5
	def teste_tarefas_changeDescricao(self):
		t1 = Tarefa(1, "t1", "d2", False)
		t1.insertBanco()

		t1.changeDescricao("d8")

		self.assertTrue(t1.descricao == "d8")

		command = "SELECT descricao FROM tarefas WHERE id = 1;"
		returned = banco.executeQuery(command)
		self.assertTrue(returned[0][0] == "d8")


	#Teste 6
	def teste_tarefas_setDone(self):
		t1 = Tarefa(1, "t1", "d2", False)
		t1.insertBanco()

		t1.setDone(True)

		self.assertTrue(t1.done)

		command = "SELECT done FROM tarefas WHERE id = 1;"
		returned = banco.executeQuery(command)
		self.assertTrue(returned[0][0])

	#Teste 7
	def teste_tarefas_changeName(self):
		t1 = Tarefa(1, "t1", "d2", False)
		t1.insertBanco()

		t1.changeName("T1")

		self.assertTrue(t1.nome == "T1")

		command = "SELECT nome FROM tarefas WHERE id = 1;"
		returned = banco.executeQuery(command)
		self.assertTrue(returned[0][0] == "T1")

	#Teste 8
	def teste_tarefas_deleteBanco(self):
		t1 = Tarefa(1, "t1", "d2", False)
		t1.insertBanco()

		t1.deleteBanco()

		returned = banco.selectAll("tarefas")
		self.assertTrue(len(returned) == 0)

	#Teste 9
	def teste_estorias_updateBanco(self):
		e1 = Estoria("e1", "d1", 1)
		e1.insertBanco()

		e1.nome = "T1"
		e1.descricao = "D2"
		e1.story_points = 8
		e1.updateBanco()

		returned = banco.selectAll("estorias")
		self.assertTrue(returned[0][2] == 'T1' and returned[0][3] == 'D2' and returned[0][4] == 8)

	#Teste 10
	def teste_estorias_deleteBanco(self):
		e1 = Estoria("e1", "d1", 1)
		e1.insertBanco()

		e1.deleteBanco()

		returned = banco.selectAll("estorias")
		self.assertTrue(len(returned) == 0)

	#Teste 11
	def teste_banco_consultaEstoriasProjeto(self):
		p1 = Projeto("p1")
		p1.insertBanco()
		e1 = Estoria("e1", "d1", 1)
		e1.insertBanco()
		e2 = Estoria("e2", "d2", 1)
		e2.insertBanco()

		returned = banco.consultaEstoriasProjeto(p1.id_projeto)
		expected = [(1, 1, 'e1', 'd1', -1), (2, 1, 'e2', 'd2', -1)]

		self.assertTrue(returned == expected)

	#Teste 12
	def teste_banco_consultaTarefasEstorias(self):
		e1 = Estoria("e1", "d1", 1)
		e1.insertBanco()
		t1 = Tarefa(1, "t1", "d1", False)
		t1.insertBanco()
		t2 = Tarefa(1, "t2", "d2", False)
		t2.insertBanco()

		returned = banco.consultaTarefasEstorias(e1.id_estoria)
		expected = [(1, 1, 't1', 'd1', False), (2, 1, 't2', 'd2', False)]

		self.assertTrue(returned == expected)

	#Teste 13
	def teste_banco_consultaProjetosUsuario(self):
		u1 = Usuario(1, 'u1', '123')
		u1.insertBanco()
		p1 = Projeto('p1')
		p1.insertBanco()
		p2 = Projeto('p2')
		p2.insertBanco()

		command = "INSERT INTO usuarios_projetos VALUES (1, 1),(1, 2);"
		banco.executeNonQuery(command)

		returned = banco.consultaProjetosUsuario(u1.id_usuario)
		expected = [(1, None, 'p1'), (2, None, 'p2')]

		self.assertTrue(returned == expected)


	#Teste 14
	def teste_banco_consultaEstoriaDaTarefa(self):
		e1 = Estoria("e1", "d1", 1)
		e1.insertBanco()
		t1 = Tarefa(1, "t1", "d2", False)
		t1.insertBanco()

		id_estoria_t1 = banco.consultaEstoriaDaTarefa(t1.id_tarefa)
		self.assertTrue(id_estoria_t1[0][0] == 1)

		e2 = Estoria("e2", "d1", 1)
		e2.insertBanco()
		t2 = Tarefa(2, "t2", "d2", False)
		t2.insertBanco()

		id_estoria_t2 = banco.consultaEstoriaDaTarefa(t2.id_tarefa)
		self.assertTrue(id_estoria_t2[0][0] == 2)



if __name__ == '__main__':
	unittest.main()