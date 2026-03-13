class GraphIncidence:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []
    
    def add_edge(self, u, v, directed=False):
        edge_id = len(self.edges)
        row = [0] * (edge_id + 1)
        if directed:
            row[u] = -1
            row[v] = 1
        else:
            row[u] = 1
            row[v] = 1
        self.edges.append(row)
    
    def get_incidence_matrix(self):
        matrix = [[0 for _ in range(len(self.edges))] 
                  for _ in range(self.num_vertices)]
        for edge_idx, edge in enumerate(self.edges):
            for vertex_idx, val in enumerate(edge):
                if val != 0:
                    matrix[vertex_idx][edge_idx] = val
        return matrix
    
    def display_matrix(self):
        print("Incidence Matrix:")
        matrix = self.get_incidence_matrix()
        for row in matrix:
            print(row)

# Example usage
g = GraphIncidence(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.display_matrix()