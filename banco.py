import sqlite3

class Banco():

	tabelaEstorias = """CREATE TABLE IF NOT EXISTS estorias (
						id INTEGER PRIMARY KEY AUTOINCREMENT,
						nome TEXT,
						descricao TEXT,
						story_points INTEGER);"""

	def __init__(self):
		self.conexao = sqlite3.connect('engsoft.db')
		self.createTables()

	def createTables(self):
		c = self.conexao.cursor()

		c.execute(self.tabelaEstorias)
		
		self.conexao.commit()
		c.close()

	def executeNonQuery(self, command):
		c = self.conexao.cursor()

		c.execute(command)

		self.conexao.commit()
		c.close()
