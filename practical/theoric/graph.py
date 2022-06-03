import numpy as np
from theoric.eulerize_directed import *
from theoric.eulerize_undirected import *

class Graph:
    def __init__(self, n, edges=None, directed=False):
        self.n = n
        self.directed = directed
        self.edges = edges

    def adj_list(self):
        succ = [[] for a in range(self.n)]
        for (a, b, w) in self.edges:
            succ[a].append(b)
            if not(self.directed):
                succ[b].append(a)
        return succ

    def adj_matrix(self):
        M = np.full((self.n, self.n), 0, dtype=object)
        for (i, j, w) in self.edges:
            M[i, j] = w
            if not(self.directed):
                M[j, i] = w
        return M

    def eulerize(self):
        if self.directed:
            self.edges = eulerize_directed(self.n, self.edges)
        else:
            self.edges = eulerize_undirected(self.n, self.edges)
    
    def is_eulerian(self):
        if self.directed:
            return is_eulerian_directed(self.n, self.edges)
        else:
            return is_eulerian_undirected(self.n, self.edges)

    def find_euler_path(self):
        if self.directed:
            return find_eulerian_cycle_directed(self.n, self.edges)
        else:
            return find_eulerian_cycle_undirected(self.n, self.edges)
    
def directed_graph_from_cycle(n, cycle):
    edges = []
    for i in range(len(cycle) - 1):
        edges.append((cycle[i], cycle[i + 1], 1))
    return Graph(n, edges, True)