from collections import deque


def bfs(graph, start_node, max_depth=2):

    visited = set()

    queue = deque()

    recommendations = []

    queue.append(
        (start_node, 0)
    )

    visited.add(start_node)

    while queue:

        current_node, depth = queue.popleft()

        if depth > 0:
            recommendations.append(current_node)

        if depth < max_depth:

            for neighbor, _ in graph.get_neighbors(
                current_node
            ):

                if (
                    neighbor not in visited
                    and neighbor.franquia == start_node.franquia
                ):

                    visited.add(neighbor)

                    queue.append(
                        (
                            neighbor,
                            depth + 1
                        )
                    )

    return recommendations