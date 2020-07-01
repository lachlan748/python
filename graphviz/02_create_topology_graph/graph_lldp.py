#!/usr/bin/env python3

import glob
import re
from pprint import pprint
from graphviz import Digraph, Source

pattern = re.compile('Gi0/|Et[1234]')

device_lldp_neighbors = []

# walk thru files in ./tmp directory
for file_name in glob.glob('../01_discover_lldp_neighs/tmp/*'):
    # device name
    device = file_name.split('/')[3].split('_')[0]
    print("device: " + device)
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = eval(line) #eval the line as list
            for item in line[0]:

                # get ios lldp info
                match = re.findall(r'((\S+)\s+Gi0/[1234])', item)
                if match:
                    for node in match:
                        neigh = node[1].split('.')[0]
                        device_lldp_neighbors.append((device, neigh))
                        print(f"  neighbours: {neigh}")

                # get eos lldp info
                #match = re.findall(r'(Et\d+\s+(\S+))', item)
                #if match:
                #    for node in match:
                #        neigh = node[1].split('.')[0]
                #        device_lldp_neighbors.append((device, neigh))
                #        print(f"  neighbours: {neigh}")



device_lldp_neighbors = list(set(device_lldp_neighbors))

print("*" * 10)
print("Edges: " + str(device_lldp_neighbors))

my_graph = Digraph("My_Network")
my_graph.edge("R5", "veos2")
my_graph.edge("R4", "veos1")

# construct the edge relationships
for neighbors in device_lldp_neighbors:
    node1, node2 = neighbors
    my_graph.edge(node1, node2)

# Insert arbitrary DOT language commands
# such as the rank=same command
source = my_graph.source
original_text = "digraph My_Network {"
new_text = 'digraph My_Network {\n{rank=same R4 veos1 veos2 R5}\n{rank=same R1}\n'
new_source = source.replace(original_text, new_text)
print(new_source)
new_graph = Source(new_source)
new_graph.render("output/lldp_graph.gv")
