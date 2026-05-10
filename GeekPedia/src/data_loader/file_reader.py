import json

from core.graph import Graph
from core.node import Node


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
    # CRIAR CONEXÕES
    # -----------------------------

    for conexao in data["conexoes"]:

        origem = nodes[conexao["origem"]]
        destino = nodes[conexao["destino"]]

        graph.add_edge(
            origem,
            destino,
            conexao["peso"]
        )

    return graph