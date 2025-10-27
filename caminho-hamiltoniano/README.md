# Algoritmo de Caminho Hamiltoniano

Implementação de um algoritmo para encontrar caminhos hamiltonianos em grafos orientados e não orientados usando backtracking.

## Como executar o código

Utilizando qualquer versão do Python 3, execute o comando abaixo no terminal:

```bash
python main.py
```

## Funcionamento teórico

Um **caminho hamiltoniano** é um caminho em um grafo que visita cada vértice exatamente uma vez. Diferente do ciclo hamiltoniano, o caminho não precisa retornar ao vértice inicial.

O algoritmo utiliza a técnica de **backtracking** para explorar todas as possibilidades de caminhos no grafo, eliminando ramos que não podem levar a uma solução válida.

### Passos do algoritmo

1. **Escolha do vértice inicial:**
   - O algoritmo tenta começar a partir de cada vértice do grafo.

2. **Exploração recursiva:**
   - A partir do vértice atual, tenta visitar cada vizinho ainda não visitado.
   - Marca o vizinho como visitado e adiciona ao caminho.
   - Chama recursivamente o algoritmo para continuar construindo o caminho.

3. **Verificação da solução:**
   - Se o tamanho do caminho é igual ao número de vértices, encontrou um caminho hamiltoniano.

4. **Backtracking:**
   - Se um caminho não leva a uma solução, remove o último vértice adicionado.
   - Marca o vértice como não visitado e tenta o próximo vizinho.

### Exemplo

Para um grafo com 5 vértices conectados em ciclo (0-1-2-3-4-0), o algoritmo pode encontrar o caminho `[0, 1, 2, 3, 4]`, visitando cada vértice exatamente uma vez.

## Funcionamento a nível de código

No arquivo `main.py` estão implementadas as funções `find_hamiltonian_path` e `hamiltonian_path`, que utilizam backtracking para encontrar um caminho hamiltoniano no grafo.

### Análise linha a linha da função auxiliar (find_hamiltonian_path)

**Linha 1:** Definição da função que recebe o grafo, o caminho atual e o array de visitados, retornando uma lista com o caminho ou None.

```python
def find_hamiltonian_path(graph: Graph, path: List[int], visited: List[bool]) -> Optional[List[int]]:
```

**Linhas 2-3:** **Caso base da recursão**. Se o caminho contém todos os vértices do grafo, encontramos um caminho hamiltoniano válido. Retorna uma cópia do caminho para evitar modificação.

```python
    if len(path) == graph.num_vertices:
        return path.copy()
```

**Linha 4:** Obtém o último vértice do caminho atual. Se o caminho estiver vazio (caso inicial), usa o vértice 0.

```python
    current_vertex = path[-1] if path else 0
```

**Linha 5:** Inicia a exploração de todos os vizinhos do vértice atual.

```python
    for neighbor in graph.get_neighbors(current_vertex):
```

**Linhas 6-8:** Verifica se o vizinho ainda não foi visitado. Se válido, marca como visitado e adiciona ao caminho.

```python
        if not visited[neighbor]:
            visited[neighbor] = True
            path.append(neighbor)
```

**Linhas 9-13:** **Chamada recursiva**. Tenta construir o resto do caminho a partir deste novo estado. Se encontrar uma solução válida, retorna imediatamente.

```python
            result = find_hamiltonian_path(graph, path, visited)
            
            if result is not None:
                return result
```

**Linhas 14-16:** **Backtracking**. Se a exploração não levou a uma solução, desfaz as mudanças, ou seja, remove o vértice do caminho e marca como não visitado pra tentar outras possibilidades.

```python
            path.pop()
            visited[neighbor] = False
```

**Linha 17:** Se nenhum vizinho levou a uma solução, retorna None indicando que não tem caminho hamiltoniano a partir desse estado.

```python
    return None
```

### Análise linha a linha da função principal (hamiltonian_path)

**Linha 1:** Definição da função que recebe um grafo e retorna um caminho hamiltoniano ou None.

```python
def hamiltonian_path(graph: Graph) -> Optional[List[int]]:
```

**Linha 2:** Itera sobre todos os vértices do grafo como possíveis pontos de partida.

```python
    for start_vertex in range(graph.num_vertices):
```

**Linhas 3-5:** Inicializa as estruturas de dados para esta tentativa:
- `visited`: array booleano para rastrear vértices visitados
- `path`: lista iniciando com o vértice de partida

```python
        visited = [False] * graph.num_vertices
        visited[start_vertex] = True
        path = [start_vertex]
```

**Linhas 6-8:** Chama a função auxiliar de busca. Se encontrar um caminho válido, retorna imediatamente.

```python
        result = find_hamiltonian_path(graph, path, visited)
        if result is not None:
            return result
```

**Linha 9:** Se nenhum vértice inicial levou a um caminho hamiltoniano, retorna None.

```python
    return None
```

## Relatório

### Análise da complexidade computacional: Classes P, NP, NP-Completo e NP-Difícil

O problema do Caminho Hamiltoniano pertence à classe **NP-Completo**.

**Justificativa:**

1. **Pertence a NP:** Dado um caminho candidato, podemos verificar em tempo polinomial se ele é um caminho hamiltoniano válido. Basta verificar se:
   - Todos os vértices aparecem exatamente uma vez O(n)
   - Cada passada no caminho corresponde a uma aresta válida no grafo O(n)

2. **É NP-Difícil:** O problema do Caminho Hamiltoniano é pelo menos tão difícil quanto qualquer problema em NP. Ele pode ser reduzido ao Problema do Ciclo Hamiltoniano (também NP-Completo) e vice-versa.

3. **Relação com o Problema do Caixeiro Viajante:**
   - O Caixeiro Viajante é NP-Difícil e sua versão de decisão é NP-Completo.
   - O Caminho Hamiltoniano é um caso especial onde:
     - Todas as arestas têm peso 1
     - Buscamos um caminho (não ciclo) de custo n-1
   - Podemos reduzir o Caminho Hamiltoniano ao caixeiro, provando sua NP-Completude.

**Implicação:** Não se conhece algoritmo polinomial para resolver este problema. A melhor abordagem conhecida tem complexidade exponencial no pior caso.

### Análise da complexidade assintótica de tempo

A complexidade temporal do algoritmo de backtracking implementado é **O(n!)** no pior caso, onde n é o número de vértices.

**Método utilizado:** Contagem de operações e análise de árvore de recursão.

**Explicação:**

1. **Árvore de decisão:**
   - No primeiro nível, temos até n escolhas (vértices iniciais)
   - No segundo nível, temos até (n-1) escolhas para cada ramo
   - No terceiro nível, temos até (n-2) escolhas
   - E assim sucessivamente até chegar a 1 escolha

2. **Número total de nós explorados:**
$$
n \times (n-1) \times (n-2) \times ... \times 1 = n!
$$

3. **Trabalho em cada nó:**
   - Verificar vizinhos: O(grau do vértice) ≤ O(n)
   - Operações de marcação e desmarcação: O(1)
   - Cópia do caminho (caso base): O(n)

4. **Complexidade total:**
$$
T(n) = O(n!) \times O(n) = O(n \times n!)
$$

Simplificando para notação assintótica, temos: **O(n!)**

### Aplicação do Teorema Mestre

**Não é possível aplicar o Teorema Mestre** ao algoritmo de Caminho Hamiltoniano.

**Justificativa:**

O Teorema Mestre se aplica a relações de recorrência da forma:
$$
T(n) = aT(n/b) + f(n)
$$

Onde:
- a ≥ 1 (número de subproblemas)
- b > 1 (fator de divisão do tamanho do problema)
- f(n) é o custo de dividir e combinar

**Por que não se aplica:**

1. **Não há divisão do problema em subproblemas de tamanho proporcional:** O algoritmo não divide o problema em partes menores de tamanho n/b. Em vez disso, explora n diferentes caminhos, cada um reduzindo o problema em apenas 1 vértice.

2. **Estrutura de ramificação variável:** O número de chamadas recursivas varia em cada nível (n, n-1, n-2, ...), não é constante como requer o Teorema Mestre.

3. **Forma da recorrência:** A recorrência do algoritmo é:
$$
T(n) = n \times T(n-1) + O(n)
$$

Ou seja, é uma problema onde não se aplica divisão e conquista.

### Análise dos casos de complexidade

#### Melhor caso: O(n)

Ocorre quando o primeiro vértice testado já forma um caminho hamiltoniano válido seguindo sempre o primeiro vizinho disponível.

**Exemplo:** Grafo em linha (0-1-2-3-4), começando do vértice 0.

**Impacto:** Extremamente raro em grafos aleatórios. Representa a situação ideal onde não há backtracking.

#### Caso médio e pior caso: O(n!)

Ocorre quando o algoritmo precisa explorar todas as permutações de vértices antes de encontrar um caminho (ou concluir que não existe).

Dito isso, isso apenas destaca o por que o problema é NP-Completo e por que, na prática, são usadas algoritmos aproximados para grafos grandes, sacrificando a garantia de encontrar a solução ótima em favor de tempo de execução razoável.

---
