class Sessao:
    def __init__(self, filme_id: int, cinema_id: int, horario: str, sala: str, id: int = None):
        self.id = id
        self.filme_id = filme_id
        self.cinema_id = cinema_id
        self.horario = horario
        self.sala = sala
        self.publico = 0
