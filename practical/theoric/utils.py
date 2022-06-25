from theoric.graph import *
import math

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

def find_bridges_undirected(adj_list):
    dfs_counter = 0
    n = len(adj_list) 
    dfs_ord = [math.inf] * n
    low_link = [math.inf] * n
    visited_vertices = [False] * n
    parent_vertex = [-1] * n
    total = []
    for i in range(n):
        if visited_vertices[i] == False:
            dfs(i, total, visited_vertices, parent_vertex, low_link, dfs_ord, dfs_counter, adj_list)
    return total

def dfs(u, total, visited_vertices, parent_vertex, low_link, dfs_ord, dfs_counter, adj_list):
    visited_vertices[u] = True
    dfs_ord[u] = dfs_counter
    low_link[u] = dfs_counter
    dfs_counter += 1
    for v in adj_list[u]:
        if visited_vertices[v] == False:
            parent_vertex[v] = u
            dfs(v, total, visited_vertices, parent_vertex, low_link, dfs_ord, dfs_counter, adj_list)
            low_link[u] = min(low_link[u], low_link[v])
            if low_link[v] > dfs_ord[u]:
                total.append((u, v))
        elif v!= parent_vertex[u]:
            low_link[u] = min(low_link[u], dfs_ord[v])