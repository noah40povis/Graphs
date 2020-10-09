

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
            raise IndexError("Nonexistent vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
    
    def find_earliest_ancestor(self, start):
        #create a list for a stack
        stack = []
        #append the the starting node as a list to the stack because we will be takiing mulitiple nodes
        stack.append([start]) #two dimensional array 
        #create a set 
        visited = set()
        #path is a one dimensional array 
        path = [start]
        while len(stack) > 0:
            #pop is pulling the start value out of the arrray and saving it into the innerpath variable 
            innerpath = stack.pop() #popping the last element from the stack list to get the vertex
            vertex = innerpath[-1] #set vertex to innerpath 
            if vertex not in visited: #if vertex not in visited add it to it 
                visited.add(vertex)

                #for neighbors in vertex 
                for next_vertex in self.get_neighbors(vertex): 
                    #make copy path 
                    path_copy = list(innerpath)
                    #append neighbors to path copy 
                    path_copy.append(next_vertex)
                    #then append path copy to stack which is just adding them to the stack list 
                    stack.append(path_copy)
                    #if the path copy is greater than the original path switch original path to the new path
                    if len(path_copy) > len(path):
                        path = path_copy
                    #if the path copy is equal length of the path and the path copy last element does not equal
                    # the last element of the original path make path copy the new path 
                    if len(path_copy) == len(path) and path_copy[-1] != path[-1]:
                        path = path_copy


        return path 




def earliest_ancestor(ancestors, starting_node):
    # #made stackl 
    # stack = []
    # #append startin node 
    # stack.append(starting_node)
    # visited = set()
    # visited.add(starting_node)
    #^^ dont reallly need

    #make graph 
    ancestor_graph = Graph()
    #make your graph 
    for pair in ancestors: 
        ancestor_graph.add_vertex(pair[0])
        ancestor_graph.add_vertex(pair[1])

    #had to split up these two for loops because it was return an error 
    for pair in ancestors:
        ancestor_graph.add_edge(pair[1], pair[0])
    
    ancestor = ancestor_graph.find_earliest_ancestor(starting_node)
    if ancestor[-1] == starting_node:
        return -1 
    else:
        return ancestor[-1] 