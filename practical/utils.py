import osmnx as ox
import networkx as nx
from theoric.graph import *

def random_adj_matrix(n, maxEdge):
    M = np.zeros((n, n))
    i = 0
    dict = {}
    while i < maxEdge:
        x = np.random.randint(0, n)
        y = np.random.randint(0, n)
        if x != y and (x, y) not in dict:
            M[x, y] = 1
            i += 1
            dict[(x, y)] = 1
    return M

def random_edges(n, maxEdge):
    M = random_adj_matrix(n, maxEdge)
    e = []
    for i in range(n):
        for j in range(n):
            if M[i, j] != 0:
                e.append((i, j, M[i, j]))
    return e

def directed_graph_to_nxgraph(g):
    G = nx.DiGraph()

    for i in range(g.n):
        G.add_node(i)
    
    for (a, b, w) in g.edges:
        G.add_edge(a, b, weight=w)
    return G

def directed_nxgraph_to_graph(G):
    g = Graph(G.number_of_edges(), G.edges(), True)
    return g

def undirected_graph_to_nxgraph(g):
    G = nx.Graph()

    for (a, b, w) in g.edges:
        G.add_edge(a, b, weight=w)
    return G

# à changer
def undirected_nxgraph_to_graph(G):
    graph = Graph(len(G), None, False)
    graph.edges = []
    
    nodes = {}
    index = 0
    for node in G.nodes:
        nodes[node] = index
        index += 1
    nodes

    length = nx.get_edge_attributes(G, "length")
    
    edges = []
    for edge in G.edges:
        node1 = nodes[edge[0]]
        node2 = nodes[edge[1]]
        weight = length[edge]
        edges.append((node1, node2, weight))
    
    graph.edges = edges
        
    return graph