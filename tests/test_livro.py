import unittest
from src.livro import Livro

class TestCriacaoLivro(unittest.TestCase):
    def test_criar_livro(self):
        livro = Livro("O Hobbit", "J.R.R. Tolkien")
        self.assertEqual(livro.titulo, "O Hobbit")
        self.assertEqual(livro.autor, "J.R.R. Tolkien")
        self.assertFalse(livro.emprestado)