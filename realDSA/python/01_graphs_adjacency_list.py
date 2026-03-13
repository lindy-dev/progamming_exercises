from collections import defaultdict

class Graph:
    def __init__(self):
        # Dictionary to store the graph: {node: [list of neighbours]}
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """Adds a directed edge from u to v."""
        self.graph[u].append[v]

    def add_undirected_edge(self, u, v):
        """Adds an undirected edge (both directions)."""
        self.add_edge(u, v)
        self.add_edge(v, u)

    def get_neighbours(self, vertex):
        """Returns a list of neighbors for a specific vertex."""
        return self.graph.get(vertex, [])

    def print_graph(self):
        """Prints the adjacency list representation."""
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

# --- Usage Example ---
if __name__ == "__main__":
    g = Graph()
    
    # Create a graph: A->B, A->C, B->D
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    
    print("Graph Structure:")
    g.print_graph()

    # Check neighbors of 'A'
    print(f"\nNeighbors of A: {g.get_neighbors('A')}")
