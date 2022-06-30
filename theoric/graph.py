import numpy as np
from theoric.eulerize_directed import *
from theoric.eulerize_undirected import *
from theoric.utils import *


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
        edges_count = len(self.edges)
        if self.directed:
            self.edges = eulerize_directed(self.n, self.edges)
        else:
            self.edges = eulerize_undirected(self.n, self.edges)
        print("Eulerized " + str(edges_count) + " edges to " + str(len(self.edges)))
    
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

    # osmnx already adds the weights so it's useless here
    # but if we happened not have osmnx it's good
    def add_snow_and_weights(self, edges, snow):
        s = {}
        for (a, b, w) in snow.keys():
            p = snow[(a, b, w)]

            key = find_alternate_key(edges, (a, b))
            if key != None:
                s[key] = p
                s[(a, b, w)] = p
            else:
                s[(a, b, w)] = p
        self.snow = s

    def remove_unsnowy(self):
        i = 0
        if self.directed == False:
            return
            bridges = find_bridges_undirected(self.adj_list())
            if bridges == None:
                return
            for (a, b, w) in self.snow.keys():
                if ((a, b, w) in self.snow and 15 >= self.snow[(a, b, w)] >= 2.5):
                    continue

                if (a, b) not in bridges and (b, a) not in bridges:
                    self.edges.remove((a, b, w))
                    i += 1
            print("Removed " + str(i))
    
def directed_graph_from_cycle(n, cycle):
    edges = []
    for i in range(len(cycle) - 1):
        edges.append((cycle[i], cycle[i + 1], 1))
    return Graph(n, edges, True)

def find_alternate_key(d, value):
    for (a, b, c) in d:
        if a == value[1] and b == value[0]:
            return (a, b, c)
    return None