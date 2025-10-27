from abc import ABC, abstractmethod
from typing import List, Dict


class Graph(ABC):
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adjacency_list: Dict[int, List[int]] = {i: [] for i in range(num_vertices)}
    
    @abstractmethod
    def add_edge(self, u: int, v: int) -> None:
        pass
    
    def remove_edge(self, u: int, v: int) -> None:
        if v in self.adjacency_list[u]:
            self.adjacency_list[u].remove(v)
    
    def get_neighbors(self, v: int) -> List[int]:
        return self.adjacency_list[v]
    
    def get_degree(self, v: int) -> int:
        return len(self.adjacency_list[v])
    
    def __str__(self) -> str:
        result = []
        for vertex in range(self.num_vertices):
            neighbors = ', '.join(map(str, self.adjacency_list[vertex]))
            result.append(f"{vertex}: [{neighbors}]")
        return '\n'.join(result)
