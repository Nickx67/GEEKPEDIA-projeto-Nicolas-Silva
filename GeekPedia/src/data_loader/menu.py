class Menu:

    @staticmethod
    def show():

        print("\n===== GEEKPEDIA =====\n")

        print("1 - Recomendações Diretas (BFS)")
        print("2 - Caminho Inteligente (Dijkstra)")
        print("0 - Sair")

        option = input(
            "\nEscolha uma opção: "
        )

        return option

    @staticmethod
    def choose_title():

        title = input(
            "\nDigite o nome da obra: "
        )

        return title