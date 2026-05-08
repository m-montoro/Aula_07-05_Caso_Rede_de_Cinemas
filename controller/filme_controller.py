from service.filme_service import FilmeService


class FilmeController:
    def __init__(self, view):
        self.service = FilmeService()
        self.view = view

    def cadastrar_filme(self):
        titulo, diretor, genero, duracao = self.view.obter_dados_filme()
        try:
            self.service.cadastrar_filme(titulo, diretor, genero, int(duracao))
            self.view.mostrar_mensagem("Filme cadastrado com sucesso!")
        except ValueError as e:
            self.view.mostrar_mensagem(f"Erro: {e}")

    def listar_filmes(self):
        filmes = self.service.listar_filmes()
        self.view.mostrar_filmes(filmes)
