# -*- coding: utf-8 -*-
"""
Created on April 23 18:33 2017

@author: qiangwennorge
"""

def make_link(G, node1, node2, weight):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G

def shortest_dist_node(dist):
    best_node = 'undefined'
    best_value = 100000
    for v in dist:
        if dist[v] < best_value:
            (best_node,best_value) = (v,dist[v])
    return best_node


def dijkstra(G,v):
    dist_so_far = {}
    dist_so_far[v] = 0
    final_dist = {}
    while len(final_dist) < len(G):
        w = shortest_dist_node(dist_so_far)
        # lock it down!
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                elif final_dist[w] + G[w][x] < dist_so_far[x]:
                    dist_so_far[x] = final_dist[w] + G[w][x]
    return final_dist

(a,b,c,d,e,f,g,h,i,j) = ('A','B','C','D','E','F','G','H','I','J')
triples = ((a,c,3),(c,b,10),(a,b,15),(d,b,9),(a,d,4),(d,f,7),(d,e,3),
           (e,g,1),(e,f,5),(f,g,2),(b,f,1),(h,i,3),(a,i,8),(b,h,2),(d,j,7))

G = {}

for (i,j,k) in triples:
    make_link(G,i,j,k)

print dijkstra(G,a)