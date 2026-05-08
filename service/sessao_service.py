from model.sessao import Sessao
from repository.sessao_repository import SessaoRepository
from repository.filme_repository import FilmeRepository


class SessaoService:
    def __init__(self):
        self.sessao_repo = SessaoRepository()
        self.filme_repo = FilmeRepository()

    def cadastrar_sessao(self, filme_id: int, cinema_id: int, horario: str, sala: str):
        if not horario or not sala:
            raise ValueError("Horario e sala sao obrigatorios.")
        filme = self.filme_repo.buscar_por_id(filme_id)
        if not filme:
            raise ValueError("Filme nao encontrado.")
        sessao = Sessao(filme_id, cinema_id, horario, sala)
        self.sessao_repo.salvar(sessao)

    def listar_sessoes(self):
        return self.sessao_repo.listar()

    def listar_por_cinema(self, cinema_id: int):
        return self.sessao_repo.listar_por_cinema(cinema_id)

    def registrar_publico(self, sessao_id: int, quantidade: int):
        if quantidade < 0:
            raise ValueError("Quantidade de publico nao pode ser negativa.")
        self.sessao_repo.registrar_publico(sessao_id, quantidade)

    def total_publico_por_filme(self, filme_id: int):
        return self.sessao_repo.total_publico_por_filme(filme_id)
