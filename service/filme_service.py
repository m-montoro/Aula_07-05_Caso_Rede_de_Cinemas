from model.filme import Filme
from repository.filme_repository import FilmeRepository


class FilmeService:
    def __init__(self):
        self.repository = FilmeRepository()

    def cadastrar_filme(self, titulo: str, diretor: str, genero: str, duracao_min: int):
        if not titulo or not diretor:
            raise ValueError("Titulo e diretor sao obrigatorios.")
        if duracao_min <= 0:
            raise ValueError("Duracao deve ser maior que zero.")
        filme = Filme(titulo, diretor, genero, duracao_min)
        self.repository.salvar(filme)

    def listar_filmes(self):
        return self.repository.listar()

    def buscar_filme(self, filme_id: int):
        filme = self.repository.buscar_por_id(filme_id)
        if not filme:
            raise ValueError("Filme nao encontrado.")
        return filme
