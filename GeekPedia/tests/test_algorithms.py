import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)

from core.graph import Graph
from core.node import Node
from algorithms.bfs import bfs
from algorithms.dijkstra import (
    dijkstra,
    get_shortest_path
)

# Criação de nós simulados para os testes
node_naruto = Node(1, "Naruto", "Anime", "Ação", ["Ninjas"], "Jovem", "Naruto")
node_storm = Node(2, "Naruto Storm", "Jogo", "Luta", ["Ninjas"], "Jovem", "Naruto")
node_tekken = Node(3, "Tekken", "Jogo", "Luta", ["Artes Marciais"], "Jovem", "Tekken")

def test_bfs():
    graph = Graph()

    graph.add_node(node_naruto)
    graph.add_node(node_storm)
    graph.add_node(node_tekken)

    graph.add_edge(node_naruto, node_storm, 4)
    graph.add_edge(node_storm, node_tekken, 6)

    result = bfs(graph, node_naruto)

   
    assert node_storm in result
    assert node_tekken not in result

def test_dijkstra():
    graph = Graph()

    graph.add_node(node_naruto)
    graph.add_node(node_storm)
    graph.add_node(node_tekken)

    graph.add_edge(node_naruto, node_storm, 4)
    graph.add_edge(node_storm, node_tekken, 6)

    distances, previous_nodes = dijkstra(graph, node_naruto)

    path = get_shortest_path(previous_nodes, node_naruto, node_tekken)

    # Verifica se a distância calculada está correta
    assert distances[node_tekken] == 10

    # Verifica se o caminho reconstruído está correto
    assert path == [node_naruto, node_storm, node_tekken]