from db.database import get_connection
from model.filme import Filme


class FilmeRepository:
    def salvar(self, filme: Filme):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO filmes (titulo, diretor, genero, duracao_min) VALUES (?, ?, ?, ?)",
            (filme.titulo, filme.diretor, filme.genero, filme.duracao_min)
        )
        conn.commit()
        conn.close()

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, titulo, diretor, genero, duracao_min FROM filmes")
        rows = cursor.fetchall()
        conn.close()
        return [Filme(r[1], r[2], r[3], r[4], r[0]) for r in rows]

    def buscar_por_id(self, filme_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, titulo, diretor, genero, duracao_min FROM filmes WHERE id = ?", (filme_id,))
        r = cursor.fetchone()
        conn.close()
        if r:
            return Filme(r[1], r[2], r[3], r[4], r[0])
        return None
