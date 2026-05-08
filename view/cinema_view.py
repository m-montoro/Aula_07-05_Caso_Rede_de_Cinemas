class CinemaView:
    def mostrar_menu_principal(self):
        print("\n===== SISTEMA DE REDE DE CINEMAS =====")
        print("1 - Gerenciar Filmes")
        print("2 - Gerenciar Sessoes")
        print("0 - Sair")

    def mostrar_menu_filmes(self):
        print("\n--- Menu de Filmes ---")
        print("1 - Cadastrar Filme")
        print("2 - Listar Filmes")
        print("0 - Voltar")

    def mostrar_menu_sessoes(self):
        print("\n--- Menu de Sessoes ---")
        print("1 - Cadastrar Sessao")
        print("2 - Listar Sessoes")
        print("3 - Registrar Publico")
        print("4 - Total de Publico por Filme")
        print("0 - Voltar")

    def obter_dados_filme(self):
        titulo = input("Titulo: ")
        diretor = input("Diretor: ")
        genero = input("Genero: ")
        duracao = input("Duracao (minutos): ")
        return titulo, diretor, genero, duracao

    def obter_dados_sessao(self):
        filme_id = input("ID do Filme: ")
        cinema_id = input("ID do Cinema (ex: 1): ")
        horario = input("Horario (ex: 14:30): ")
        sala = input("Sala: ")
        return filme_id, cinema_id, horario, sala

    def obter_dados_publico(self):
        sessao_id = input("ID da Sessao: ")
        quantidade = input("Quantidade de publico: ")
        return sessao_id, quantidade

    def obter_id_filme(self):
        return input("ID do Filme: ")

    def mostrar_filmes(self, filmes):
        print("\n========= FILMES EM CARTAZ =========")
        if not filmes:
            print("Nenhum filme cadastrado.")
        for f in filmes:
            print(f"[{f.id}] {f.titulo} | Dir: {f.diretor} | Genero: {f.genero} | {f.duracao_min} min")
        print("=====================================")

    def mostrar_sessoes(self, sessoes):
        print("\n=========== SESSOES ===========")
        if not sessoes:
            print("Nenhuma sessao cadastrada.")
        for s in sessoes:
            print(f"[{s.id}] Filme ID: {s.filme_id} | Cinema ID: {s.cinema_id} | {s.horario} | Sala: {s.sala} | Publico: {s.publico}")
        print("================================")

    def mostrar_mensagem(self, mensagem):
        print(f"\n>>> {mensagem}")
