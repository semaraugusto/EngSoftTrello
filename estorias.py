import banco

class Estoria(object):

	def __init__(self, nome, descricao, story_points = -1):
	
		self.id = banco.proxEstoriaID
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

	def deleteEstoria(self):

		banco = Banco()
		try:

			c = banco.conexao.cursor()

			c.execute("delete from estorias where idusuario = " + self.idestoria + " ")

			banco.conexao.commit()
			c.close()

			return "estoria excluída com sucesso!"
		except:
			return "Ocorreu um erro na exclusão da estoria"

	def selectEstoria(self, idusuario):
		banco = Banco()
		try:

			c = banco.conexao.cursor()

			c.execute("select * from usuarios where idestoria = " + idestoria + "  ")

			for linha in c:
				self.idestoria = linha[0]
				self.nome = linha[1]
				self.descricao = linha[2]
				self.sp = linha[3]

			c.close()

			return "Busca feita com sucesso!"
		except:
			return "Ocorreu um erro na busca da estoria"