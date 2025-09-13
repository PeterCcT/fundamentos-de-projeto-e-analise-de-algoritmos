# Algoritmo de Seleção de Mínimo e Máximo

Algoritmo de seleção de min e max usando divisão e conquista

## Como executar o código

Utilizando qualquer versão do Python 3, execute o comando abaixo no terminal:

```bash
python main.py
```

## Funcionamento teórico

O algoritmo de seleção de mínimo e máximo utiliza a estratégia de divisão e conquista para encontrar, em uma lista de números, o menor e o maior valor com o menor número possível de comparações.

### Passos do algoritmo

1. **Divisão:**
   - Se a lista possui apenas um elemento, esse elemento é tanto o mínimo quanto o máximo.
   - Caso contrário, a lista é dividida em duas metades.
2. **Conquista:**
   - O algoritmo é chamado recursivamente para cada metade, retornando o mínimo e o máximo de cada parte.
3. **Combinação:**
   - O menor valor entre os mínimos das duas metades é o mínimo global.
   - O maior valor entre os máximos das duas metades é o máximo global.

### Exemplo

Para a lista `[3, 4, 5, 3, 1, 2]`, o algoritmo divide a lista, resolve recursivamente e combina os resultados para retornar `(1, 5)`.

## Funcionamento a nível de código

No arquivo `main.py` está implementada a função `get_min_and_max`, que recebe uma lista de números e retorna uma tupla com o menor e o maior valor.

### Análise linha a linha da função principal

**Linha 1:** Definição da função que recebe uma lista de números (int ou float) e retorna uma tupla contendo o valor mínimo e máximo.

```python
def get_min_and_max(values: list[Number]) -> tuple[Number, Number]:
```

**Linhas 2-3:** **Caso base da recursão**. Se a lista possui apenas um elemento, esse elemento é tanto o mínimo quanto o máximo. Esta é a condição de parada que evita um looping infinito.

```python
    if len(values) == 1:
        return values[0], values[0]
```

**Linha 4:** Calcula o índice do meio da lista usando divisão inteira. Para uma lista de tamanho n, isso nos dá a posição n//2, que será usada para dividir a lista em duas partes aproximadamente iguais.

```python
    list_middle_index = len(values) // 2
```

**Linhas 5-6:** **Divisão do problema**. A lista é dividida em duas sublistas:
- `left_values`: contém elementos do índice 0 até o índice do meio
- `right_values`: contém elementos do índice do meio até o final da lista

```python
    left_values = values[:list_middle_index]
    right_values = values[list_middle_index:]
```

**Linhas 7-8:** **Conquista recursiva**. O algoritmo começa as chamadas recursivas:
- `left_result`: tupla (min, max) da metade esquerda
- `right_result`: tupla (min, max) da metade direita

```python
    left_result = get_min_and_max(left_values)
    right_result = get_min_and_max(right_values)
```

**Linha 9:** **Combinação dos resultados**. Compara os mínimos e máximos das duas metades:
- `min(left_result[0], right_result[0])`: o menor entre os dois mínimos
- `max(left_result[1], right_result[1])`: o maior entre os dois máximos

```python
    return min(left_result[0], right_result[0]), max(left_result[1], right_result[1])
```

## Análise de complexidade

### Análise da complexidade assintótica pelo teorema mestre

Se levarmos em consideração o teorema mestre
$$
aT(N/b) + F(N)
$$

Temos que:
- a -> Número de operações recursivas por chamada
- b -> Fator de divisão do tamanho da entrada em cada operação recursiva
- f(n) -> Custo externo, ou seja, se tirar a recursão qual a perfomance do algoritmo?

Dito isso o valor para cada variável seria:
- a -> 2, já que temos duas chamadas recursivas toda vez que o metodo é chamado
- b -> 2, já que a lista é sempre dividida pela metade para cada operação recursiva
- f(n) -> 1, não existe nenhuma operação relevante fora da recursividade

Dito isso, podemos resolver o teorema mestre
$$
T = 2T(N/2) + 1 \\
\text{logo} \\
N^{\log{_2}2} = N
$$

Como F(N) é 1 podemos descartar seu uso e temos no final que a complexidade é O(N) como mostra o resultado do teorema mestre

### Análise da complexidade assintótica pelo método de contagem de operações

Ao todo temos 3 operações no código:

- 1 caso base
- 2 chamadas recursivas

Levando em consideração isso, podemos chegar no seguinte calculo para cada nível de da recursão

$$
f(n) = 1 + 2 \times N
$$

Mas existe um fator intrigante, cada chamada recursiva divide a lista pela metade, então na verdade temos 

$$
f(n) = 1 + 2 \times N/2^k \\
$$

Onde k nada mais é que o nível da recursão, pois se pensarmos bem a cada nível ele está dividindo a lista mais uma vez...Indo um pouco mais a fundo, pensando apenas na analise assintótica a única operação importante para nós seria saber quantas chamadas ocorrem em função de N para cada nível de recursão, se pensarmos assim podemos dizer que temos $2^k$ chamadas por nível, indo mais a fundo teríamos um somatório então 

$$
\sum_{k=1}^{\log{_2}N} 2^k
$$

Se pararmos para analisar esse somatório ele nada mais é que uma progressão geométrica, logo aplicando a fórmula da P.G temos um resultado final de 

$$
Pg = 2(2^k-1) \\
\downarrow \\
Pg = 2(2^{\log{_2}N} -1) \\
\downarrow \\
Pg = 2(N-1) \\
\downarrow \\
Pg = 2N-2
$$

Ou seja, removendo as contantes temos que o resultado final é O(N)

---
