from datetime import datetime

class NotificacaoAtraso:
    def __init__(self, usuario, livro, data_emprestimo, dias_limite=7):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.dias_limite = dias_limite

    def esta_atrasado(self):
        if not self.data_emprestimo:
            return False
        data_atual = datetime.now().date()
        dias_passados = (data_atual - self.data_emprestimo).days
        return dias_passados > self.dias_limite

    def gerar_mensagem(self):
        if self.esta_atrasado():
            return f"Atenção: {self.usuario.nome}, o livro '{self.livro.titulo}' está atrasado!"
        return None
