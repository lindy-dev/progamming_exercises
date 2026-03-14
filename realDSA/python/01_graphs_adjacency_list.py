# Adjacency list implementation 
# takes into account edge weights 

class Vertex: 
    def __init__(self, key):
        self.key = key
        self.neighbours = {}

    def get_neighbour(self, other):
        return self.neighbours.get(other, None)
    
    def set_neighbour(self, other, weight = 0):
        self.neighbours[other] = weight

    def __str__(self):
        return (
            f"{self.key} connected to: " + 
            f"{[x.key for x in self.neighbours]}"
        )
    def __repr__(self):
        return f"Vertex ({self.key}) "
    
    def get_neighbours(self):
        return self.neighbours.keys()
    
    def get_key(self):
        return self.key 
    


class Graph:
    def __init__(self):
        self.vertices = {}

    def set_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def get_vertex(self, key):
        return self.vertices.get(key, None)
    
    def __contains__(self, key):
        return key in self.vertices
    
    def add_edge(self, from_vert, to_vert, weight=0):
        if from_vert not in self.vertices:
            self.set_vertex(from_vert)

        if to_vert not in self.vertices:
            self.set_vertex(to_vert)

        self.vertices[from_vert].set_neighbour(
            self.vertices[to_vert], weight
        )

    def get_vertices(self):
        return self.vertices.keys()
    
    def __iter__(self):
        return iter(self.vertices.values())


# Example usage
g = Graph()
for i in range(6):
    g.set_vertex(i)

print(g.vertices)

g.add_edge(0,1,5)
g.add_edge(0,5,2)
g.add_edge(1,2,4)
g.add_edge(2,3,9)
g.add_edge(3,4,7)
g.add_edge(3,5,3)
g.add_edge(4,0,1)
g.add_edge(5,4,8)
g.add_edge(5,2,1)

for v in g:
    for w in v.get_neighbours():
        print(f"({v.get_key()}, {w.get_key()})")

