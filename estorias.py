import banco
import tarefas

class Estoria():
    def __init__(self, nome, descricao,id_projeto, story_points=-1, id_estoria=None):
        self.nome = nome
        self.descricao = descricao
        self.story_points = story_points
        self.id_projeto = id_projeto

        if id is None:
            self.id_estoria = banco.proxEstoriaID
        else:
            self.id_estoria = id_estoria


    def insertBanco(self):
        try:
            banco.insertEstoria(self.nome, self.descricao, self.story_points,self.id_projeto)
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
                self.story_points,
                self.id_projeto)
            return True

        except BaseException:
            return False

    def deleteBanco(self):
        try:
            banco.deleteByID("estorias", self.id_estoria)
            return True

        except BaseException:
            return False

    def changeDescricao(self,descricao):
        self.descricao = descricao
        self.updateBanco()

    def changeName(self,name):
        self.nome = name
        self.updateBanco()

    def changeSP(self,sp):
        self.story_points = sp
        self.updateBanco()

    def getTarefas(self):
        command = "SELECT T.nome FROM tarefas T JOIN estorias E ON T.id_estoria = E.(a) VALUES ({a});"
        command = command.format(a=self.id_estoria)
        banco.executeQuery(command)