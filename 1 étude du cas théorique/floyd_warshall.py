import numpy as np


def init_mat(n, edges, op_plus, e_plus, op_times, e_times):
    # Set up the matrix
    M = np.full((n, n), e_plus, dtype=np.object_)
    # Matrix for the successors of each vertex
    Succ = np.full((n, n), None, dtype=np.object_)

    # Diag elems
    for i in range(n):
        M[i, i] = e_times
        Succ[i, i] = i

    # Add the edges
    for (a,b,w) in edges:
        assert M[a, b] == e_plus
        M[a, b] = w
        Succ[a, b] = b

    return M, Succ

def add(a, b):
    return a + b

def min(a, b):
    if a > b:
        return b
    else:
        return a

def max(a, b):
    if a > b:
        return a
    else:
        return b

def mul(a, b):
    return a * b

# les opérateurs doivent avoir un sens
def floyd_warshall(n, edges, op_plus = min, e_plus = np.inf, op_times = add, e_times = 0):
    # Generalised Floyd-Warshall algorithm
    # with successor computation

    M_last, Succ = init_mat(n, edges, op_plus, e_plus, op_times, e_times)

    # Floyd-Warshall triple loop
    for k in range(n):
        M_current = np.full((n, n), None, dtype=np.object_)
        for i in range(n):
            for j in range(n):
                M_current[i,j] = op_plus(M_last[i][j], op_times(M_last[i,k], M_last[k,j]))
                # Check if changed
                if M_current[i,j] != M_last[i,j]:
                    Succ[i,j] = Succ[i,k]
        M_last = M_current

    return M_current, Succ

def path_i2j(Succ, i, j):
    assert len(Succ) == len(Succ[0])
    assert (0 <= i < len(Succ)) and (0 <= j < len(Succ))

    if Succ[i][j] is None:
        return []

    path = [i]
    while i != j:
        i = Succ[i][j]
        path.append(i)
    return path

def safest_path(n, edges, i, j):
    M,S = floyd_warshall(n,edges, max, 0., mul, 1.)
    return path_i2j(S, i, j)