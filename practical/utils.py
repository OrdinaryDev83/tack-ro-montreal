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

def directed_nxgraph_to_graph(nxGraph):
    graph = Graph(len(nxGraph), None, False)
    graph.edges = []
    
    nodes = {}
    index = 0
    for node in nxGraph.nodes:
        nodes[node] = index
        index += 1
    nodes

    length = nx.get_edge_attributes(nxGraph, "length")
    
    edges = []
    for edge in nxGraph.edges:
        node1 = nodes[edge[0]]
        node2 = nodes[edge[1]]
        weight = length[edge]
        edges.append((node1, node2, weight))
    
    graph.edges = edges
        
    return graph, nodes

def undirected_graph_to_nxgraph(graph):
    nxGraph = nx.Graph()
    
    # On ajoute les noeuds
    for i in range(graph.n):
        nxGraph.add_node(i)

    # On ajoute les arêtes avec leur poids
    for edge in graph.edges:
        nxGraph.add_edge(edge[0], edge[1], weight=edge[2])
    
    return nxGraph

# à changer
def undirected_nxgraph_to_graph(nxGraph):
    graph = Graph(len(nxGraph.nodes), None, False)
    graph.edges = []
    
    nodes = {}
    index = 0
    for node in nxGraph.nodes:
        nodes[node] = index
        index += 1

    length = nx.get_edge_attributes(nxGraph, "length")
    
    edges = []
    for edge in nxGraph.edges:
        node1 = nodes[edge[0]]
        node2 = nodes[edge[1]]
        weight = length[edge]
        edges.append((node1, node2, weight))
    
    graph.edges = edges
        
    return graph, nodes

def remove_nxgraph_loops(graph):
    E = [edge for edge in graph.edges]
    for (a, b, w) in E:
        if a == b:
            graph.remove_edge(a, b)

def directed_graph_from_cycle(n, cycle):
    graph = Graph(n, None, True)
    edges = []
    size = len(cycle)

    for i in range(size - 1):
        edge = (cycle[i], cycle[i + 1], i / size)
        edges.append(edge)

    finalEdge = (cycle[-1], cycle[0], 1)
    edges.append(finalEdge)

    graph.edges = edges

    return graph

def cut_edges(G):
    depth = [-1] * G.order
    cutpoints = [0] * G.order
    cutedge = []
    x = 0
    depth[x] = 0
    nb_child = 0
    for adj in G.adjlists[x]:
        if depth[adj] == -1:
            depth[adj] = 1
            nb_child += 1
            higher_adj = __cut_edges(G,x,adj,depth,cutpoints,cutedge)
            if higher_adj > depth[x]:
                cutedge.append((x,adj))
    cutpoints[0] = nb_child-1
    return (cutpoints,cutedge)

def __cut_edges(G,x,y,depth,cutpoints,cutedge):
    higher_y = depth[y]
    for adj in G.adjlists[y]:
        if depth[adj] == -1:
            depth[adj] = depth[y] + 1
            higher_z = __cut_edges(G,y,adj,depth,cutpoints,cutedge)
            higher_y = min(higher_y,higher_z)
            if higher_z >= depth[y]:
                cutpoints[y] += 1
                if higher_z > depth[y]:
                    cutedge.append((y,adj))
        else:
            if adj != x:
                higher_y = min(higher_y,depth[adj])
    return higher_y