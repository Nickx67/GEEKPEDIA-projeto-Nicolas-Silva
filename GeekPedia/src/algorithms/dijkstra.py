import heapq


def dijkstra(graph, start_node):

    # -----------------------------------
    # INICIALIZAÇÃO
    # -----------------------------------

    distances = {
        node: float("inf")
        for node in graph.get_nodes()
    }

    previous_nodes = {
        node: None
        for node in graph.get_nodes()
    }

    distances[start_node] = 0

    # Heap:
    # (distância, título, nó)
    priority_queue = [
        (
            0,
            start_node.titulo,
            start_node
        )
    ]

    # -----------------------------------
    # PROCESSAMENTO
    # -----------------------------------

    while priority_queue:

        current_distance, _, current_node = (
            heapq.heappop(priority_queue)
        )

        # Ignora caminhos piores
        if current_distance > distances[
            current_node
        ]:
            continue

        # Explora vizinhos
        for neighbor, weight in graph.get_neighbors(
            current_node
        ):

            distance = (
                current_distance + weight
            )

            # Relaxamento
            if distance < distances[neighbor]:

                distances[neighbor] = distance

                previous_nodes[
                    neighbor
                ] = current_node

                heapq.heappush(
                    priority_queue,
                    (
                        distance,
                        neighbor.titulo,
                        neighbor
                    )
                )

    return distances, previous_nodes


# -----------------------------------
# RECONSTRUIR CAMINHO
# -----------------------------------

def get_shortest_path(
    previous_nodes,
    start_node,
    target_node
):

    path = []

    current_node = target_node

    while current_node is not None:

        path.append(current_node)

        current_node = previous_nodes[
            current_node
        ]

    path.reverse()

    # Verifica se há caminho válido
    if path and path[0] == start_node:

        return path

    return []