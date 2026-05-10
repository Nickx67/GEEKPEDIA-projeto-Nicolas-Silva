from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra


class RecommendationService:

    def __init__(self, graph):

        self.graph = graph

    # -----------------------------------
    # BFS
    # -----------------------------------
    def get_direct_recommendations(
        self,
        start_node,
        max_depth=2
    ):

        return bfs(
            self.graph,
            start_node,
            max_depth
        )

    # -----------------------------------
    # DIJKSTRA (TOP K)
    # -----------------------------------
    def get_smart_recommendations(
        self,
        start_node,
        top_k=5
    ):

        distances, _ = dijkstra(
            self.graph,
            start_node
        )

        recommendations = sorted(
            [
                (
                    node,
                    cost
                )
                for node, cost in distances.items()
                if node != start_node
                and cost < float("inf")
            ],
            key=lambda x: x[1]
        )

        return recommendations[
            :top_k
        ]