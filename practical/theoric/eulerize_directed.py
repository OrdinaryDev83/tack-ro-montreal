import numpy as np
from theoric.utils import *

def shortest_distances_directed(n, edges, src):
    dist = [np.inf] * n
    dist[src] = 0
    oldDist = dist.copy()

    for i in range(n - 1):
        for (x, y, z) in edges:
            dist[y] = min(dist[y], dist[x] + z)
        if dist != oldDist:
            oldDist = dist.copy()
        else:
            break

    return dist

def find_closest_unbalanced(src, dists, balance):
    minDist, bestPartner = np.inf, src
    n = len(balance)
    for dst in range(src + 1, n):
        if balance[src] * balance[dst] < 0 and dists[dst] <= minDist:
            minDist, bestPartner = dists[dst], dst

    return bestPartner

def vertices_ratio(n, edges):
    # in // out ratio
    balance = [0 for i in range(n)]

    for e in edges:
        balance[e[0]] += 1
        balance[e[1]] -= 1

    return balance

def is_eulerian_directed(n, edges):
    balance = vertices_ratio(n, edges)
    return all(balance[i] == 0 for i in range(n))

def eulerize_directed(n, edges):
    # déjà eulerien
    if is_eulerian_directed(n, edges):
        return edges

    balance = vertices_ratio(n, edges)

    # ils doivent tous être balance

    for v in range(len(balance)):
        if balance[v] != 0:
            dists = shortest_distances_directed(n, edges, v)

        while balance[v] != 0:
            bestPartner = find_closest_unbalanced(v, dists, balance)

            # donator notation (out +, in -)
            if balance[v] > 0:
                while balance[bestPartner] < 0 and balance[v] > 0:
                    edges.append((bestPartner, v, dists[bestPartner]))
                    balance[v] -= 1
                    balance[bestPartner] += 1
            else:
                while balance[bestPartner] > 0 and balance[v] < 0:
                    edges.append((v, bestPartner, dists[bestPartner]))
                    balance[v] += 1
                    balance[bestPartner] -= 1

    return edges

def adj_list(n, edges):
        succ = [[] for a in range(n)]
        for (a, b, w) in edges:
            succ[a].append(b)
        return succ

# Hierholzer's implementation
def find_eulerian_cycle_directed(n, edges):
    adj = adj_list(n, edges)

    # needs to be connected and odd vertices 0 or 2
    ov = odd_vertices(n, edges)
    assert is_edge_connected(n, edges) \
        and (len(ov) == 0 or len(ov) == 2)
    if len(adj) == 0:
        return []

    nbEdges = [0] * n
    for i in range(len(adj)):
        nbEdges[i] = len(adj[i])

    circuit = []
    currentPath = [0]
    currentVertex = 0

    while currentPath:
        if nbEdges[currentVertex]:
            currentPath.append(currentVertex)
            nextVertex = adj[currentVertex][-1]
            nbEdges[currentVertex] -= 1
            adj[currentVertex].pop()
            currentVertex = nextVertex
        else:
            circuit.append(currentVertex)
            currentVertex = currentPath.pop()

    circuit.reverse()
    circuit.pop()
    return circuit
