from graph import Graph


class UndirectedGraph(Graph):
    def add_edge(self, source_vertex: int, vertex: int) -> None:
        if vertex not in self.adjacency_list[source_vertex]:
            self.adjacency_list[source_vertex].append(vertex)
        if source_vertex not in self.adjacency_list[vertex]:
            self.adjacency_list[vertex].append(source_vertex)

    def remove_edge(self, source_vertex: int, vertex: int) -> None:
        if source_vertex in self.adjacency_list[vertex]:
            self.adjacency_list[vertex].remove(source_vertex)

    def get_num_edges(self) -> int:
        return sum(len(adj) for adj in self.adjacency_list.values()) // 2
