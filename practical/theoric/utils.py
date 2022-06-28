from graph import *
import math
from matplotlib import pyplot as plt
import networkx as nx

def show_graph(G):    
    labels = {}
    for i in range(len(G.nodes)):
        labels[i] = str(i)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, labels=labels)
    plt.show()
    
    
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

def odd_vertices(n, edges):
    deg = [0] * n
    for (a, b, w) in edges:
        deg[a] += 1
        deg[b] += 1
    return [a for a in range(n) if deg[a] % 2]

def edges_from_matrix(n, matrix):
        edges = []
        for i in range(n):
            for j in range(n):
                if matrix[i, j] != 0:
                    edges.append((i, j, matrix[i, j]))
        return edges

# same for undirected and directed as it only makes sense
# for undirected graphs
def is_edge_connected(n, edges):
    if n == 0 or len(edges) == 0:
        return True
    # Convert to adjacency list
    succ = [[] for a in range(n)]
    for (a, b, w) in edges:
        succ[a].append(b)
        succ[b].append(a)
    # BFS over the graph, starting from one extremity of the first edge
    touched = [False] * n
    init = edges[0][0]
    touched[init] = True
    todo = [init]
    while todo:
        s = todo.pop()
        for d in succ[s]:
            if touched[d]:
                continue
            touched[d] = True
            todo.append(d)
    for a in range(n):
        if succ[a] and not touched[a]:
            return False
    return True

def find_bridges_undirected(adj_list):
    dfs_counter = 0
    n = len(adj_list) 
    dfs_ord = [math.inf] * n
    low_link = [math.inf] * n
    visited_vertices = [False] * n
    parent_vertex = [-1] * n
    total = []
    for i in range(n):
        if visited_vertices[i] == False:
            dfs(i, total, visited_vertices, parent_vertex, low_link, dfs_ord, dfs_counter, adj_list)
    return total

def dfs(u, total, visited_vertices, parent_vertex, low_link, dfs_ord, dfs_counter, adj_list):
    visited_vertices[u] = True
    dfs_ord[u] = dfs_counter
    low_link[u] = dfs_counter
    dfs_counter += 1
    for v in adj_list[u]:
        if visited_vertices[v] == False:
            parent_vertex[v] = u
            dfs(v, total, visited_vertices, parent_vertex, low_link, dfs_ord, dfs_counter, adj_list)
            low_link[u] = min(low_link[u], low_link[v])
            if low_link[v] > dfs_ord[u]:
                total.append((u, v))
        elif v!= parent_vertex[u]:
            low_link[u] = min(low_link[u], dfs_ord[v])