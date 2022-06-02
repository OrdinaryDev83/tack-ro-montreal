import numpy as np

class Graph:
    def __init__(self, n, edges=None, directed=False):
        self.n = n
        self.directed = directed
        self.edges = edges

    def adj_matrix(self):
        M = np.full((self.n, self.n), 0, dtype=object)
        for (i, j, w) in self.edges:
            M[i, j] = w
            if not(self.directed):
                M[j, i] = w
        return M