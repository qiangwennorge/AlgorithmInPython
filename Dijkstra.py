# -*- coding: utf-8 -*-
"""
Created on April 23 18:33 2017

@author: qiangwennorge
"""

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
    while len(final_dist) < len(G)
        w = shortest_dist_node(dist_so_far)
        # lock it down!
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                new_dist = final_dist[w] + G[w][x]
                if (x not in dist_so_far) or (new_dist < dist_so_far[x]):
                    dist_so_far[x] = new_dist
    return final_dist

