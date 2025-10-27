from graph import Graph


class DirectedGraph(Graph):    
    def add_edge(self, source_vertex: int, vertex: int) -> None:
        if vertex not in self.adjacency_list[source_vertex]:
            self.adjacency_list[source_vertex].append(vertex)
    
    def get_in_degree(self, vertex: int) -> int:
        degree = 0
        for i in range(self.num_vertices):
            if vertex in self.adjacency_list[i]:
                degree += 1
        return degree

    def get_out_degree(self, vertex: int) -> int:
        return len(self.adjacency_list[vertex])
    
    def get_num_edges(self) -> int:
        return sum(len(adj) for adj in self.adjacency_list.values())
