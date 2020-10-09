import random
import math 

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
    
    def populate_graph(self, num_users, avg_friendships):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        random.shuffle(possible_friendships)
        for i in range(0, math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
    
   


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  

        #instatiate empty que 
        queue = []
        #add user to que 
        queue.append([user_id])

        #while queue is greter than 0
        while queue:
            #find the first list in the que 
            current_user = queue.pop(0)
            #grab last item in list 
            current_vertex = current_user[-1]
            #if current vertex which is a node is not in the visited dic: 
            if current_vertex not in visited:
                #add it as the key and the path from the starting node as the value 
                visited[current_vertex] = current_user
                #find all the friends of that node 
                for friend in self.friendships[current_vertex]:
                    if friend not in visited: #check if friends are in the visited 
                        new_path = current_user.copy() #if not make a copy of the path to it 
                        new_path.append(friend) #add the current friend to that path 
                        queue.append(new_path)  add that path to the queue 
       #when the queue is exhausted return the dict 
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
