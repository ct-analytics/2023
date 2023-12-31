## Borrowed heavily from https://github.com/wleftwich/aoc/blob/main/2023/10-pipe-maze.ipynb

from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
import sys

sys.setrecursionlimit(15000)

f = "day 10/day10.txt"

with open(f,'r') as input:
    grid = [[x for x in row] for row in input.read().strip().split('\n')]

# pprint(grid)

G = nx.Graph()
starting_pos = None
for i,row in enumerate(grid):
    for j,col in enumerate(row):
        pos = (i+1,j+1)
        if col == "S":
            starting_pos = pos
        else: 
            G.add_node(pos,p=col)

# print(G.nodes)

# pipe_lookup = {
#     "|": [( 0, -1), ( 0, 1)], 
#     "-": [(-1,  0), ( 1, 0)], 
#     "L": [( 0, -1), ( 1, 0)],
#     "J": [( 0, -1), (-1, 0)],
#     "7": [( 0,  1), (-1, 0)],
#     "F": [( 0,  1), ( 1, 0)],
#     "S": [( 0, -1), ( 0, 1), (1, 0), (-1, 0)],
#     ".": [] 
# }

pipe_lookup = {
    "|": [(-1,  0), ( 1,  0)], 
    "-": [( 0, -1), ( 0,  1)], 
    "L": [(-1,  0), ( 0,  1)],
    "J": [(-1,  0), ( 0, -1)],
    "7": [( 1,  0), ( 0, -1)],
    "F": [( 1,  0), ( 0,  1)],
    "S": [( 0, -1), ( 0,  1), (1, 0), (-1, 0)],
    ".": [] 
}

for pos, atts in G.nodes(data=True):
    print(f"Starting node {pos} with pipe {atts["p"]}")
    connections = pipe_lookup[atts["p"]]
    # print(connections)
    for c in connections:
        possible_pos = tuple([pos[i] + c[i] for i in range(2)])
        print(f"    Checking if {possible_pos} is in Grid")
        if possible_pos in G:
            # G.add_edge(pos,possible_pos)
            connecting_node_pipe = G.nodes[possible_pos]["p"]
            # connecting_node_connections = pipe_lookup[connecting_node_pipe]
            # cnc = list(map(lambda x,y:x+y,pipe_lookup[connecting_node_pipe],possible_pos))
            connecting_node_connections = []
            for x in pipe_lookup[connecting_node_pipe]:
                possible_backwards_connection = tuple(map(lambda x,y: x+y, x,possible_pos))
                connecting_node_connections.append(possible_backwards_connection)
            
            print(f"    Backwards connections from {possible_pos} include: {connecting_node_connections}")

            if pos in connecting_node_connections:
                print(f"    Adding edge from {pos} to {possible_pos}")
                G.add_edge(pos, possible_pos)

print(f"Starting node {starting_pos} with pipe S")
G.add_node(starting_pos, p="S")
for d in pipe_lookup['S']:
    # print(f"    Adding {d}")
    possible_pos = tuple([starting_pos[i] + d[i] for i in range(2)])
    print(f"    Checking if {possible_pos} is in Grid")
    if possible_pos in G:
        # print(f"    Adding edge from {pos} to {possible_pos}")
        # G.add_edge(starting_pos, possible_pos)
        connecting_node_pipe = G.nodes[possible_pos]["p"]
        # connecting_node_connections = pipe_lookup[connecting_node_pipe]
        # cnc = list(map(lambda x,y:x+y,pipe_lookup[connecting_node_pipe],possible_pos))
        connecting_node_connections = []
        for x in pipe_lookup[connecting_node_pipe]:
            possible_backwards_connection = tuple(map(lambda x,y: x+y, x,possible_pos))
            connecting_node_connections.append(possible_backwards_connection)
        
        print(f"    Backwards connections from {possible_pos} include: {connecting_node_connections}")

        if starting_pos in connecting_node_connections:
            print(f"    Adding edge from {starting_pos} to {possible_pos}")
            G.add_edge(starting_pos, possible_pos)
                
# for n,d in G.adjacency():
#     pprint(n)
#     pprint(d)
# G.remove_nodes_from(list(nx.isolates(G)))
# nx.draw(G)
# plt.show()
        
# nx.write_network_text(G)

print(f"Furthest distance is {len(nx.find_cycle(G,starting_pos)) // 2}")

# def connect_components(G):
#     # connect up all nodes without crossing loop
#     for node in G:
#         node_d = G.nodes.get(node)
#         if node is None:
#             continue

#         if node_d.get("onloop"):
#             continue

#         # for d in [1, 0 + 1j, -1, 0 - 1j]:
#         for d in [( 0, -1), ( 0,  1), (1, 0), (-1, 0)]:
#             # nabe = node + d
#             nabe = tuple(map(lambda x,y: x+y, node,d))

#             if nabe not in G:
#                 continue

#             nabe_d = G.nodes[nabe]
#             if nabe_d.get("onloop"):
#                 continue

#             G.add_edge(node, nabe)


# def mark_loop_node_neighbors(G, node, inside_rotator):
#     node_d = G.nodes[node]
#     # inside_directions = {node_d["direction"] * inside_rotator, node_d["prev_direction"] * inside_rotator}
#     inside_directions = {tuple(map(lambda x,y: x*y, node_d["direction"],inside_rotator)),
#                          tuple(map(lambda x,y: x*y, node_d["prev_direction"],inside_rotator))}
#     for d in [( 0, -1), ( 0,  1), (1, 0), (-1, 0)]:
#         # nabe = node + d
#         nabe = tuple(map(lambda x,y: x+y, node,d))
#         if nabe not in G:
#             continue

#         nabe_d = G.nodes[nabe]
#         if nabe_d.get("onloop"):
#             continue

#         if d in inside_directions:
#             nabe_d["inside"] = True
            

# def get_inside_rotator(G, node_next):    
#     # leftmost = math.inf + 0j
#     leftmost = (0,math.inf)
#     for node in node_next:
#         # if node.real < leftmost.real:
#         if node[1] < leftmost[1]:
#             leftmost = node
#     leftmost_d = G.nodes[leftmost]
#     leftmost_directions = leftmost_d["direction"], leftmost_d["prev_direction"]
#     # if 1j in leftmost_directions:
#     #     inside_rotator = 0-1j
#     # elif -1j in leftmost_directions:
#     #     inside_rotator = 0+1j
#     # else:
#     #     raise ValueError("Can't happen")
#     # return inside_rotator

#     if (1,0) in leftmost_directions:
#         inside_rotator = (-1,0)
#     elif (-1,0) in leftmost_directions:
#         inside_rotator = (1,0)
#     else:
#         raise ValueError("Can't happen...")
#     return inside_rotator
    

# def set_directions(G, node, nxt, prv):
#     D = G.nodes[node]
#     D["onloop"] = True
#     # D["direction"] = nxt - node
#     D["direction"] = tuple(map(lambda x,y: x-y, nxt,node))
#     # D["prev_direction"] = node - prv   
#     D["prev_direction"] = tuple(map(lambda x,y: x-y, node,prv)) 


# loop = nx.find_cycle(G, starting_pos)

# node_next = {}
# node_prev = {}
# for a, b in loop:
#     node_next[a] = b
#     node_prev[b] = a

# for node, nxt in node_next.items():
#     prv = node_prev[node]
#     set_directions(G, node, nxt, prv)

# inside_rotator = get_inside_rotator(G, node_next)

# for node in node_next:
#     mark_loop_node_neighbors(G, node, inside_rotator)

# connect_components(G)
# inside_count = 0
# for cc in nx.connected_components(G):
#     for node in cc:
#         if G.nodes[node].get("inside"):
#             inside_count += len(cc)
#             break 


# https://github.com/savbell/advent-of-code-one-liners/blob/master/2023/day-10.py
# grid = [[x for x in row] for row in q[10].strip().split('\n')]
pipe_map = {'|': [(0, -1), (0, 1)], '-': [(1, 0), (-1, 0)], 
            'L': [(0, -1), (1, 0)], 'J': [(0, -1), (-1, 0)], 
            '7': [(0, 1), (-1, 0)], 'F': [(0, 1), (1, 0)], 
            '.': [], 'S': [(0, -1), (0, 1), (1, 0), (-1, 0)]}

def find_valid_moves(grid, pos, pipe_map, prev_dir=None):
    char = grid[pos[1]][pos[0]]
    valid_directions = pipe_map[char]
    valid_moves = []
    for d in valid_directions:
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        new_char = grid[new_pos[1]][new_pos[0]]
        if 0 <= new_pos[0] < len(grid[0]) and 0 <= new_pos[1] < len(grid):
            if d == (0, -1) and (0, 1) in pipe_map[new_char] and prev_dir != (0, 1):
                valid_moves.append(new_pos)
            if d == (0, 1) and (0, -1) in pipe_map[new_char] and prev_dir != (0, -1):
                valid_moves.append(new_pos)
            if d == (1, 0) and (-1, 0) in pipe_map[new_char] and prev_dir != (-1, 0):
                valid_moves.append(new_pos)
            if d == (-1, 0) and (1, 0) in pipe_map[new_char] and prev_dir != (1, 0):
                valid_moves.append(new_pos)
    return valid_moves

def find_start_char(grid, pos, pipe_map):
    valid_moves = find_valid_moves(grid, pos, pipe_map)
    valid_directions = [(x[0]-pos[0], x[1]-pos[1]) for x in valid_moves]
    for k, v in pipe_map.items():
        if v == valid_directions:
            return k

def solve(grid, pos, pipe_map, visited, prev_dir=None):
    move = find_valid_moves(grid, pos, pipe_map, prev_dir)[0]
    if move == start_pos and len(visited) > 0:
        return visited
    visited.add(move)
    return solve(grid, move, pipe_map, visited, (move[0]-pos[0], move[1]-pos[1]))

start_pos = [(x, y) for y, row in enumerate(grid) for x, char in enumerate(row) if char == 'S'][0]
grid[start_pos[1]][start_pos[0]] = find_start_char(grid, start_pos, pipe_map)
visited = solve(grid, start_pos, pipe_map, { start_pos })

contained = set()
for i in range(len(grid)):
    within = 0
    for j in range(len(grid[0])):
        if (j, i) in visited:
            if grid[i][j] in ['|', 'L', 'J']:
                within = not within
        elif within:
            contained.add((j, i))

print(f"The number of nodes inside the loop is {len(contained)}.")

# 5600 is too high