class Estorias(object):


	def __init__(self, idestoria = 0, nome = "", descricao = "",  sp = "")
	  self.info = {}
	  self.idusuario = idusuario
	  self.nome = nome
	  self.descricao = descricao
	  self.sp = sp

	def insertUser(self):
	 
		banco = Banco()
		try:

		  c = banco.conexao.cursor()

		  c.execute("insert into usuarios (nome,descricao,sp) values ('" + self.nome + "', '" + self.descricao + "', '" + self.sp +"' )")

		  banco.conexao.commit()
		  c.close()

		  return "Estoria cadastrada com sucesso!"
		except:
		  return "Ocorreu um erro na inserção do usuário"