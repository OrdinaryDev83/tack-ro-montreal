n = 5
edges = [(0,1,1), (1,0,3), (2,3,1), (1,4,4), (4,3,-1), (3,4,2)]

def same(a, b):
    return (a[0] == b[0]).all() and (a[1] == b[1]).all()

assert same(floyd_warshall(n, edges),
(np.array([[ 0.,  1., np.inf,  4.,  5.],
       [ 3.,  0., np.inf,  3.,  4.],
       [np.inf, np.inf,  0.,  1.,  3.],
       [np.inf, np.inf, np.inf,  0.,  2.],
       [np.inf, np.inf, np.inf, -1.,  0.]]),
       np.array([[ 0.,  1., None,  1.,  1.],
       [ 0.,  1., None,  4.,  4.],
       [None, None,  2.,  3.,  3.],
       [None, None, None,  3.,  4.],
       [None, None, None,  3.,  4.]])))

n = 5
edges = [(0,1,1), (1,0,3), (3,2,1), (1,4,4), (4,3,-1), (3,4,2)]
assert same(floyd_warshall(n, edges), (np.array([[0, 1, 5, 4, 5],
       [3, 0, 4, 3, 4],
       [np.inf, np.inf, 0, np.inf, np.inf],
       [np.inf, np.inf, 1, 0, 2],
       [np.inf, np.inf, 0, -1, 0]], dtype=object), np.array([[0, 1, 1, 1, 1],
       [0, 1, 4, 4, 4],
       [None, None, 2, None, None],
       [None, None, 2, 3, 4],
       [None, None, 3, 3, 4]], dtype=object)))

n = 5
edges = [(0,1,7), (1,0,3), (3,2,1), (1,4,4), (4,3,3), (3,4,2), (0,3,1)]
assert same(floyd_warshall(n, edges), (np.array([[0, 7, 2, 1, 3],
       [3, 0, 5, 4, 4],
       [np.inf, np.inf, 0, np.inf, np.inf],
       [np.inf, np.inf, 1, 0, 2],
       [np.inf, np.inf, 4, 3, 0]], dtype=object), np.array([[0, 1, 3, 3, 3],
       [0, 1, 0, 0, 4],
       [None, None, 2, None, None],
       [None, None, 2, 3, 4],
       [None, None, 3, 3, 4]], dtype=object)))
n = 5
edges = [(0,1,1), (1,0,3), (2,3,1), (1,4,4), (4,3,-1), (3,4,2)]
assert same(floyd_warshall(n, edges), (np.array([[0, 1, np.inf, 4, 5],
       [3, 0, np.inf, 3, 4],
       [np.inf, np.inf, 0, 1, 3],
       [np.inf, np.inf, np.inf, 0, 2],
       [np.inf, np.inf, np.inf, -1, 0]], dtype=object), np.array([[0, 1, None, 1, 1],
       [0, 1, None, 4, 4],
       [None, None, 2, 3, 3],
       [None, None, None, 3, 4],
       [None, None, None, 3, 4]], dtype=object)))

g = (3, [(0,1,0.8), (1,2,0.5), (0,2,0.3)])
assert safest_path(*g, 0, 2) == [0, 1, 2]
assert safest_path(*g, 1, 2) == [1, 2]
assert safest_path(*g, 1, 1) == [1]
assert safest_path(*g, 2, 0) == []