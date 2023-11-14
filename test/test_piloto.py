import unittest
import xmlrunner
import os
import sys

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
    def test_email_valido(self):
        self.assertIn('.com.br',self.piloto.email)
    

if __name__ == 'main':
    with open('.\\artefact\\results.xml', 'wb') as output:
        unittest.main(
            testRunner=output,
            failfast=False, buffer=False, catchbreak=False)