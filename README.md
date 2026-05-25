# GeekPedia — Sistema de Recomendação Temática Baseado em Grafos

O **GeekPedia** é um sistema inteligente de recomendação multiplataforma (animes, jogos e filmes) desenvolvido para a disciplina de **Teoria dos Grafos** (Profa. Dra. Andréa Ono Sakai). O sistema mapeia conexões complexas entre obras utilizando uma abordagem de grafos ponderados, permitindo que o usuário explore recomendações diretas e caminhos conceituais profundos através de uma interface web interativa em Flask.

---

## 1. Localização do Grafo no Repositório

O grafo e os seus componentes estruturais estão estritamente isolados na camada de **Domínio (Core)** do projeto. Abaixo está o mapeamento dos arquivos que definem e configuram o grafo:

```text
GeekPedia/
├── data/
│   └── dataset.json              # Banco de dados estruturado (vértices e arestas reais)
└── src/
    ├── core/
    │   ├── graph.py              # CLASSE PRINCIPAL: Implementação da Lista de Adjacência
    │   └── node.py               # CLASSE DO VÉRTICE: Representação da obra e suas tags
    └── data_loader/
        └── file_reader.py        # PARSER: Instancia o grafo carregando o arquivo JSON

Detalhes Técnicos dos Arquivos Core:
src/core/node.py (Vértices): Cada obra de entretenimento é representada como um nó contendo propriedades específicas (id, titulo, midia, genero, temas, publico_alvo, franquia).

src/core/graph.py (Estrutura): Implementa o grafo utilizando uma Lista de Adjacência estruturada nativamente. Essa escolha garante alta eficiência de memória para o cenário esparso do catálogo. As arestas são bidirecionais (não-dirigidas) e ponderadas.

2. Como o Grafo é Utilizado no Sistema
O ciclo de vida e a utilização do grafo no GeekPedia seguem uma arquitetura em camadas bem definida, dividida em quatro etapas fundamentais:

A. Carga e Inicialização (Infraestrutura)
Quando o servidor Flask (app.py) é iniciado, o arquivo src/data_loader/file_reader.py entra em ação:

Ele lê o catálogo armazenado em data/dataset.json.

Instancia um objeto da classe Graph.

Adiciona cada obra como um Node (vértice) e mapeia as similaridades com seus respectivos pesos (penalidades conceituais).

B. Processamento dos Motores de Busca (Algoritmos)
O grafo populado em memória é fornecido à camada de serviços (src/services/recommendation_service.py), que aciona os dois algoritmos centrais do projeto:

Busca em Largura (BFS): Utilizado para Recomendações Diretas. Ele varre a vizinhança imediata (grau 1 e 2) do nó pesquisado, restringindo os resultados a obras que fazem parte da mesma franquia ou universo direto.

Algoritmo de Dijkstra: Utilizado para Caminhos Inteligentes (Deep Discovery). Ele avalia os pesos das arestas e encontra a rota de menor custo acumulado através de uma Fila de Prioridade, conectando obras distantes (como ir de um anime para um jogo de luta) com o menor salto lógico possível.

C. Comunicação via API (Back-end)
O arquivo central src/app.py encapsula o grafo e expõe rotas que servem como endpoints para o front-end:

POST /bfs: Recebe o título da obra, localiza o nó no grafo e retorna os vizinhos imediatos.

POST /dijkstra: Recebe o título, executa o Dijkstra a partir do nó inicial, aplica uma trava de limite de custo acumulado (para evitar recomendações distantes demais) e retorna o Top K de mídias ordenadas.

D. Renderização Visual Interativa (Front-end)
No navegador, o front-end transforma a estrutura abstrata em uma representação visual:

O arquivo static/script.js faz uma requisição assíncrona ao servidor.

# 1. Instale o micro-framework Flask (necessário para o servidor web)
pip install flask

# 2. Certifique-se de estar na pasta raiz do projeto (onde fica data/ e src/)
# Execute o servidor web do Flask
python src/app.py

# 3. Acesse o sistema
# O terminal indicará que o servidor local está ativo. Abra o navegador e acesse:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

Ao receber a resposta, a função limpa o container HTML e reconstrói o grafo na tela dinamicamente.

Utilizando cálculos matemáticos, o JavaScript distribui radialmente as recomendações ao redor do nó de origem.
