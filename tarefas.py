import banco

class Tarefa(object):

	def __init__(self, id_estoria, nome, descricao,done, id = None):
	
		if id is None:
			self.id = banco.proxTarefaID
		else:
			self.id = id

		self.id_estoria = id_estoria
		self.nome = nome
		self.descricao = descricao
		self.done = done

	def insertTarefaBanco(self):
	 
		try:

			banco.insertTarefa(self.id_estoria, self.nome, self.descricao,self.done)
			return True

		except  Exception as e:
			#raise e
			return False

	def updateTarefaBanco(self):

		try:

			banco.updateTarefa(self.id,self.id_estoria ,self.nome, self.descricao,self.done)
			return True

		except:
			return False

	def deleteTarefaBanco(self):

		try:
			
			banco.deleteByID("tarefas", self.id)

			return True
		except:
			return False