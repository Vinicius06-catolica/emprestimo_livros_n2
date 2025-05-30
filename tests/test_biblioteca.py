import unittest
from src.biblioteca import Biblioteca

class TestCriacaoBiblioteca(unittest.TestCase):
    def test_criar_biblioteca(self):
        biblioteca = Biblioteca()
        self.assertEqual(biblioteca.livros, [])
        self.assertEqual(biblioteca.usuarios, [])
