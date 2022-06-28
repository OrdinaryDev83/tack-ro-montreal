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

def odd_vertices(n, edges):
    deg = [0] * n
    for (a, b, w) in edges:
        deg[a] += 1
        deg[b] += 1
    return [a for a in range(n) if deg[a] % 2]

def adj_list(n, edges):
        succ = [[] for a in range(n)]
        for (a, b, w) in edges:
            succ[a].append(b)
        return succ

# Hierholzer's implementation
def find_eulerian_cycle_directed(n, edges, startPoint):
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
    currentPath = [startPoint]
    currentVertex = startPoint

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

