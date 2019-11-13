import unittest
import os
import banco
from equipes import *
from projetos import *
from InitialScreen import *
from interface import *
from security import *

class Tests(unittest.TestCase):

    def setUp(self):
        if os.path.exists("engsoft.db"):
            os.remove("engsoft.db")
        banco.inicializaBanco()

    # teste 1
    def teste_projeto_update_banco(self):
        proj = Projeto('projeto', 10, 1)
        proj.insertBanco()
        proj.changeName("projeto_changed")
        query = banco.selectAll('projetos')
        expected = [(1, 10, 'projeto_changed')]
        self.assertTrue(expected == query)

    # teste 2
    def teste_initial_screen_constructor(self):
        app = Application()
        initial_page = app.frames[InitialPage]
        option_assert_1 = initial_page.options_brightness == "Black"
        option_assert_2 = initial_page.options_colour == "#0A6450"
        option_assert_3 = initial_page.options_count == 2

        # creating options avaiable
        self.assertTrue(option_assert_1)
        self.assertTrue(option_assert_2)
        self.assertTrue(option_assert_3)

    # teste 3
    def teste_initial_screen_create_option(self):
        app = Application()
        initial_page = app.frames[InitialPage]
        initial_page.createOption(initial_page, "Create new project", initial_page.createNewProject)
        self.assertTrue(initial_page.options_count == 3)

    # teste 4
    def teste_initial_screen_set_user_id(self):
        app = Application()
        initial_page = app.frames[InitialPage]
        initial_page.set_user_id(15)
        self.assertTrue(initial_page.user_id == 15)

    # teste 5
    def teste_project_screen_create_listbox(self):
        page = ProjectPage(0,0)
        page.initializeProject(0,12,"projetoTeste")
        page.createListBox(page, [], "teste", 3, 0, "tes{}: ")
        self.assertTrue(len(page.list_boxes) == 5)

    # teste 6
    def teste_banco_confirma_login(self):
        banco.insertUsuario("tiago", "senha", 0)
        self.assertTrue(banco.confirmaLogin("tiago", "senha"))
        self.assertFalse(banco.confirmaLogin("tiago", "senhaFalsa"))
    
    # teste 7
    def teste_banco_get_by_id(self):
        banco.insertUsuario("tiago", "senha", 0)
        query = banco.getById('usuarios', "tiago")
        expected = [(1,)]
        self.assertTrue(query == expected)

    # teste 8
    def teste_banco_insert_projeto(self):
        banco.insertProjeto("ProjetoBacana", 1)
        query = banco.selectAll('projetos')
        expected = [(1, 1, "ProjetoBacana")]
        self.assertTrue(query == expected)

    # teste 9
    def teste_banco_update_projeto(self):
        banco.insertProjeto("ProjetoInalterado", 1)
        banco.updateProjeto(1, "ProjetoAlterado")
        query = banco.selectAll('projetos')
        unchanged = [(1, 1, "ProjetoInalterado")]
        expected = [(1, 1, "ProjetoAlterado")]
        self.assertFalse(query == unchanged)
        self.assertTrue(query == expected)


    # teste 10
    def teste_banco_insert_usuario(self):
        banco.insertUsuario("tiago", "senha", 1)
        command = "SELECT id, id_equipe, nome FROM usuarios"
        query = banco.executeQuery(command)
        expected = [(1, 1, "tiago")]
        self.assertTrue(query == expected)

    # teste 11
    def teste_banco_update_usuario(self):
        banco.insertUsuario("tiago", "senha", 1)
        banco.updateUsuario(1, "tiagoNO")
        command = "SELECT id, id_equipe, nome FROM usuarios"
        query = banco.executeQuery(command)
        expected = [(1, 1, "tiagoNO")]
        self.assertTrue(query == expected)

    # teste 12
    def teste_banco_select_id(self):
        banco.insertUsuario("tiago", "senha", 1)
        query = banco.selectID('usuarios', 'tiago')
        expected = [(1, )]
        self.assertTrue(query == expected)

    # teste 13
    def teste_banco_select_all_by_id(self):
        banco.insertProjeto("Projeto", 1)
        query = banco.selectAllbyID('projetos', 1)
        expected = [(1, 1, "Projeto")]
        self.assertTrue(query == expected)

    # teste 14
    def teste_banco_delete_by_id(self):
        banco.insertProjeto("Projeto", 1)
        banco.insertProjeto("Projeto2", 1)
        query = banco.deleteByID('projetos', 1)
        query = banco.selectAll('projetos')
        wrong_delete = [(1, 1, "Projeto")]
        not_delete = [(1, 1, "Projeto"), (2, 1, "Projeto2")]
        expected = [(2, 1, "Projeto2")]
        self.assertTrue(query == expected)
        self.assertFalse(query == not_delete)
        self.assertFalse(query == wrong_delete)

    # teste 15
    def teste_banco_count_query(self):
        banco.insertProjeto("Projeto", 1)
        banco.insertProjeto("Projeto2", 1)
        banco.insertProjeto("Projeto3", 1)
        banco.insertProjeto("Projeto4", 1)
        count = banco.countQuery('projetos')
        expected = 4
        self.assertTrue(count == expected)


if __name__ == '__main__':
    unittest.main()

