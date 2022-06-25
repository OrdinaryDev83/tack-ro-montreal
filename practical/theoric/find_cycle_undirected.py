import numpy as np
from theoric.utils import *

# A Changer

def convertListToAdjaList(n, edges):
    L = [[] for _ in range(n)]
    for edge in edges:
        L[edge[0]].append(edge[1])
        L[edge[1]].append(edge[0])  # Non-Directed hypothesis
    return L

def find_eulerian_cycle_undirected(m, edges, startPoint):
    cycle = []
    E = len(edges)
    if E == 0:
        return cycle, 0

    totalWeight = 0 # the starting point is added at the end anyway
    X = startPoint
    cycle.append(X)
    index_to_insert = 1
    edges_used = [False] * E
    L = convertListToAdjaList(m, edges)

    while False in edges_used:
        current_v = X

        while True:
            current_v = visit_unused_edge(L, current_v, edges, edges_used)
            cycle.insert(index_to_insert, current_v)
            totalWeight += 1
            index_to_insert += 1
            if current_v == X:
                break

        # Checking if the current X still has unvisited edges
        unvisited_start = has_unvisited_edges(X, edges, edges_used)

        # Determining the new X
        if not unvisited_start and False in edges_used:
            for v in range(len(cycle)):
                if has_unvisited_edges(cycle[v], edges, edges_used):
                    X = cycle[v]
                    index_to_insert = v + 1
                    break
        # at this point we loop back with possibly a new starting vertice
        # until every edge is visited

    cycle.pop()
    return cycle, totalWeight


def visit_unused_edge(L, v, edges, edges_used):
    for i in range(len(L[v])):
        if find_list((v, L[v][i]), edges, edges_used) == -1:
            continue
        return L[v][i]
    return -1


def find_list(edge, L, edges_used):
    for i in range(len(L)):
        if not edges_used[i] and ((edge[0], edge[1]) == (L[i][0], L[i][1])
                                  or (edge[1], edge[0]) == (L[i][0], L[i][1])):
            edges_used[i] = True
            return i
    return -1


def has_unvisited_edges(node, edges, edges_used):
    for i in range(len(edges)):
        if edges_used[i]:
            continue
        if edges[i][0] == node or edges[i][1] == node:
            return True
    return False
