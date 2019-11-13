import banco

class Projeto():
    def __init__(self, nome, id_equipe = None, id_projeto=None): # semar
        self.nome = nome
        self.id_equipe = id_equipe

        if id_projeto is None:
            self.id_projeto = banco.proxProjetoID
        else:
            self.id_projeto = id_projeto


    def insertBanco(self): # semar
        try:
            banco.insertProjeto(self.nome, self.id_equipe)
            return True

        except Exception as e:
            #raise e
            return False

    def updateBanco(self): # tiago
        # try:
        banco.updateProjeto(
            self.id_projeto,
            self.nome,
        )
        return True
        #
        # except BaseException:
        #     return False

    def deleteBanco(self): # semar
        banco.deleteByID("projetos", self.id_projeto)


    def changeName(self,nome): # semar
        self.nome = nome
        self.updateBanco()
        return self
