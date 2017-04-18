# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 21:06:15 2017

@author: qiangwennorge
"""

# Generate links between each nodes, the format of the output
# will be: G = {Node1:{NeighborNode1:1,NeighborNode2:1...}...}
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

# Traverse the graph, if the node is traversed, then 'marked' will be set True
# The order of the visit will also be added
def dfs_traversal(G, start, traversed = {}, traversalord = 0, s = []):
    s.append(start)
    while s:
        current = s.pop()
        if current not in traversed:
            traversed[current] = {}
            traversalord += 1
            traversed[current]['marked'] = True
            traversed[current]['order'] = traversalord
            s.extend([node for node in G[current] if node not in traversed and node not in s])
    return traversed


# Examples for generating a graph
edges = [('a', 'g'), ('a', 'd'), ('g', 'c'), ('g', 'd'), ('a','b'), ('b','e'),('d','f')]
edges2 = [('a','b'),('a','e'),('b','f'),('b','g'),('b','h'),('c','e'),('c','f'),('d','g'),('d','h'),
          ('e','f'),('e','i'),('f','j'),('i','j')]
G = {}
for v1, v2 in edges:
    make_link(G, v1, v2)

# Print the traversed graph after DFS by starting at given node.
print dfs_traversal(G, 'a')
