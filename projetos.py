import banco

class Projeto():
    def __init__(self, nome, id_projeto=None):
        self.nome = nome

        if id is None:
            self.id_projeto = banco.proxProjetoID
        else:
            self.id_projeto = id_projeto


    def insertProjetoBanco(self):
        try:
            banco.insertProjeto(self.nome)
            return True

        except Exception as e:
            #raise e
            return False

    def updateProjetoBanco(self):
        try:
            banco.updateProjeto(
                self.id_projeto,
                self.nome,
            )
            return True

        except BaseException:
            return False

    def deleteBanco(self):
        try:
            banco.deleteByID("projetos", self.id_projeto)
            return True

        except BaseException:
            return False

    def changeName(self,name):
        self.name = name
        self.updateBanco()

