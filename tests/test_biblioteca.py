import unittest
from src.biblioteca import Biblioteca
from src.livro import Livro
from src.usuario import Usuario

class TestCriacaoBiblioteca(unittest.TestCase):
    def test_criar_biblioteca(self):
        biblioteca = Biblioteca()
        self.assertEqual(biblioteca.livros, [])
        self.assertEqual(biblioteca.usuarios, [])

class TestEmprestimoLivro(unittest.TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()
        self.livro = Livro("1984", "George Orwell")
        self.usuario = Usuario("Winston Smith")
        self.biblioteca.adicionar_livro(self.livro)
        self.biblioteca.adicionar_usuario(self.usuario)

    def test_emprestar_livro_valido(self):
        self.biblioteca.emprestar_livro("Winston Smith", "1984")
        self.assertTrue(self.livro.emprestado)
        self.assertIn(self.livro, self.usuario.livros_emprestados)

    def test_emprestar_livro_inexistente(self):
        with self.assertRaises(ValueError):
            self.biblioteca.emprestar_livro("Winston Smith", "Livro Inexistente")

    def test_emprestar_livro_com_usuario_inexistente(self):
        with self.assertRaises(ValueError):
            self.biblioteca.emprestar_livro("Vinicius Bueno", "Livro Inexistente")

    def test_emprestar_livro_ja_emprestado(self):
        self.biblioteca.emprestar_livro("Winston Smith", "1984")
        with self.assertRaises(ValueError):
            self.biblioteca.emprestar_livro("Winston Smith", "1984")

class TestDevolucaoLivro(unittest.TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()
        self.livro = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
        self.livro2 = Livro("Livro nao emprestado", "Autor desconhecido")
        self.usuario = Usuario("Vini")
        self.biblioteca.adicionar_livro(self.livro)
        self.biblioteca.adicionar_livro(self.livro2)
        self.biblioteca.adicionar_usuario(self.usuario)
        self.biblioteca.emprestar_livro("Vini", "O Senhor dos Anéis")

    def test_devolver_livro_valido(self):
        self.biblioteca.devolver_livro("Vini", "O Senhor dos Anéis")
        self.assertFalse(self.livro.emprestado)
        self.assertNotIn(self.livro, self.usuario.livros_emprestados)

    def test_devolver_livro_nao_emprestado(self):
        with self.assertRaises(ValueError):
            self.biblioteca.devolver_livro("Vini", "Livro nao emprestado")


class TestLimiteEmprestimos(unittest.TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()
        self.usuario = Usuario("Harry Potter")
        self.biblioteca.adicionar_usuario(self.usuario)

        self.livros = [
            Livro("Livro 1", "Autor 1"),
            Livro("Livro 2", "Autor 2"),
            Livro("Livro 3", "Autor 3"),
            Livro("Livro 4", "Autor 4")
        ]
        for livro in self.livros:
            self.biblioteca.adicionar_livro(livro)

    def test_limite_3_emprestimos(self):
        for i in range(3):
            self.biblioteca.emprestar_livro("Harry Potter", f"Livro {i + 1}")

        with self.assertRaises(ValueError):
            self.biblioteca.emprestar_livro("Harry Potter", "Livro 4")

    def test_devolver_e_emprestar_novamente(self):
        for i in range(3):
            self.biblioteca.emprestar_livro("Harry Potter", f"Livro {i + 1}")

        self.biblioteca.devolver_livro("Harry Potter", "Livro 1")
        self.biblioteca.emprestar_livro("Harry Potter", "Livro 4")

        self.assertEqual(len(self.usuario.livros_emprestados), 3)
        titulos = [livro.titulo for livro in self.usuario.livros_emprestados]
        self.assertNotIn("Livro 1", titulos)
        self.assertIn("Livro 4", titulos)
