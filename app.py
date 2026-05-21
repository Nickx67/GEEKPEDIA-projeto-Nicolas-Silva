
from flask import Flask, render_template, request, jsonify

from data_loader.file_reader import load_graph_from_json
from services.recommendation_service import RecommendationService


# -----------------------------------
# APP
# -----------------------------------

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


# -----------------------------------
# CARREGAR GRAFO
# -----------------------------------

import os

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

dataset_path = os.path.join(
    BASE_DIR,
    "data",
    "dataset.json"
)

graph = load_graph_from_json(
    dataset_path
)


service = RecommendationService(graph)


# -----------------------------------
# HOME
# -----------------------------------

@app.route("/")
def home():

    return render_template("index.html")


# -----------------------------------
# BFS
# -----------------------------------


@app.route("/bfs", methods=["POST"])
def bfs_route():

    print("ROTA BFS CHAMADA")

    data = request.json

    print(data)

    title = data.get("title")

    print(title)

    start_node = graph.find_node_by_title(
        title
    )

    print(start_node)

    if not start_node:

        return jsonify({
            "error": "Obra não encontrada"
        })

    recommendations = (
        service.get_direct_recommendations(
            start_node
        )
    )

    print(recommendations)

    result = [
        str(node)
        for node in recommendations
    ]

    return jsonify(result)




# -----------------------------------
# DIJKSTRA
# -----------------------------------

@app.route("/dijkstra", methods=["POST"])
def dijkstra_route():

    data = request.json

    title = data.get("title")

    start_node = graph.find_node_by_title(
        title
    )

    if not start_node:

        return jsonify({
            "error": "Obra não encontrada"
        })

    recommendations = (
        service.get_smart_recommendations(
            start_node
        )
    )

    result = [
        {
            "title": str(node),
            "cost": cost
        }
        for node, cost in recommendations
    ]

    return jsonify(result)


# -----------------------------------
# EXECUÇÃO
# -----------------------------------

if __name__ == "__main__":

    app.run(debug=True)

