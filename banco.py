import sqlite3
class Banco():


	def __init__(self):
		self.conexao = sqlite3.connect('engsoft.db')
		self.createTable()

	def createTable(self):
		c = self.conexao.cursor()

		c.execute("""create table if not exists estorias (
					idestoria integer primary key autoincrement ,
					nome text,
					descricao text,
					sp text)""")
		self.conexao.commit()
		c.close()
