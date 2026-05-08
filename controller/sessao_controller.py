from service.sessao_service import SessaoService


class SessaoController:
    def __init__(self, view):
        self.service = SessaoService()
        self.view = view

    def cadastrar_sessao(self):
        filme_id, cinema_id, horario, sala = self.view.obter_dados_sessao()
        try:
            self.service.cadastrar_sessao(int(filme_id), int(cinema_id), horario, sala)
            self.view.mostrar_mensagem("Sessao cadastrada com sucesso!")
        except ValueError as e:
            self.view.mostrar_mensagem(f"Erro: {e}")

    def listar_sessoes(self):
        sessoes = self.service.listar_sessoes()
        self.view.mostrar_sessoes(sessoes)

    def registrar_publico(self):
        sessao_id, quantidade = self.view.obter_dados_publico()
        try:
            self.service.registrar_publico(int(sessao_id), int(quantidade))
            self.view.mostrar_mensagem("Publico registrado com sucesso!")
        except ValueError as e:
            self.view.mostrar_mensagem(f"Erro: {e}")

    def total_publico_por_filme(self):
        filme_id = self.view.obter_id_filme()
        total = self.service.total_publico_por_filme(int(filme_id))
        self.view.mostrar_mensagem(f"Total de publico para o filme: {total} pessoas")
