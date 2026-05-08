class Filme:
    def __init__(self, titulo: str, diretor: str, genero: str, duracao_min: int, id: int = None):
        self.id = id
        self.titulo = titulo
        self.diretor = diretor
        self.genero = genero
        self.duracao_min = duracao_min
