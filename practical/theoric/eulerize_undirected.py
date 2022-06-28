import numpy as np
from utils import *

# bellman-ford for undirected graph
def shortest_relative_distances(n, edges, src):
    dist = [np.inf] * n
    dist[src] = 0
    oldDist = dist.copy()

    for i in range(n - 1):
        for (x, y, z) in edges:
            dist[y] = min(dist[y], dist[x] + z)
            dist[x] = min(dist[x], dist[y] + z)
        if dist != oldDist:
            oldDist = dist.copy()
        else:
            break

    return dist

def closest_from_source(S, dists, listOdd):
    minDist, bestNeighbour = np.inf, S
    for D in listOdd:
        if D == S:
            continue
        if dists[D] < minDist:
            minDist, bestNeighbour = dists[D], D

    return bestNeighbour

def is_eulerian_undirected(n, edges):
    return is_edge_connected(n, edges) and not odd_vertices(n, edges)

def nedge(a, b):
    return (a, b) if a < b else (b, a)

def is_eulerian_cycle(n, edges, cycle):
    if len(edges) != len(cycle):
        return False
    if len(edges) == 0:
        return True
    eset = {}
    for (a, b, w) in edges:
        s = nedge(a, b)
        if s in eset:
            eset[s] += 1
        else:
            eset[s] = 1
    for (a, b) in zip(cycle, cycle[1:]+cycle[0:1]):
        s = nedge(a, b)
        if s in eset and eset[s] > 0:
            eset[s] -= 1
        else:
            return False
    for val in eset.values():
        if val != 0:
            return False
    return True

def eulerize_undirected(n, edges):
    oddVertices = odd_vertices(n, edges)

    # déjà eulerien
    if len(oddVertices) == 0:
        return edges

    # Match pairs of odd-degrees Vertices until there are no more left
    while len(oddVertices) != 0:
        oddV = oddVertices[0]
        shortestDist = shortest_relative_distances(n, edges, oddV)
        next = closest_from_source(oddV, shortestDist, oddVertices)
        edges.append((oddV, next, shortestDist[next]))

        oddVertices.remove(oddV)
        oddVertices.remove(next)

    return edges


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
    return cycle


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
