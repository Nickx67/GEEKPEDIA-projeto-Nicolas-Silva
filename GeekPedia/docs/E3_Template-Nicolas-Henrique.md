# E3 — MVP: Núcleo Funcional com Primeiras Telas

> **Disciplina:** Teoria dos Grafos  
> **Prazo:** 10 de maio de 2026  
> **Peso:** 25% da nota final  

---

## Identificação do Grupo

| Campo | Preenchimento |
|-------|---------------|
| Nome do projeto | Geekpedia|
| Repositório GitHub | |
| Integrante 1 | Nicolas Silva Rodrigues de Melo — 38630192 |
| Integrante 2 | Henrique de Figueiredo Lourenço — 37509021 |
| Integrante 3 *(se houver)* | Nome — RA |

---

## 1. Como Executar o MVP

> Instrua como rodar o projeto do zero. Alguém que nunca viu o código deve conseguir executar seguindo estas instruções.

**Pré-requisitos:**
    Python 3.10+

```bash
# Ex.: Python 3.11+, Node 18+, Java 17+...
```

**Instalação:**

```bash
# Clone e instale dependências
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
# pip install -r requirements.txt  (ou npm install, etc.)
```

**Execução:**

```bash
# Comando para rodar o MVP
# Execute a partir da raiz do projeto
python src/main.py
```

**Saída esperada:**

```
===== GEEKPEDIA =====
1 - Recomendações Diretas (BFS)
2 - Caminho Inteligente (Dijkstra)
0 - Sair

Escolha uma opção:

# Cole aqui um exemplo real da saída do seu programa
```

---

## 2. Algoritmo Implementado

| Campo | Resposta |
|-------|----------|
| Nome do algoritmo | Algoritmo de Dijkstra|
| Arquivo de implementação | src/algorithms/dijkstra.py |
| Complexidade de tempo | O((V + E) log V)|
| Complexidade de espaço | O(V + E) |

**Trecho do código com comentário de Big-O:**

```python
# Cole aqui o trecho principal do algoritmo
# com comentários de complexidade nas linhas críticas

# Explora vizinhos - O(E) total no decorrer do algoritmo    
for neighbor, weight in graph.get_neighbors(current_node):
    distance = current_distance + weight # O(1)

    # Relaxamento - O(1)
    if distance < distances[neighbor]:
        distances[neighbor] = distance
        previous_nodes[neighbor] = current_node
        
        # Inserção na Priority Queue - O(log V)
        heapq.heappush(priority_queue, (distance, neighbor.titulo, neighbor))
```

---

## 3. Estrutura do Repositório

> Confirme que a estrutura implementada está de acordo com o E2.


```
GeekPedia/
├── src/
│   ├── core/
│   │   ├── graph.py
│   │   └── node.py
│   ├── algorithms/
│   │   ├── bfs.py
│   │   └── dijkstra.py
│   ├── data_loader/
│   │   ├── file_reader.py
│   │   └── menu.py
│   └── main.py
├── tests/
│   ├── test_algorithms.py
│   └── test_graph.py
└── data/
    └── dataset.json
```

**Desvios em relação ao E2** *(se houver)*:
1. A pasta de infraestrutura, originalmente documentada como src/io/, foi renomeada para src/data_loader/. Essa alteração foi estritamente técnica e necessária, pois io é uma biblioteca nativa do Python, o que estava causando conflitos de importação no interpretador.
2. Foi adicionado o arquivo menu.py dentro de data_loader/ para separar a lógica de interface (CLI) do fluxo principal em main.py, melhorando a arquitetura.

---

## 4. Telas do MVP

> Insira screenshots ou gravações da interface funcionando.

### Tela de Entrada

![Tela de entrada](./assets/mvp_entrada.png)

*Descrição:*

### Tela de Resultado

![Tela de resultado](./assets/mvp_resultado.png)

*Descrição:*

---

## 5. Testes Unitários

| Algoritmo | Caso de teste | Status | Comando para executar |
|-----------|--------------|--------|----------------------|
| | Caso base | ✅ / ❌ | `pytest tests/test_algoritmo.py::test_caso_base` |
| | Grafo vazio | ✅ / ❌ | |
| | Grafo completo | ✅ / ❌ | |

**Como rodar todos os testes:**

```bash
pytest tests/
```

**Resultado atual:**

```
# Cole aqui a saída do pytest / JUnit
```

---

## 6. Histórico de Commits

> Liste os 5+ commits mais relevantes desta entrega.

| Hash (7 chars) | Mensagem | Autor |
|----------------|----------|-------|
| `abc1234` | feat: implementa classe Graph com lista de adjacência | |
| `def5678` | feat: implementa algoritmo Dijkstra | |
| `ghi9012` | test: adiciona testes unitários para Dijkstra | |
| `jkl3456` | feat: leitura de grafo a partir de JSON | |
| `mno7890` | feat: tela de resultado via CLI | |

---

## 7. O que está funcionando / O que ainda falta

| Funcionalidade | Status | Observação |
|---------------|--------|------------|
| Classe do grafo | ✅ Completo | |
| Algoritmo principal | ✅ Completo / 🔄 Parcial | |
| Leitura de arquivo | ✅ Completo / 🔄 Parcial | |
| Tela de entrada | ✅ Completo / 🔄 Parcial | |
| Tela de resultado | ✅ Completo / 🔄 Parcial | |
| Testes unitários | ✅ Completo / 🔄 Parcial | |

---

## Checklist de Entrega

- [ ] Repositório público e acessível
- [ ] .gitignore configurado
- [ ] README com instruções de execução do MVP
- [ ] Algoritmo principal executando sem erros
- [ ] Tela de entrada e tela de resultado demonstráveis
- [ ] 3 testes unitários por algoritmo (mínimo caso base passando)
- [ ] ≥ 5 commits com prefixos semânticos (feat:, fix:, test:, docs:)
- [ ] Ao menos 1 arquivo de grafo de exemplo em `data/`

---

*Teoria dos Grafos — Profa. Dra. Andréa Ono Sakai*
