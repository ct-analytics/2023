from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

f = "day 10/day10.txt"

with open(f,'r') as input:
    grid = [[x for x in row] for row in input.read().strip().split('\n')]

pipe_map = {}

pprint(grid)

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
    print(f"    Adding {d}")
    possible_pos = tuple([starting_pos[i] + d[i] for i in range(2)])
    print(f"    Checking if {possible_pos} is in Grid")
    if possible_pos in G:
        G.add_edge(starting_pos, possible_pos)
        # connecting_node = G.nodes[possible_pos]["t"]
        # connecting_node_connections = pipe_lookup[connecting_node]
        # if d in connecting_node_connections:
        #     G.add_edge(starting_pos, possible_pos)
                
# for n,d in G.adjacency():
#     pprint(n)
#     pprint(d)

# nx.draw(G)
# plt.show()
        
nx.write_network_text(G)

print(f"Furthest distance is {len(nx.find_cycle(G,starting_pos)) // 2}")