import numpy as np
from utils import *

def odd_vertices(n, edges):
    deg = [0] * n
    for (a, b, w) in edges:
        deg[a] += 1
        deg[b] += 1
    return [a for a in range(n) if deg[a] % 2]

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

def find_eulerian_cycle(n, edges):
    assert is_eulerian_undirected(n, edges)
    if len(edges) == 0:
        return []
    cycle = [edges[0][0]] # start somewhere
    while True:
        rest = []
        for (a, b, w) in edges:
            if cycle[-1] == a:
                cycle.append(b)
            elif cycle[-1] == b:
                cycle.append(a)
            else:
                rest.append((a,b,w))
        if not rest:
            assert cycle[0] == cycle[-1]
            return cycle[0:-1]
        edges = rest
        if cycle[0] == cycle[-1]:
            # Rotate the cycle so that the last state
            # has some outgoing edge in EDGES.
            for (a, b, w) in edges:
                if a in cycle:
                    idx = cycle.index(a)
                    cycle = cycle[idx:-1] + cycle[0:idx+1]
                    break

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

def is_edge_connected(n, edges):
    if n == 0 or len(edges) == 0:
        return True
    # Convert to adjacency list
    succ = [[] for a in range(n)]
    for (a, b, w) in edges:
        succ[a].append(b)
        succ[b].append(a)
    # BFS over the graph, starting from one extremity of the first edge
    touched = [False] * n
    init = edges[0][0]
    touched[init] = True
    todo = [init]
    while todo:
        s = todo.pop()
        for d in succ[s]:
            if touched[d]:
                continue
            touched[d] = True
            todo.append(d)
    for a in range(n):
        if succ[a] and not touched[a]:
            return False
    return True

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