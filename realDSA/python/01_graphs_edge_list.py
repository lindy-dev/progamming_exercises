class GraphEdgeList:
    def __init__(self):
        self.edges = [] # Initialize an empty list to hold edge tuples
    
    def add_edge(self, u, v, weight=1):
        # Store the connection as a tuple: (Start Node, End Node, Weight)
        self.edges.append((u, v, weight))
    
    def remove_edge(self, u, v):
        self.edges = [(a, b, w) for a, b, w in self.edges 
                      if not (a == u and b == v)]
    
    def has_edge(self, u, v):
        # Iterate through all edges to see if any match 'u' -> 'v'
        return any(a == u and b == v for a, b, _ in self.edges)
    
    def get_neighbors(self, vertex):
        neighbors = []
        for u, v, w in self.edges:
            if u == vertex:
                neighbors.append((v, w))
            elif not any(a == vertex and b == vertex for a, b, _ in self.edges):  # undirected check
                if v == vertex:
                    neighbors.append((u, w))
        return neighbors
    
    def display(self):
        print("Edge List:")
        for u, v, w in self.edges:
            print(f"{u} -> {v} (weight: {w})")

# Example usage
g = GraphEdgeList()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.display()