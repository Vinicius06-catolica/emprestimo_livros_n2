from src.livro import Livro
from src.usuario import Usuario
from datetime import date

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)

    def adicionar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)

    def _buscar_usuario(self, nome: str) -> Usuario:
        for usuario in self.usuarios:
            if usuario.nome == nome:
                return usuario
        raise ValueError(f"Usuário '{nome}' não cadastrado")

    def _buscar_livro(self, titulo: str) -> Livro:
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        raise ValueError(f"Livro '{titulo}' não encontrado no acervo")

    def emprestar_livro(self, nome_usuario: str, titulo_livro: str):
        usuario = self._buscar_usuario(nome_usuario)
        livro = self._buscar_livro(titulo_livro)

        if livro.emprestado:
            raise ValueError(f"Livro '{titulo_livro}' já está emprestado")

        if len(usuario.livros_emprestados) >= 3:
            raise ValueError("Limite de empréstimos atingido")

        usuario.livros_emprestados.append(livro)
        livro.emprestado = True
        livro.data_emprestimo = date.today()

    def devolver_livro(self, nome_usuario: str, titulo_livro: str):
        usuario = self._buscar_usuario(nome_usuario)
        livro = self._buscar_livro(titulo_livro)

        if livro not in usuario.livros_emprestados:
            raise ValueError("Livro não foi emprestado para este usuário")

        usuario.livros_emprestados.remove(livro)
        livro.emprestado = False
        livro.data_emprestimo = None