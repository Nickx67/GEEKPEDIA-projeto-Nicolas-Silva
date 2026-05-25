const stars =
    document.getElementById("stars");

for (let i = 0; i < 250; i++) {

    const star =
        document.createElement("div");

    star.className = "star";

    const size =
        Math.random() * 3 + 1;

    star.style.width =
        size + "px";

    star.style.height =
        size + "px";

    star.style.left =
        Math.random() * 100 + "%";

    star.style.top =
        Math.random() * 100 + "%";

    star.style.opacity =
        Math.random();

    star.style.animationDelay =
        Math.random() * 5 + "s";

    stars.appendChild(star);
}

function drawGraph(mainTitle, recommendations) {

    const graph =
        document.getElementById("graph");
        document.getElementById(
    "graph"
).innerHTML = `
    <div class="error-box">
        Obra não encontrada
    </div>
`;

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

const variation =
    (Math.random() - 0.5) * 100;

const randomRadius =
    radius + variation;

const x =
    centerX +
    randomRadius * Math.cos(angle);

const y =
    centerY +
    randomRadius * Math.sin(angle);

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
    dx * dx +
    dy * dy
);

const angleDeg =
    Math.atan2(dy, dx) *
    180 / Math.PI;

line.style.width =
    length + "px";

line.style.left =
    startX + "px";

line.style.top =
    startY + "px";

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
        if (data.error) {

    document
        .getElementById("graph")
        .innerHTML =
        "<h2>Obra não encontrada</h2>";

    return;
}
        

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
        if (data.error) {

    document
        .getElementById("graph")
        .innerHTML =
        "<h2>Obra não encontrada</h2>";

    return;
}

        drawGraph(title, data);
    });
}

