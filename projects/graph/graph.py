"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Stack(): #FIFO 
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0: 
            return self.stack.pop()
        else:
            return None 
    def size(self):
        return len(self.stack)

class Queue(): #lifo 
    def __init__(self):
        self.queue = []
        #adding to the tail 
    def enqueue(self, value):
        self.queue.append(value)
        #deque is removing head 
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None 
    def size(self):
        return len(self.queue)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v_from, v_to):
        if v_from in self.vertices and v_to in self.vertices:
           self.vertices[v_from].add(v_to)
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        q = Queue()
        visited = set()

        # init: 
        q.enqueue(starting_vertex) #adds starting node to tail of list 

        #while queue isn't empty
        while q.size() > 0: 
            v = q.dequeue() #removes item from the end of the list 
            if v not in visited: #checks if the tiem is in the set
                print(v)

                visited.add(v)  #add to set 

                for neighor in self.get_neighbors(v):
                    q.enqueue(neighor) #add each neighbor to the end of the queue 

    def dft(self, starting_vertex):
        q = Stack() #fifo 
        visited = set() #visited list 

        q.push(starting_vertex) # add to head 

        while q.size() > 0:
            v = q.pop() #remove last item 

            if v not in visited:
                print(v)

                visited.add(v) #add to visit list first 

                for neighbor in self.get_neighbors(v):
                    q.push(neighbor) #add to head of neighbors list 


    def dft_recursive(self, starting_vertex, stack = Stack(), visited=set()):
        if starting_vertex not in visited: #check if the item is in the visited set
            print(starting_vertex) #print to pass test 
            visited.add(starting_vertex)#adds item to set 
            for neighbor in self.get_neighbors(starting_vertex): #find all of the neighbors for this point 
                self.dft_recursive(neighbor, stack, visited)#run recursion on all of neighbors 

   

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        path =  Queue() #create a que lifo 
        path.enqueue([starting_vertex]) #create a list by adding it to head 
        visited = set() #create empty set to add too 
        while path.size() > 0: #while path is existent 
            new_path = path.dequeue() #remove head of the path and cast to variable. this is a list. 
            edge = new_path[-1] #check last item in the variable list 
            if edge not in visited: #if edge is not in viisted add to list 
                if edge is destination_vertex: #if edge is the destination return path 
                    return new_path
                visited.add(edge)
                for neighbor in self.get_neighbors(edge): #loop through nieghbors of edge creat new path then add new path to head 
                    #of original path 
                    path_copy = new_path.copy()
                    path_copy.append(neighbor)
                    path.enqueue(path_copy)




        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        path = Stack() #start up empty stack 
        path.push([starting_vertex]) #add start point as list 
        visited = set() #create empty set 
        while path.size() > 0: #while stack exist 
            new_path = path.pop() #remove tail of the path and cash a variable to it as a list 
            edge = new_path[-1] #check the last item in the variable list 
            if edge not in visited: #if last item isnt in visited
                if edge is destination_vertex: #checks if the last item is the destination 
                    return new_path
                visited.add(edge) #add edge to visisted list 
                for neighbor in self.get_neighbors(edge): #for all the neighbors from this last point
                    path_copy = new_path.copy() #not sure why this fixed an error 
                    path_copy.append(neighbor) #add the neighbor to the eend of the list 
                    path.push(path_copy) #add that end of stack 


    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited.insert(starting_vertex) #Add starting point to visited set.
        path = path + [starting_vertex] #Add starting point to path list.
        if starting_vertex == destination_vertex: #Check if starting point is the destination.
            return path #Return the path list (needs to be a list to pass test.)
        for neighbor in self.get_neighbors(starting_vertex): #Generates a list of all neighbors.
            if neighbor not in visited: #Checks if neighbor is already in visited set.
                newpath = self.dfs_recursive(neighbor, destination_vertex, visited, path) #Performs recursion on each neighbor not already in the list.
                if newpath is not None: #Checks that recursion for content.
                    return newpath  #Returns those that have something.
            

            


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
