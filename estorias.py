class Estorias(object):


	def __init__(self, idestoria = 0, nome = "", descricao = "",  sp = "")
	  self.info = {}
	  self.idestoria = idestoria
	  self.nome = nome
	  self.descricao = descricao
	  self.sp = sp

	def insertEstoria(self):
	 
		banco = Banco()
		try:

		  c = banco.conexao.cursor()

		  c.execute("insert into estorias (nome,descricao,sp) values ('" + self.nome + "', '" + self.descricao + "', '" + self.sp +"' )")

		  banco.conexao.commit()
		  c.close()

		  return "Estoria cadastrada com sucesso!"
		except:
		  return "Ocorreu um erro no cadastro da estoria"

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