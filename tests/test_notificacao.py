import unittest
from datetime import datetime, timedelta
from src.usuario import Usuario
from src.livro import Livro
from src.notificacao import NotificacaoAtraso

class TestNotificacaoAtraso(unittest.TestCase):
    def setUp(self):
        self.usuario = Usuario("João")
        self.livro = Livro("Python Clean Code", "Robert Martin")

    def test_livro_em_dia_nao_gera_notificacao(self):
        data_emprestimo = datetime.now().date() - timedelta(days=3)
        notificacao = NotificacaoAtraso(self.usuario, self.livro, data_emprestimo)
        self.assertFalse(notificacao.esta_atrasado())
        self.assertIsNone(notificacao.gerar_mensagem())

    def test_livro_atrasado_gera_notificacao(self):
        data_emprestimo = datetime.now().date() - timedelta(days=10)
        notificacao = NotificacaoAtraso(self.usuario, self.livro, data_emprestimo)
        self.assertTrue(notificacao.esta_atrasado())
        self.assertIsNotNone(notificacao.gerar_mensagem())
        self.assertIn("está atrasado", notificacao.gerar_mensagem())

    def test_gerar_mensagem_para_livro_em_dia(self):
        data_emprestimo = datetime.now().date() - timedelta(days=2)
        notificacao = NotificacaoAtraso(self.usuario, self.livro, data_emprestimo)
        mensagem = notificacao.gerar_mensagem()
        self.assertIsNone(mensagem)

    def test_livro_sem_data_emprestimo_nao_gera_atraso(self):
        notificacao = NotificacaoAtraso(self.usuario, self.livro, None)
        self.assertFalse(notificacao.esta_atrasado())
        self.assertIsNone(notificacao.gerar_mensagem())

    def test_atraso_com_limite_personalizado(self):
        data_emprestimo = datetime.now().date() - timedelta(days=5)
        notificacao = NotificacaoAtraso(self.usuario, self.livro, data_emprestimo, dias_limite=3)
        self.assertTrue(notificacao.esta_atrasado())
        self.assertIsNotNone(notificacao.gerar_mensagem())
        self.assertIn("está atrasado", notificacao.gerar_mensagem())
