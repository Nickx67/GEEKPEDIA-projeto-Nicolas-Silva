# E1 - Entregável 1: GeekPedia (Grafos)

## Identificação do Grupo
| Campo | Preenchimento |
| :--- | :--- |
| **Nome do projeto** | Geekpedia |
| **Integrante 1** | Nicolas Silva Rodrigues de Melo — RA 38630192 |
| **Integrante 2** | Henrique de Figueiredo Lourenço — RA 37509021 |
| **Integrante 3** | N/A |
| **Domínio de aplicação** | Sistemas de recomendação — entretenimento digital |

---

## 1. Algoritmos Escolhidos

### Algoritmo 1
| Campo | Resposta |
| :--- | :--- |
| **Nome do algoritmo** | Algoritmo de Dijkstra |
| **Categoria** | Caminho Mínimo (Guloso) |
| **Complexidade de tempo** | O ((V + E) log V) com Min-Priority Queue |
| **Complexidade de espaço** | O (V + E) para armazenar o grafo e distâncias |
| **Problema que resolve** | Encontra a recomendação indireta de maior relevância (menor "custo" de similaridade) entre duas obras distantes no grafo. |

**Por que este algoritmo foi escolhido?** O Geekpedia utiliza um grafo ponderado onde os pesos representam "penalidades" por diferenças de atributos (mídia, gênero, etc.). O Dijkstra é o algoritmo ideal para encontrar o caminho que minimiza essas penalidades, garantindo que a recomendação feita ao usuário seja matematicamente a mais próxima possível do seu gosto original, mesmo que atravesse diferentes mídias.

**Alternativa descartada e motivo:**
| Algoritmo alternativo | Motivo da exclusão |
| :--- | :--- |
| **Bellman-Ford** | Como o nosso sistema de pesos é baseado em penalidades positivas (0 a 10) e não possui ciclos negativos, o Bellman-Ford seria menos eficiente que o Dijkstra, apresentando uma complexidade de O(V x E). |

**Limitações no contexto do problema:** O algoritmo assume que o usuário deseja a similaridade máxima absoluta. Ele não introduz "serendipidade" (descobertas ao acaso) de forma nativa, focando estritamente na menor distância numérica entre os vértices.

**Referência bibliográfica:** CORMEN, T. H. et al. Algoritmos: teoria e prática. 3. ed. Rio de Janeiro: Elsevier, 2012.

### Algoritmo 2
| Campo | Resposta |
| :--- | :--- |
| **Nome do algoritmo** | Busca em Largura (BFS) |
| **Categoria** | Busca em Grafo |
| **Complexidade de tempo** | O(V + E) |
| **Complexidade de espaço** | O(V) |
| **Problema que resolve** | Exploração de vizinhança imediata para recomendações de alta similaridade direta. |

**Por que este algoritmo foi escolhido?** O BFS é utilizado para identificar obras que estão a poucos "saltos" de distância do conteúdo original, independente do peso. Isso permite que o sistema ofereça uma lista rápida de conteúdos relacionados que compartilham quase todas as tags com a obra pesquisada.

**Alternativa descartada e motivo:**
| Algoritmo alternativo | Motivo da exclusão |
| :--- | :--- |
| **Busca em Profundidade (DFS)** | O DFS poderia levar o usuário a recomendações muito distantes do ponto de origem logo no início da busca, não garantindo a exploração por camadas de proximidade que o sistema de recomendação exige. |

**Limitações no contexto do problema:** O BFS ignora os pesos das arestas, tratando todas as conexões de similaridade como tendo a mesma importância, o que pode gerar recomendações menos precisas que o Dijkstra em grafos muito densos.

**Referência bibliográfica:** SEDGEWICK, R.; WAYNE, K. Algorithms. 4. ed. Upper Saddle River: Addison-Wesley, 2011.

---

## 2. Objetivo Geral
Desenvolver um sistema baseado em grafos ponderados capaz de calcular a distância conceitual entre obras de entretenimento digital para recomendar conteúdos direta e indiretamente relacionados, independentemente da mídia original.

---

## 3. Definição do Dataset

**Formato de entrada aceito:** O sistema aceitará arquivos no formato JSON, devido à facilidade de representar objetos (obras) com múltiplas tags e suas conexões.

**Exemplo de estrutura do arquivo de entrada:**
```json
{ 
  "obras": [ 
    { "id": 1, "titulo": "Naruto", "categoria": "Anime", "tags": ["Ação", "Shonen"] }, 
    { "id": 2, "titulo": "Tekken", "categoria": "Jogo", "tags": ["Luta", "Arcade"] } 
  ], 
  "conexoes": [ 
    { "origem": 1, "destino": 2, "peso": 4 } 
  ] 
} 
```

---

## 4. Público-Alvo / Caso de Uso Principal
O sistema é voltado para fãs de cultura pop que consomem múltiplas formas de mídia e desejam expandir seu repertório de forma fluida e embasada.

**Cenário concreto de uso:** Um usuário finalizou a série de anime "Naruto" e busca novas experiências. Ao pesquisar "Naruto" no sistema, ele receberá recomendações diretas via BFS (como o anime "Dragon Ball", que está a poucos saltos de distância no grafo). Simultaneamente, o algoritmo de Dijkstra navegará pelo grafo cruzando mídias para recomendar o jogo de luta "Tekken", encontrando um caminho viável de menor penalidade conceitual que conecta as obras por meio de atributos compartilhados, como a temática de artes marciais e o público-alvo competitivo.

---

## 5. Justificativa Técnica — Por que Grafos?
A modelagem em grafos é a abordagem ideal porque mapeia perfeitamente a estrutura não-linear e conectada do entretenimento: as obras se tornam os vértices e as relações de similaridade assumem o papel de arestas. A similaridade é recíproca, tornando o grafo inerentemente não-dirigido. Além disso, a similaridade varia em graus de intensidade (uma continuação direta é muito mais similar do que uma obra apenas do mesmo gênero), o que exige um grafo ponderado. Nesse modelo, o peso atua como uma medida de "distância conceitual" calculada pelas divergências nas tags de cada obra.

Essa estrutura justifica e potencializa o uso de dois algoritmos clássicos com papéis delimitados: o BFS fará a varredura da vizinhança direta sem se preocupar em somar custos extensos (ótimo para indicar obras idênticas ou do mesmo universo imediato). Já o Dijkstra atuará como o núcleo avançado do sistema, avaliando os pesos para encontrar o trajeto com o menor acúmulo de diferenças (menor custo) através do grafo inteiro. Dessa forma, é garantida a melhor sugestão indireta matematicamente possível.

---

## 6. Tipo de Grafo

| Característica | Escolha | Justificativa breve |
| :--- | :--- | :--- |
| **Dirigido ou não-dirigido** | Não-dirigido | A relação de similaridade e a diferença de atributos entre obras são bidirecionais e simétricas. |
| **Ponderado ou não-ponderado** | Ponderado | O peso numérico (1 a 10) representa a penalidade/distância gerada pela diferença de tags estruturais entre as obras. |
| **Conectado / bipartido / geral** | Geral | Podem existir componentes isolados caso algumas obras de nicho não compartilhem tags suficientes com o resto do catálogo para formar conexões. |
| **Representação interna pretendida** | Lista de adjacência | Muito mais eficiente para uso de memória, uma vez que o grafo de recomendações será altamente esparso. |

---

## 7. Diagrama Conceitual
**Legenda:** A figura ilustra um protótipo não-dirigido do domínio do sistema. Vértices: obras de entretenimento. Arestas: relações de similaridade sem direção. Pesos: custo numérico indicando a distância conceitual (penalidade por tags diferentes). A topologia apresenta ciclos e múltiplos caminhos viáveis que serão explorados pelos algoritmos BFS e Dijkstra.

*(Insira aqui a imagem do diagrama conceitual que consta no PDF original)*

---

### Checklist de Entrega
Antes de submeter, confirme:
- [x] Texto entre 300 e 600 palavras (seções 1 a 5)
- [x] Todos os campos da tabela de identificação preenchidos
- [x] Tipo de grafo especificado com justificativa
- [x] Diagrama presente e referenciado no texto
- [x] Arquivo nomeado como E1_Geekpedia_Grafos.docx (versão Word) ou PR aberto (versão GitHub)
