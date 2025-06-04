class Livro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False
        self.data_emprestimo = None

