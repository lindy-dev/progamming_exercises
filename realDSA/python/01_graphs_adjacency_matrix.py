class GraphMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices # Store total number of nodes
        # Create a square grid filled with zeros. 
        # Outer list creates rows, inner list comprehension creates columns.
        self.matrix = [[0 for _ in range(num_vertices)] 
                       for _ in range(num_vertices)]
    
    def add_edge(self, u, v, directed=False):
        self.matrix[u][v] = 1 # Mark the cell at row 'u', column 'v' as connected
        if not directed:
            # If undirected, the connection goes both ways (symmetric matrix)
            self.matrix[v][u] = 1
    
    def remove_edge(self, u, v, directed=False):
        self.matrix[u][v] = 0
        if not directed:
            self.matrix[v][u] = 0
    
    def has_edge(self, u, v):
        return bool(self.matrix[u][v])
    
    def get_neighbors(self, vertex):
        # Iterate through all possible column indices for this specific row
        return [i for i in range(self.num_vertices) 
                if self.matrix[vertex][i] == 1] # Return index 'i' only if there is a connection (1)
    
    def display(self):
        print("Adjacency Matrix:")
        for row in self.matrix: # Loop through each row of the grid
            print(row) # Print the entire row list

# Example usage
g = GraphMatrix(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.display()