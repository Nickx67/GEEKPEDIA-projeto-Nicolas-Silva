from collections import defaultdict


class Graph:

    def __init__(self):

        self.adjacency_list = defaultdict(list)

    # -----------------------------------
    # ADICIONAR VÉRTICE
    # -----------------------------------

    def add_node(self, node):

        if node not in self.adjacency_list:

            self.adjacency_list[node] = []

    # -----------------------------------
    # ADICIONAR ARESTA
    # -----------------------------------

    def add_edge(
        self,
        origin,
        destination,
        weight
    ):

        self.adjacency_list[origin].append(
            (destination, weight)
        )

        self.adjacency_list[destination].append(
            (origin, weight)
        )
    def find_node_by_title(
    self,
    title
):

        for node in self.adjacency_list.keys():

            if node.titulo.lower() == title.lower():

                return node

        return None
    # -----------------------------------
    # PEGAR VIZINHOS
    # -----------------------------------

    def get_neighbors(self, node):

        return self.adjacency_list[node]
    def get_nodes(self):

        return list(
        self.adjacency_list.keys()
    )

    # -----------------------------------
    # EXIBIR GRAFO
    # -----------------------------------

    def display(self):

        print("\n===== GRAFO =====\n")

        for node in self.adjacency_list:

            print(f"{node}:")

            for neighbor, weight in self.adjacency_list[node]:

                print(
                    f"   -> {neighbor} "
                    f"(peso: {weight})"
                )

            print()