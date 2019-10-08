import banco

class Usuario(object):

	def __init__(self, id_equipe , id_usuario ,nome, id = None):
	
		if id is None:
			self.id = banco.proxUsuarioID
		else:
			self.id = id

		self.id_equipe = id_equipe
		self.id_usuario = id_usuario
		self.nome = nome


	def insertUsuarioBanco(self):
	 
		try:

			banco.insertUsuario(self.id_usuario, self.nome)
			return True

		except  Exception as e:
			#raise e
			return False

	def updateUsuarioBanco(self):

		try:

			banco.updateUsuario(self.id,self.id_usuario ,self.nome)
			return True

		except:
			return False

	def deleteUsuarioBanco(self):
		try:
			
			banco.deleteUsuario(self.id)
			return True
		except:
			return False

	def changeUsuarioName(self,nome):
		self.nome = nome
		self.updateUsuarioBanco()