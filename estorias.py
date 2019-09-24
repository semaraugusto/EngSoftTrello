import banco

class Estoria():
    def __init__(self, nome, descricao, story_points=-1, id_estoria=None):
        if id is None:
            self.id_estoria = banco.proxEstoriaID
        else:
            self.id_estoria = id_estoria

        self.nome = nome
        self.descricao = descricao
        self.story_points = story_points

    def insertBanco(self):
        try:
            banco.insertEstoria(self.nome, self.descricao, self.story_points)
            return True

        except Exception as e:
            #raise e
            return False

    def updateBanco(self):
        try:
            banco.updateEstoria(
                self.id_estoria,
                self.nome,
                self.descricao,
                self.story_points)
            return True

        except BaseException:
            return False

    def deleteBanco(self):
        try:
            banco.deleteByID("estorias", self.id_estoria)
            return True

        except BaseException:
            return False

    
