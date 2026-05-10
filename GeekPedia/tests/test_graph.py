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

def test_add_node():
    
    graph = Graph()

    node_naruto = Node(1, "Naruto", "Anime", "Ação", ["Ninjas"], "Jovem", "Naruto")

    
    graph.add_node(node_naruto)

    
    assert node_naruto in graph.adjacency_list