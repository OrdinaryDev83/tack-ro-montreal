import numpy as np

class Graph:
    def __init__(self, n, edges=None, directed=False):
        self.n = n
        self.directed = directed
        self.edges = edges