import unittest
from src.usuario import Usuario

class TestCriacaoUsuario(unittest.TestCase):
    def test_criar_usuario(self):
        usuario = Usuario("Frodo Baggins")
        self.assertEqual(usuario.nome, "Frodo Baggins")
        self.assertEqual(usuario.livros_emprestados, [])