# E2 — Design Técnico, Arquitetura e Backlog

> **Disciplina:** Teoria dos Grafos  
> **Prazo:** 13 de abril de 2026  
> **Peso:** 20% da nota final  

---

## Identificação do Grupo

| Campo | Preenchimento |
|-------|---------------|
| Nome do projeto | |
| Repositório GitHub | |
| Integrante 1 | Nicolas Silva Rodrigues de Melo — 38630192 |
| Integrante 2 | Henrique de Figueiredo Lourenço — 37509021 |
| Integrante 3 *(se houver)* | Nome — RA |

---

## 1. Algoritmos Escolhidos

### 1.1 Algoritmo Principal

| Campo | Resposta |
|-------|----------|
| Nome do algoritmo |Algoritmo de Dijkstra |
| Categoria |Caminho Mínimo (Guloso) |
| Complexidade de tempo | O((V + E) log V) com Min-Priority Queue |
| Complexidade de espaço | O(V+E) para armazenar o grafo e distâncias |
| Problema que resolve |Encontra a recomendação indireta de maior relevância (menor "custo" de similaridade) entre duas obras distantes no grafo.|

**Por que este algoritmo foi escolhido?**

<!-- Justifique a escolha para o seu domínio específico -->
  O Geekpedia utiliza um grafo ponderado onde os pesos representam "penalidades" por diferenças de atributos (mídia, gênero, etc.). O Dijkstra é o algoritmo ideal para encontrar o caminho que minimiza essas penalidades, garantindo que a recomendação feita ao usuário seja matematicamente a mais próxima possível do seu gosto original, mesmo que atravesse diferentes mídias.

**Alternativa descartada e motivo:**

| Algoritmo alternativo | Motivo da exclusão |
|----------------------|-------------------|
|Bellman-Ford | Como o nosso sistema de pesos é baseado em penalidades positivas (0 a 10) e não possui ciclos negativos, o Bellman-Ford seria menos eficiente que o Dijkstra, apresentando uma complexidade de O(V x E).|

**Limitações no contexto do problema:**

<!-- Liste ao menos 1 limitação relevante -->
O algoritmo assume que o usuário deseja a similaridade máxima absoluta. Ele não introduz "serendipidade" (descobertas ao acaso) de forma nativa, focando estritamente na menor distância numérica entre os vértices.

**Referência bibliográfica:**

> CORMEN, T. H. et al. Algoritmos: teoria e prática. 3. ed. Rio de Janeiro: Elsevier, 2012.

---

### 1.2 Algoritmo Adicional *(se houver)*

| Campo | Resposta |
|-------|----------|
| Nome do algoritmo |Busca em Largura (BFS) |
| Categoria |Busca em Grafo |
| Complexidade de tempo | O(V + E) |
| Complexidade de espaço | O(V) |
| Problema que resolve | Exploração de vizinhança imediata para recomendações de alta similaridade direta. |

**Justificativa:**

<!-- Por que este segundo algoritmo complementa o projeto? -->
  O BFS é utilizado para identificar obras que estão a poucos "saltos" de distância do conteúdo original, independente do peso. Isso permite que o sistema ofereça uma lista rápida de conteúdos relacionados que compartilham quase todas as tags com a obra pesquisada.

 **Alternativa descartada e motivo:**
 | Algoritmo alternativo | Motivo da exclusão |
|----------------------|-------------------|
|Busca em Profundidade (DFS)|O DFS poderia levar o usuário a recomendações muito distantes do ponto de origem logo no início da busca, não garantindo a exploração por camadas de proximidade que o sistema de recomendação exige.|

**Limitações no contexto do problema:**
O BFS ignora os pesos das arestas, tratando todas as conexões de similaridade como tendo a mesma importância, o que pode gerar recomendações menos precisas que o Dijkstra em grafos muito densos.

**Referência bibliográfica:**

> SEDGEWICK, R.; WAYNE, K. Algorithms. 4. ed. Upper Saddle River: Addison-Wesley, 2011.
    
---

## 2. Arquitetura em Camadas

> Insira o diagrama abaixo. Pode ser exportado do Draw.io, Excalidraw, etc.


![Diagrama de arquitetura]()

### Descrição das camadas

| Camada | Responsabilidade | Artefatos principais |
|--------|-----------------|----------------------|
| Apresentação (UI/CLI) |Interagir com o usuário, coletar entradas e exibir resultados | Interface CLI, entrada de nome do usuário, seleção de algoritmo (BFS/Dijkstra), exibição de recomendações | 
| Aplicação (Service) | Orquestrar o fluxo da aplicação e aplicar regras de uso |RecommendationService, lógica de decisão do algoritmo, definição de Top K resultados |
| Domínio (Core) | Implementar as regras de negócio e algoritmos centrais| Estrutura do grafo, função de similaridade, algoritmo BFS, algoritmo Dijkstra|
| Infraestrutura (I/O) | Lidar com entrada e saída de dados externos| Leitura de JSON, parser de dados| 

---

## 3. Estrutura de Diretórios

```
geekpedia/
├── docs/
│   ├── README.md
│   ├── E1_Geekpedia_Grafos.docx      # Documento de Requisitos [cite: 51]
│   └── E2_Designer_técnico.md        # Este documento de design técnico [cite: 52]
├── src/
│   ├── core/
│   │   ├── graph.py                  # Implementação da Lista de Adjacência [cite: 86]
│   │   └── node.py                   # Definição dos vértices (obras e suas tags) [cite: 68]
│   ├── algorithms/
│   │   ├── dijkstra.py               # Algoritmo de recomendação profunda [cite: 83]
│   │   └── bfs.py                    # Algoritmo de exploração rasa [cite: 82]
│   ├── io/
│   │   ├── file_reader.py            # Leitor de arquivos JSON [cite: 29]
│   │   └── graph_generator.py        # Gerador de grafos aleatórios [cite: 35]
│   ├── service/
│   │   └── recommendation_service.py # Orquestração e regras de negócio 
│   └── main.py                       # Ponto de entrada (CLI) [cite: 26]
├── tests/
│   ├── test_graph.py                 # Testes unitários da estrutura
│   └── test_algorithms.py            # Testes dos motores de recomendação
├── data/
│   └── dataset.json                  # Arquivo com o catálogo de obras [cite: 33]
└── requirements.txt                  # Dependências do projeto (se houver)
```

> **Justificativa de desvios** *(se houver)*: 

---

## 4. Definição do Dataset

**Formato de entrada aceito:**

<!-- JSON / CSV / GraphML / lista de adjacência — descreva a estrutura -->

**Exemplo de estrutura do arquivo de entrada:**

```json
{
  "obras": [
    {
      "id": 1,
      "titulo": "Naruto",
      "midia": "anime",
      "genero": "acao",
      "temas": ["ninjas", "amizade"],
      "publico_alvo": "jovem",
      "franquia": "Naruto"
    },
    {
      "id": 2,
      "titulo": "Naruto Storm",
      "midia": "jogo",
      "genero": "luta",
      "temas": ["ninjas", "combate"],
      "publico_alvo": "jovem",
      "franquia": "Naruto"
    },
    {
      "id": 3,
      "titulo": "Tekken",
      "midia": "jogo",
      "genero": "luta",
      "temas": ["artes marciais"],
      "publico_alvo": "jovem",
      "franquia": "Tekken"
    }
  ],
  "conexoes": [
    {
      "origem": 1,
      "destino": 2,
      "peso": 4,
      "justificativa": "Mesma franquia, penalidade por troca de mídia e tema."
    },
    {
      "origem": 2,
      "destino": 3,
      "peso": 6,
      "justificativa": "Franquias diferentes, mesma mídia e gênero."
    }
  ]
}
```

**Estratégia de geração aleatória:**

| Parâmetro | Descrição |
|-----------|-----------|
| Número de vértices | O usuário define a quantidade N de obras fictícias a serem geradas. Para cada uma, o sistema sorteia atributos (Mídia, Gênero, Franquia) de um pool pré-definido.  |
| Densidade | Controla a probabilidade (0.0 a 1.0) de existir uma conexão entre dois vértices quaisquer. O sistema percorre os pares e, se o sorteio for favorável, calcula o peso baseado na similaridade dos atributos sorteados. |
| Faixa de pesos | Definida pela Função de Similaridade. Embora os pesos sejam calculados pelas tags (1 a 10), o gerador pode introduzir um fator de ruído aleatório para testar como o Dijkstra lida com caminhos de custos variados em grafos muito grandes.  |

---

## 5. Backlog do Projeto

### 5.1 In-Scope — O que será implementado

| # | Funcionalidade | Prioridade | Critério de aceite |
|---|---------------|------------|-------------------|
| 1 | Carregamento de Dataset| Alta | Dado um arquivo JSON válido, quando o sistema iniciar, então o grafo deve ser populado corretamente em memória. |
| 2 |Recomendação Direta (BFS) |Alta| Dado um título inicial, quando o usuário solicitar similares, então o sistema deve retornar os vizinhos de grau 1 e 2.|
| 3 |Recomendação Inteligente (Dijkstra) |Alta |Dado um título de anime e um de jogo, quando solicitado o caminho, então o sistema deve exibir a menor rota de similaridade entre eles. |
| 4 | Filtro por Categoria|Média | Dado uma lista de recomendações, quando o filtro "Jogo" for ativado, então apenas vértices daquela categoria devem aparecer.|
| 5 |Geração de Grafo Aleatório |Baixa |Dado um N de vértices, quando solicitado, então o sistema deve criar conexões e pesos aleatórios para teste de performance. |

### 5.2 Out-of-Scope — O que NÃO será feito

| Funcionalidade excluída | Motivo |
|------------------------|--------|
| Interface Gráfica (GUI)| O foco do projeto é o desempenho dos algoritmos de grafos via console.|
|Web Scrapping em tempo real |Os dados serão estáticos (Dataset local) para garantir a estabilidade dos testes. |
|Sistema de Login de Usuário |O sistema é uma ferramenta de consulta técnica, não uma rede social. |

---

## Checklist de Entrega

- [x] Big-O de tempo e espaço declarados para cada algoritmo
- [x] Ao menos 1 alternativa descartada com justificativa
- [x] Diagrama de arquitetura com 4 camadas identificadas
- [x] Referência bibliográfica para cada algoritmo (ABNT ou IEEE)
- [x] Backlog com ≥ 5 itens In-Scope e ≥ 3 Out-of-Scope
- [x] Ao menos 3 critérios de aceite no formato "dado / quando / então"
- [x] Exemplo de estrutura de arquivo de entrada presente

---

*Teoria dos Grafos — Profa. Dra. Andréa Ono Sakai*
