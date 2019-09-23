import banco

class Estoria(object):

	def __init__(self, nome, descricao, story_points = -1, id = None):
	
		if id is None:
			self.id = banco.proxEstoriaID
		else:
			self.id = id

		self.nome = nome
		self.descricao = descricao
		self.story_points = story_points

	def insertBanco(self):
	 
		try:

			banco.insertEstoria(self.nome, self.descricao, self.story_points)
			return True

		except  Exception as e:
			#raise e
			return False

	def updateBanco(self):

		try:

			banco.updateEstoria(self.id, self.nome, self.descricao, self.story_points)
			return True

		except:
			return False

	def deleteBanco(self):

		try:

			banco.deleteByID("estorias", self.id)

			return True
		except:
			return False