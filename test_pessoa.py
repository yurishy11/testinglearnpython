"""
class Pessoa
    __init__
        nome str
        sobrenome str
        dados_obtidos bool (inicia False)
    
    API:
        obter_todos_os_dados -> method
            OK
            404

            (dados_obtidos True se dados obtidos com sucesso)
"""
import unittest
from unittest.mock import patch
from Pessoa import Pessoa


class TestPessoa(unittest.TestCase):
    def setUp(self):
        # Sera executado antes de cada teste
        self.p1 = Pessoa('Luiz', 'Felipe')
        self.p2 = Pessoa('Maria', 'Maria')

    def test_pessoa_attr_nome_possui_o_valor_correto(self):
        self.assertEqual(self.p1.nome, 'Luiz')
        self.assertEqual(self.p2.nome, 'Maria')

    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.p1.nome, str)
        self.assertIsInstance(self.p2.nome, str)

    def test_pessoa_attr_sobrenome_possui_o_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Felipe')
        self.assertEqual(self.p2.sobrenome, 'Maria')
    
    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)
        self.assertIsInstance(self.p2.sobrenome, str)

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obtidos)
        self.assertFalse(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_OK(self):
        # Simulação
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), "CONECTADO")
            self.assertTrue(self.p1.dados_obtidos)
            self.assertEqual(self.p2.obter_todos_os_dados(), "CONECTADO")
            self.assertTrue(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_404(self):
        # Simulação
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), "ERRO 404")
            self.assertFalse(self.p1.dados_obtidos)
            self.assertEqual(self.p2.obter_todos_os_dados(), "ERRO 404")
            self.assertFalse(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_e_falha_sequencial(self):
        # Simulação
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), "CONECTADO")
            self.assertTrue(self.p1.dados_obtidos)
            self.assertEqual(self.p2.obter_todos_os_dados(), "CONECTADO")
            self.assertTrue(self.p2.dados_obtidos)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), "ERRO 404")
            self.assertFalse(self.p1.dados_obtidos)
            self.assertEqual(self.p2.obter_todos_os_dados(), "ERRO 404")
            self.assertFalse(self.p2.dados_obtidos)

if __name__ == "__main__":
    unittest.main(verbosity=2)