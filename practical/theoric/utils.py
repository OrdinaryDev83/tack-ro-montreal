from theoric.graph import *

def odd_vertices(n, edges):
    deg = [0] * n
    for (a, b, w) in edges:
        deg[a] += 1
        deg[b] += 1
    return [a for a in range(n) if deg[a] % 2]

def edges_from_matrix(n, matrix):
        edges = []
        for i in range(n):
            for j in range(n):
                if matrix[i, j] != 0:
                    edges.append((i, j, matrix[i, j]))
        return edges

# same for undirected and directed as it only makes sense
# for undirected graphs
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