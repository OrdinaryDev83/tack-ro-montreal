import numpy as np
from theoric.eulerize_directed import *
from theoric.eulerize_undirected import *

class Graph:
    def __init__(self, n, edges=None, directed=False):
        self.n = n
        self.directed = directed
        self.edges = edges
        self.snow = {}

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
            M[i, j] = (w, self.snow[(i, j)])
            if not(self.directed):
                M[j, i] = (w, self.snow[(i, j)])
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

    def add_random_snow(self):
        for edge in self.edges:
            s = np.random.normal((2.5 + 15.0) / 2.0, 3.189) # 95% de chance d'avoir de la neige
            if s > 50:
                s = 50
            elif s < 0:
                s = 0
            self.snow[edge] = s

    def remove_unsnowy(self):
        i = 0
        if self.directed == False:
            bridges = find_bridges_undirected(self.adj_list())
            if bridges == None:
                return
            for b in bridges:
                if b == None:
                    continue
                b1, b2 = b
                if ((b1, b2) in self.snow and self.snow[(b1, b2)] < 2.5):
                    continue
                elif ((b2, b1) in self.snow and self.snow[(b2, b1)] < 2.5):
                    continue

                w = 0
                for (a, b, w) in self.edges:
                    if (a == b1 and a == b2) or (a == b2 and a == b1):
                        self.edges.remove((a, b, w))
                        i += 1
        print("Removed " + str(i))
    
def directed_graph_from_cycle(n, cycle):
    edges = []
    for i in range(len(cycle) - 1):
        edges.append((cycle[i], cycle[i + 1], 1))
    return Graph(n, edges, True)