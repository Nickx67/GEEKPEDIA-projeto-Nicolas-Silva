from data_loader.file_reader import load_graph_from_json
from services.recommendation_service import RecommendationService
from data_loader.menu import Menu


def main():

    # -----------------------------
    # CARREGAR GRAFO
    # -----------------------------
    graph = load_graph_from_json(
        "data/dataset.json"
    )

    service = RecommendationService(
        graph
    )

    while True:

        option = Menu.show()

        # -------------------------
        # BFS
        # -------------------------
        if option == "1":

            title = Menu.choose_title()

            start_node = graph.find_node_by_title(
                title
            )

            if not start_node:

                print(
                    "\nObra não encontrada!"
                )

                continue

            recommendations = (
                service.get_direct_recommendations(
                    start_node
                )
            )

            print(
                "\n=== RECOMENDAÇÕES BFS ===\n"
            )

            for node in recommendations:

                print(node)

        # -------------------------
        # DIJKSTRA
        # -------------------------
        elif option == "2":

            title = Menu.choose_title()

            start_node = graph.find_node_by_title(
                title
            )

            if not start_node:

                print(
                    "\nObra não encontrada!"
                )

                continue

            recommendations = (
                service.get_smart_recommendations(
                    start_node
                )
            )

            print(
                "\n=== RECOMENDAÇÕES INTELIGENTES ===\n"
            )

            for node, cost in recommendations:

                print(
                    f"{node} "
                    f"(Custo: {cost})"
                )

        # -------------------------
        # SAIR
        # -------------------------
        elif option == "0":

            print("\nSaindo...")
            break

        # -------------------------
        # OPÇÃO INVÁLIDA
        # -------------------------
        else:

            print(
                "\nOpção inválida!"
            )


if __name__ == "__main__":

    main()