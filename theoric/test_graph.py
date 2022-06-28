M = np.array([
    [0, 1, 2, 0],
    [0, 0, 0, 1],
    [2, 0, 0, 3],
    [0, 0, 0, 0]
    ])
dir = True
E_M = edges_from_matrix(4, M)
g = Graph(4, E_M, dir)
assert g.n == 4
assert len(g.edges) == 5
assert g.directed == dir

E = np.array([(0, 1, 1), (0, 2, 2), (1, 3, 1), (2, 0, 2), (2, 3, 3)])
dir = True
g = Graph(4, E, dir)
assert g.n == 4
assert len(g.edges) == 5
assert g.directed == dir