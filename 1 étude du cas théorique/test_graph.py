from imports import *

M = np.array([
    [0, 1, 2, 0],
    [0, 0, 0, 1],
    [2, 0, 0, 3],
    [0, 0, 0, 0]
    ])
g = Graph(4, M, True, True)
D, P = floyd_warshall(g)
print(g.adj)
print(D)
print(P)

## tests : 

################ liste d'adjacences
#assert g.adjlists == 

################ directed ou non



################ costs ou non





################# matrice des couts





##################