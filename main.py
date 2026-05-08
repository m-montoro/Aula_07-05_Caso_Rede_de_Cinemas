from controller.filme_controller import FilmeController
from controller.sessao_controller import SessaoController
from view.cinema_view import CinemaView


def main():
    view = CinemaView()
    filme_ctrl = FilmeController(view)
    sessao_ctrl = SessaoController(view)

    while True:
        view.mostrar_menu_principal()
        opcao = input("Opcao: ").strip()

        if opcao == "1":
            while True:
                view.mostrar_menu_filmes()
                sub = input("Opcao: ").strip()
                if sub == "1":
                    filme_ctrl.cadastrar_filme()
                elif sub == "2":
                    filme_ctrl.listar_filmes()
                elif sub == "0":
                    break
                else:
                    view.mostrar_mensagem("Opcao invalida.")

        elif opcao == "2":
            while True:
                view.mostrar_menu_sessoes()
                sub = input("Opcao: ").strip()
                if sub == "1":
                    sessao_ctrl.cadastrar_sessao()
                elif sub == "2":
                    sessao_ctrl.listar_sessoes()
                elif sub == "3":
                    sessao_ctrl.registrar_publico()
                elif sub == "4":
                    sessao_ctrl.total_publico_por_filme()
                elif sub == "0":
                    break
                else:
                    view.mostrar_mensagem("Opcao invalida.")

        elif opcao == "0":
            print("Encerrando sistema. Ate logo!")
            break
        else:
            view.mostrar_mensagem("Opcao invalida.")


if __name__ == "__main__":
    main()
