import unittest
import os
import banco
from security import *
from usuarios import Usuario
from projetos import Projeto
from ProjectScreen import ProjectPage
from equipes import Equipe

class Tests(unittest.TestCase):
    def setUp(self):
        if os.path.exists("engsoft.db"):
            os.remove("engsoft.db")

        banco.inicializaBanco()

    # Test 1
    def test_user_constructor(self):
        user = Usuario(0, 'nome', 'senha', 15)
        self.assertTrue(user.id_equipe == 0)
        self.assertTrue(user.nome == 'nome')
        self.assertTrue(user.senha == 'senha')
        self.assertTrue(user.id_usuario == 15)

    # Test 2
    def test_user_changeName(self):
        user = Usuario(1, 'user', '1')
        self.assertTrue(user.nome == 'user')
        user.changeName("new_name")
        self.assertTrue(user.nome == 'new_name')

    # Test 3
    def test_user_insertBanco(self):
        pwd = "senha123"
        hashed_pwd = criptografaSenha(pwd)

        user = Usuario(1, 'user', pwd, 15)
        user.insertBanco()
        query = banco.selectAll('usuarios')
        expected = [(1, 1, 'user', hashed_pwd)]
        self.assertTrue(expected[0][0] == query[0][0])
        self.assertTrue(expected[0][1] == query[0][1])
        self.assertTrue(expected[0][2] == query[0][2])
        self.assertTrue(verificaSenha(query[0][3], pwd))

    # Test 4
    def test_user_updateBanco(self):
        pwd = "senha123"
        hashed_pwd = criptografaSenha(pwd)

        user = Usuario(1, 'user', pwd, 15)
        self.assertTrue(user.insertBanco())
        user = user.changeName('new_name')
        user.insertBanco()

        query = banco.selectAll('usuarios')
        user.updateBanco()
        expected = [(1, 1, 'new_name', hashed_pwd)]
        self.assertTrue(expected[0][0] == query[0][0])
        self.assertTrue(expected[0][1] == query[1][1])
        self.assertTrue(expected[0][2] == query[1][2])
        self.assertTrue(verificaSenha(query[1][3], pwd))

    # Test 5
    def test_user_deleteBanco(self):
        user = Usuario(1, 'user', '1', 15)
        user.deleteBanco()
        query = banco.selectAll('usuarios')
        expected = []
        self.assertTrue(len(query) == 0)

    # Test 6
    def test_criptography(self):
        pwd = "senhaExtremamenteDificilDeQuebrar"
        hashed_pwd = criptografaSenha(pwd)
        self.assertTrue(verificaSenha(hashed_pwd, pwd))
        not_pwd = 'senhaFacil'
        self.assertFalse(verificaSenha(hashed_pwd, not_pwd))

    # Test 7
    def test_projeto_constructor(self):
        proj = Projeto('projeto', 10, 15)
        self.assertTrue(proj.nome == 'projeto')
        self.assertTrue(proj.id_equipe == 10)
        self.assertTrue(proj.id_projeto == 15)


    # Test 8
    def test_projeto_insertBanco(self):
        proj = Projeto('projeto', 10, 15)
        proj.insertBanco()
        query = banco.selectAll('projetos')
        expected = [(1, 10, 'projeto')]
        self.assertTrue(expected == query)

    # Test 9
    def test_projetoDeleteBanco(self):
        proj = Projeto('projeto', 10, 15)
        proj.deleteBanco()
        query = banco.selectAll('projetos')
        self.assertTrue(len(query) == 0)

    # Test 10
    def test_projeto_changeName(self):
        proj = Projeto('projeto', 10, 15)
        self.assertTrue(proj.nome == 'projeto')
        self.assertTrue(proj.id_equipe == 10)
        self.assertTrue(proj.id_projeto == 15)
        proj = proj.changeName('outro_projeto')
        self.assertTrue(proj.nome == 'outro_projeto')
        self.assertTrue(proj.id_equipe == 10)
        self.assertTrue(proj.id_projeto == 15)

    # Test 11
    def test_projectScreen_defineProjectName(self):
        projScreen = ProjectPage(0, 0)
        projScreen.initializeProject(0, 12, 'teste')
        projScreen.defineProjectName("projName")
        self.assertTrue(projScreen.project_name == 'projName')

    # Test 12
    def test_projectScreen_getStoryIndex(self):
        banco.insertEstoria(0, 'estoria', 'desc', 8)
        page = ProjectPage(0, 0)
        page.initializeProject(0, 12, 'teste')

        self.assertTrue(page.getStoryIndex('estoria') == 0)

    # Test 13
    def test_equipe_constructor(self):
        equipe = Equipe(20, 'equipe', 0)
        self.assertTrue(equipe.id_equipe == 20)
        self.assertTrue(equipe.nome == 'equipe')
        self.assertTrue(equipe.id == 0)

    # Test 14
    def test_equipe_insertBanco(self):
        equipe = Equipe(20, 'equipe', 10)
        equipe.insertEquipeBanco()
        query = banco.selectAll('equipes')
        expected = [(20, 'equipe')]
        self.assertTrue(expected == query)

    # Test 15
    def test_equipe_deleteBanco(self):
        equipe = Equipe(20, 'equipe', 10)
        equipe.insertEquipeBanco()
        equipe.deleteBanco()
        query = banco.selectAll('equipes')
        expected = []
        self.assertTrue(expected == query)

if __name__ == '__main__':
    unittest.main()
