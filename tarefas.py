import banco

class Tarefa(object):
    def __init__(self, id_estoria, nome, descricao, done, id_equipe=None, id_tarefa=None, comments=None):
        self.id_estoria = id_estoria
        self.nome = nome
        self.descricao = descricao
        self.done = done
        self.id_equipe = id_equipe

        if id_tarefa is None:
            self.id_tarefa = banco.proxTarefaID
        else:
            self.id_tarefa = id_tarefa

        self.comments=comments


    def insertTarefaBanco(self):
        try:
            banco.insertTarefa(
                self.id_estoria,
                self.nome,
                self.descricao,
                self.done,
                self.id_equipe,
                self.comments)
            return True

        except Exception as e:
            #raise e
            return False

    def updateTarefaBanco(self):

        try:
            banco.updateTarefa(
                self.id_tarefa,
                self.id_estoria,
                self.nome,
                self.descricao,
                self.done,
                self.id_equipe,
                self.comments)
            return True

        except BaseException:
            return False

    def deleteTarefaBanco(self):

        try:
            banco.deleteByID("tarefas", self.id_tarefa)
            return True

        except BaseException:
            return False

    def changeDescricao(self,descricao):
        self.descricao = descricao
        self.updateTarefaBanco()

    def changeName(self,name):
        self.name = name
        self.updateTarefaBanco()

    def setDone(self,boolean){
        self.done = boolean
        updateTarefaBanco()
    }