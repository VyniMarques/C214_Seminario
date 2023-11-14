import unittest
import xmlrunner
import os
import sys
from unittest.mock import Mock

# Adiciona o diretório "src" ao caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.piloto import Piloto


class TestPiloto(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.piloto = Piloto("João", "Silva", 50000)

    def test_email(self):
        self.assertEqual(self.piloto.email, "João.Silva@email.com.br")

    def test_nome_completo(self):
        self.assertEqual(self.piloto.nome_completo, "João.Silva")

    def test_aumentar_salario(self):
        self.piloto.aumentar_salario()
        self.assertEqual(self.piloto.salario, 50000 * 1.10)

    def test_varificar_se_o_salario_aumentou(self):
        salario_antes = self.piloto.salario
        self.piloto.aumentar_salario()
        self.assertLessEqual(salario_antes,self.piloto.salario)

    @unittest.skip('pulando teste')
    def test_email_valido(self):
        self.assertIn('.com.br',self.piloto.email)

    def test_pilotar_carro(self):
        dict_carro = {'drift.return_value': 'estou fazendo drift', 'lancaerro.side_effect': KeyError}
        carro = Mock(marca='Ferrari', **dict_carro)
        self.assertEqual(self.piloto.drift(carro),'estou fazendo drift' )

    @unittest.expectedFailure
    def test_pilotar_carro_falhando(self):
        dict_carro = {'drift.return_value': 'estou fazendo drift', 'lancaerro.side_effect': KeyError}
        carro = Mock(marca='Ferrari', **dict_carro)
        self.assertEqual(self.piloto.drift(carro),'nao estou fazendo drift' )

    def tearDown(self):
        pass
    

if __name__ == 'main':
    unittest.main(failfast=False, buffer=False, catchbreak=False)