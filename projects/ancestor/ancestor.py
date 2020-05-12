from util import Queue

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)   

        else:
            raise IndexError('Vertex does not exist in graph')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

def earliest_ancestor(ancestors, starting_node):
    family_tree = Graph()

    for ancestor in ancestors:
        if ancestor[0] not in family_tree.vertices:
            print(ancestor[0])
            family_tree.add_vertex(ancestor[0])

    for relationship in ancestors:
        family_tree.add_edge(ancestor[1], ancestor[0])

    queue = Queue()
    queue.enqueue(starting_node)

    visited = set()
    result = -1

    while queue.size() > 0:
        node = queue.dequeue()

        if node not in visited:
            visited.add(node)
            
            if family_tree.get_neighbors(node):
                for next_node in family_tree.get_neighbors(node):
                    queue.enqueue(next_node)
            else:
                result = node