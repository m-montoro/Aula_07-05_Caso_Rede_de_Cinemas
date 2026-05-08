from db.database import get_connection
from model.sessao import Sessao


class SessaoRepository:
    def salvar(self, sessao: Sessao):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO sessoes (filme_id, cinema_id, horario, sala, publico) VALUES (?, ?, ?, ?, ?)",
            (sessao.filme_id, sessao.cinema_id, sessao.horario, sessao.sala, sessao.publico)
        )
        conn.commit()
        conn.close()

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, filme_id, cinema_id, horario, sala, publico FROM sessoes")
        rows = cursor.fetchall()
        conn.close()
        sessoes = []
        for r in rows:
            s = Sessao(r[1], r[2], r[3], r[4], r[0])
            s.publico = r[5]
            sessoes.append(s)
        return sessoes

    def listar_por_cinema(self, cinema_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, filme_id, cinema_id, horario, sala, publico FROM sessoes WHERE cinema_id = ?",
            (cinema_id,)
        )
        rows = cursor.fetchall()
        conn.close()
        sessoes = []
        for r in rows:
            s = Sessao(r[1], r[2], r[3], r[4], r[0])
            s.publico = r[5]
            sessoes.append(s)
        return sessoes

    def registrar_publico(self, sessao_id: int, quantidade: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE sessoes SET publico = publico + ? WHERE id = ?",
            (quantidade, sessao_id)
        )
        conn.commit()
        conn.close()

    def total_publico_por_filme(self, filme_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT SUM(publico) FROM sessoes WHERE filme_id = ?",
            (filme_id,)
        )
        result = cursor.fetchone()[0]
        conn.close()
        return result or 0
