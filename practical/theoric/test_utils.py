from imports import *

M = np.array([
    [0, 1, 2, 0],
    [0, 0, 0, 1],
    [2, 0, 0, 3],
    [0, 0, 0, 0]
    ])
E_M = edges_from_matrix(4, M)
assert E_M == [(0, 1, 1), (0, 2, 2), (1, 3, 1), (2, 0, 2), (2, 3, 3)]

assert is_eulerian_undirected(5, [(0, 1, 1),(0,2, 1),(0,3, 1),(0,4, 1),(1,2, 1),(3,1, 1),(4,1, 1),(3,2, 1),(2,4, 1),(4,3, 1)])
#  Königsberg 7 bridges
assert is_eulerian_undirected(4, [(0,2, 1),(2,3, 1),(3,0, 1),(2,0, 1),(2,1, 1),(3,1, 1),(1,2, 1)]) == False
assert is_eulerian_undirected(4, [])
assert is_eulerian_undirected(5, [(1,2, 1),(1,3, 1),(1,4, 1),(1,0, 1),(2,3, 1),(4,2, 1),(0,2, 1),(4,3, 1),(3,0, 1),(0,4, 1)])

g0=(4, [(0,1, 1),(1,2, 1),(2,3, 1),(3,0, 1)])
assert is_eulerian_cycle(*g0, find_eulerian_cycle_directed(*g0,0))

g1=(4, [(2,0, 1),(2,1, 1),(3,1, 1),(1,2, 1),(0,2, 1),(2,3, 1),(3,0, 1),(3,2, 1),(0,1, 1),(0,0, 1)])
assert is_eulerian_cycle(*g1, find_eulerian_cycle_undirected(*g1,0))
	
g0=(4, [(1,2, 1),(2,3, 1),(3,0, 1),(0,1, 1)])
assert is_eulerian_cycle(*g0, find_eulerian_cycle_directed(*g0,0))

g = (5,[(0,4, 1),(4,1, 1),(1,2, 1),(2,3, 1),(3,2, 1),(2,1, 1),(1,4, 1),(4,0, 1)])
assert find_eulerian_cycle_directed(*g,0) == [0, 4, 1, 2, 3, 2, 1, 4]