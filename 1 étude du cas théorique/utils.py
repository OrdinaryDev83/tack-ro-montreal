from graph import *

def edges_from_matrix(n, matrix):
        edges = []
        for i in range(n):
            for j in range(n):
                if matrix[i, j] != 0:
                    edges.append((i, j, matrix[i, j]))
        return edges

def directed_graph_from_cycle(n, cycle):
    edges = []
    for i in range(len(cycle) - 1):
        edges.append((cycle[i], cycle[i + 1], 1))
    return Graph(n, edges, True)