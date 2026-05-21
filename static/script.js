
function drawGraph(mainTitle, recommendations) {

    const graph =
        document.getElementById("graph");

    graph.innerHTML = "";

    const centerX = 390;
    const centerY = 240;

    // -------------------------
    // NÓ CENTRAL
    // -------------------------

    const centerNode =
        document.createElement("div");

    centerNode.className =
        "node center-node";

    centerNode.style.left =
        centerX + "px";

    centerNode.style.top =
        centerY + "px";

    centerNode.innerText =
        mainTitle;

    graph.appendChild(centerNode);

    // -------------------------
    // RECOMENDAÇÕES
    // -------------------------

    const radius = 220;

    recommendations.forEach((item, index) => {

        const angle =
            (2 * Math.PI * index)
            / recommendations.length;

        const x =
            centerX +
            radius * Math.cos(angle);

        const y =
            centerY +
            radius * Math.sin(angle);

        // ---------------------
        // LINHA
        // ---------------------

        const line =
            document.createElement("div");

        line.className = "line";

        const startX = centerX + 60;
        const startY = centerY + 60;

        const endX = x + 60;
        const endY = y + 60;

        const dx = endX - startX;
        const dy = endY - startY;

        const length = Math.sqrt(
            dx * dx + dy * dy
        );

        const angleDeg =
            Math.atan2(dy, dx)
            * 180
            / Math.PI;

        const offset = 60;

        const adjustedStartX =
            startX +
            (dx / length) * offset;

        const adjustedStartY =
            startY +
            (dy / length) * offset;

        line.style.width =
            (length - 120) + "px";

        line.style.left =
            adjustedStartX + "px";

        line.style.top =
            adjustedStartY + "px";

        line.style.transform =
            `rotate(${angleDeg}deg)`;

        graph.appendChild(line);

        // ---------------------
        // NÓ
        // ---------------------

        const node =
            document.createElement("div");

        node.className = "node";

        node.style.left =
            x + "px";

        node.style.top =
            y + "px";

        if (typeof item === "string") {

            node.innerText = item;
        }
        else {

            node.innerText =
                item.title +
                "\nPeso: " +
                item.cost;
        }

        graph.appendChild(node);

    });

}



function runBFS() {

    const title =
        document.getElementById(
            "titleInput"
        ).value;

    fetch("/bfs", {

        method: "POST",

        headers: {
            "Content-Type":
                "application/json"
        },

        body: JSON.stringify({
            title: title
        })
    })

    .then(response => response.json())

    .then(data => {

        drawGraph(title, data);
    });
}



function runDijkstra() {

    const title =
        document.getElementById(
            "titleInput"
        ).value;

    fetch("/dijkstra", {

        method: "POST",

        headers: {
            "Content-Type":
                "application/json"
        },

        body: JSON.stringify({
            title: title
        })
    })

    .then(response => response.json())

    .then(data => {

        drawGraph(title, data);
    });
}

