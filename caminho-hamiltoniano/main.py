from typing import List, Optional
from directed_graph import DirectedGraph
from undirected_graph import UndirectedGraph
from graph import Graph


def find_hamiltonian_path(graph: Graph, path: List[int], visited: List[bool]) -> Optional[List[int]]:
    if len(path) == graph.num_vertices:
        return path.copy()
    current_vertex = path[-1] if path else 0
    for neighbor in graph.get_neighbors(current_vertex):
        if not visited[neighbor]:
            visited[neighbor] = True
            path.append(neighbor)
            result = find_hamiltonian_path(graph, path, visited)
            if result is not None:
                return result
            path.pop()
            visited[neighbor] = False
    return None


def hamiltonian_path(graph: Graph) -> Optional[List[int]]:
    for start_vertex in range(graph.num_vertices):
        visited = [False] * graph.num_vertices
        visited[start_vertex] = True
        path = [start_vertex]
        result = find_hamiltonian_path(graph, path, visited)
        if result is not None:
            return result
    return None


print('Ex 1: Undirected Graph')
undirected = UndirectedGraph(5)
undirected.add_edge(0, 1)
undirected.add_edge(1, 2)
undirected.add_edge(2, 3)
undirected.add_edge(3, 4)
undirected.add_edge(4, 0)
undirected.add_edge(1, 4)

print('Graph:')
print(undirected)
print('\nHamiltonian Path found:', hamiltonian_path(undirected))

# Exemplo de uso com grafo direcionado
print('\nEx 2: Directed Graph')
directed = DirectedGraph(4)
directed.add_edge(0, 1)
directed.add_edge(1, 2)
directed.add_edge(2, 3)
directed.add_edge(0, 2)

print('Graph:')
print(directed)
print('\nHamiltonian Path found:', hamiltonian_path(directed))

print('\nEx 3: No Hamiltonian Path')
no_path = UndirectedGraph(4)
no_path.add_edge(0, 1)
no_path.add_edge(2, 3)

print('Graph:')
print(no_path)
print('\nHamiltonian Path found:', hamiltonian_path(no_path))
