class Estoria(object):

	def __init__(self, nome, descricao, story_points = -1):
	
		self.nome = nome
		self.descricao = descricao
		self.story_points = story_points

	def insertBanco(self, banco):
	 
		try:

			command = "INSERT INTO estorias(nome, descricao, story_points) VALUES ('{a}', '{b}', {c});"
			command = command.format(a=self.nome, b=self.descricao, c=self.story_points)
			banco.executeNonQuery(command)

			return True
		except  Exception as e:
			#raise e
			return False

	def updateEstoria(self):

		banco = Banco()
		try:

			c = banco.conexao.cursor()

			c.execute("update estorias set nome = '" + self.nome + "',descricao = '" + self.descricao + "', sp = '" + self.sp + " ")

			banco.conexao.commit()
			c.close()

			return "Estoria atualizada com sucesso!"
		except:
			return "Ocorreu um erro na alteração da estoria"

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