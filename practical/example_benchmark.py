from data import *
from districts import *
import random
from matplotlib import pyplot as plt
from time import time

def is_connected(n, edges):
    if n == 0:
        return True
    # Convert to adjacency list
    succ = [[] for a in range(n)]
    for (a,b,w) in edges:
        succ[a].append(b)
        succ[b].append(a)
    # DFS over the graph
    touched = [False] * n
    touched[0] = True
    todo = [0]
    while todo:
        s = todo.pop()
        for d in succ[s]:
            if not touched[d]:
                touched[d] = True
                todo.append(d)
    return sum(touched) == n      

def show_graph(G):    
    labels = {}
    for i in range(len(G.nodes)):
        labels[i] = str(i)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, labels=labels)
    plt.show()

def tryfor(n_nodes):
    n = n_nodes
    e = round(n * 3)
    E = []

    while not is_connected(n, E):
        E = random_edges(n, e)
    print(is_connected(n, E))

    G = Graph(n, E, False)
    print("Is Eulerian :", G.is_eulerian(), len(G.edges))
    G.eulerize()
    print("Is Eulerian :", G.is_eulerian(), len(G.edges))

    show_graph(undirected_graph_to_nxgraph(G))

    find_eulerian_cycle_undirected(G.n, G.edges, 0)

X = []
Y = []

k = 10
for i in range(0, 20):
    k = round(1.3 * k)
    print(k)
    X.append(k)
    t0 = time()
    tryfor(k)
    Y.append((time() - t0))
    print(i, time() - t0)

plt.plot(X, Y)
plt.xlabel("Nodes")
plt.ylabel("Time")
plt.show()