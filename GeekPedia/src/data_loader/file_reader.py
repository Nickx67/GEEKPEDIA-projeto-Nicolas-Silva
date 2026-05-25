import json

from core.graph import Graph
from core.node import Node


def calculate_weight(origem, destino):

    # -----------------------------
    # MESMA FRANQUIA
    # -----------------------------

    if origem.franquia == destino.franquia:

        peso = 2

    # -----------------------------
    # GÊNERO OU TEMA PARECIDO
    # -----------------------------

    elif (
        origem.genero == destino.genero
        or any(
            tema in destino.temas
            for tema in origem.temas
        )
    ):

        peso = 5

    # -----------------------------
    # MUITO DIFERENTES
    # -----------------------------

    else:

        peso = 8

    # -----------------------------
    # MUDOU A MÍDIA
    # -----------------------------

    if origem.midia != destino.midia:

        peso += 1

    return peso


def load_graph_from_json(file_path):

    graph = Graph()

    nodes = {}

    # -----------------------------
    # LER JSON
    # -----------------------------

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    # -----------------------------
    # CRIAR NÓS
    # -----------------------------

    for obra in data["obras"]:

        node = Node(
            obra["id"],
            obra["titulo"],
            obra["midia"],
            obra["genero"],
            obra["temas"],
            obra["publico_alvo"],
            obra["franquia"]
        )

        nodes[obra["id"]] = node

        graph.add_node(node)

    # -----------------------------
    # CRIAR CONEXÕES AUTOMÁTICAS
    # -----------------------------

    node_list = list(nodes.values())

    for i in range(len(node_list)):

        for j in range(i + 1, len(node_list)):

            node1 = node_list[i]
            node2 = node_list[j]

            weight = calculate_weight(
                node1,
                node2
            )

            # Evita conexões muito ruins
            if weight <= 6:

                graph.add_edge(
                    node1,
                    node2,
                    weight
                )

                graph.add_edge(
                    node2,
                    node1,
                    weight
                )

    return graph