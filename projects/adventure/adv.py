from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

def opposite(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'w':
        return 'e'
    else:
        return 'w'

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
traversal_graph = {
    0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}

while len(traversal_graph) < len(room_graph):
    valid_directions = []
    if '?' in traversal_graph[player.current_room.id]:
        for x in player.current_room.get_exits():
            if traversal_graph[player.current_room.id][x] == '?':
                valid_directions.append(x)
    else:
        for x in player.current_room.get_exits():
            if traversal_graph[player.current_room.id][x] is not None:
                valid_directions.append(x)

    direction = random.choice(valid_directions)
    prev_room = player.current_room
    
    player.travel(direction)

    if player.current_room == prev_room:
        traversal_graph[player.current_room.id][direction] = None
    else:
        traversal_graph[prev_room.id][direction] = player.current_room.id
        if player.current_room.id not in traversal_graph:
            traversal_graph[player.current_room.id] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
        traversal_graph[player.current_room.id][opposite(direction)] = prev_room.id
        traversal_path.append(direction)


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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
