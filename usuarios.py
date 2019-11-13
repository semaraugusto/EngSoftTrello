import banco

class Usuario(object):

    def __init__(self, id_equipe, nome, senha, id_usuario = None):
        if id_usuario is None:
            self.id_usuario = banco.proxUsuarioID
        else:
            self.id_usuario = id_usuario

        self.id_equipe = id_equipe
        self.nome = nome
        self.senha = senha


    def insertBanco(self):
        try:
            banco.insertUsuario(self.nome, self.senha, self.id_equipe)
            return True

        except Exception as e:
            #raise e
            return False

    def updateBanco(self):
        banco.updateUsuario(self.id_usuario, self.nome)
        return True

        # except:
        #     return False

    def deleteBanco(self):
        banco.deleteByID("usuarios", self.id_usuario)

    def changeName(self, nome):
        self.nome = nome
        self.updateBanco()
        return self
