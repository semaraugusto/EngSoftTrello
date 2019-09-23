import banco

class Equipe(object):

	def __init__(self, id_equipe , nome, id = None):
	
		if id is None:
			self.id = banco.proxEquipeID
		else:
			self.id = id

		self.id_equipe = id_equipe
		self.nome = nome


	def insertEquipeBanco(self):
	 
		try:

			banco.insertEquipe(self.id_equipe, self.nome)
			return True

		except  Exception as e:
			#raise e
			return False

	def updateEquipeBanco(self):

		try:

			banco.updateEquipe(self.id,self.id_equipe ,self.nome)
			return True

		except:
			return False

	def deleteEquipeBanco(self):

		try:
			
			banco.deleteEquipe(self.id)

			return True
		except:
			return False