from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "/Users/noahchristian/Documents/Graphs/projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = [] 
graph = {}
opposite = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
back_track_path = []
player = Player(world.starting_room)
visited = set()
def generate_traversal():
    #Create while loop while set is less than the graph size 
    while len(room_graph)>len(visited):
        #Create a variable for the current room (starts at starting room) 
        current_room = player.current_room.id
        #If this current room is not in visited 
        if current_room not in visited:  
            #find possible exits and mark them with ?
            room_exits = {direction: '?' for direction in player.current_room.get_exits()} 
            #now populate the graph with the room exits
            graph[current_room] = room_exits
            #next we add the room to the visited set
            visited.add(player.current_room.id)
        #if there are any directions in the back track path log
        if any(back_track_path):
            #set the backtrackpath of the current_room index in the graph , as the possible room_exits 
            graph[current_room][back_track_path[-1]] = prev_room 
        #find the unexplored irections in the current room 
        unexplored_directions = []
        #for key, value in the graph at the specified current_room.items 
        for key,value in graph[current_room].items():
            # if the room has a '?' 
            if value == '?':
                #append the key (direction) to list 
                unexplored_directions.append(key)
        #now lets have the player travel 
        #if there are any unexplored directions in the current room
        if len(unexplored_directions) > 0:
            random_direction = random.choice(unexplored_directions)
            #first we need to set assign the current room as the previous room
            prev_room = player.current_room.id  
            #move the player 
            player.travel(random_direction)
            #assign next_room to new room id after the move
            next_room = player.current_room.id
            #add room to graph 
            graph[prev_room][random_direction] = next_room
            #finally append the random direction in the traveersal path 
            traversal_path.append(random_direction)
            #append to backtrack log the value of the random direction key in the opposite dict 
            back_track_path.append(opposite[random_direction])
        else:
            if len(unexplored_directions) == 0:
                #move in the opposite_direction 
                opposite_direction = back_track_path[-1]
                prev_room = player.current_room.id 
                #move player 
                player.travel(opposite_direction)
                #set next room
                next_room = player.current_room.id
                #add room to graph 
                graph[prev_room][random_direction] = next_room
                #remove from the back track from the log so you dont go that way again 
                back_track_path.pop()
                #track the direction 
                traversal_path.append(opposite_direction)
    return graph 


generate_traversal()


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
