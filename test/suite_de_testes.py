import unittest
from test_piloto import TestPiloto
suite = unittest.TestSuite()

siteDeTeste = unittest.TestLoader().loadTestsFromTestCase(TestPiloto)

suite.addTest(siteDeTeste)

runner = unittest.TextTestRunner()
runner.run(suite)