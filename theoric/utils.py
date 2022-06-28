from theoric.graph import *
import math
from matplotlib import pyplot as plt
import networkx as nx

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

def random_adj_matrix(nodes_number, edges_number):
    M_directed = np.zeros((nodes_number, nodes_number))
    M_undirected = np.zeros((nodes_number, nodes_number))
    i = 0

    intersections = [0] * nodes_number

    for x in range(1, nodes_number):
        y = np.random.randint(0, x)
        while intersections[y] >= 6:
            y = np.random.randint(0, x)
        intersections[y] += 1
        intersections[x] += 1
        M_undirected[y, x] = 1
        M_directed[x, y] = 1
        if (np.random.random() < 0.6):
            M_directed[y, x] = 1
        i += 1

    while i < edges_number:
        x = np.random.randint(0, nodes_number)
        y = np.random.randint(0, nodes_number)
        if x != y and (M_undirected[x, y] == 0 or M_undirected[y, x] == 0) and intersections[x] < 6 and intersections[y] < 6:
            if (x < y):
                M_undirected[y, x] = 1
            else:
                M_undirected[x, y] = 1
            M_directed[x, y] = 1
            if (np.random.random() < 0.6):
                M_directed[y, x] = 1
            i += 1
    return M_directed, M_undirected

def random_edges(nodes_number, edges_number):
    M_directed, M_undirected = random_adj_matrix(nodes_number, edges_number)
    e_directed = []
    e_undirected = []
    for i in range(nodes_number):
        for j in range(nodes_number):
            if M_directed[i, j] != 0:
                e_directed.append((i, j, M_directed[i, j]))
            if M_undirected[i, j] != 0:
                e_undirected.append((i, j, M_undirected[i, j]))
    return e_directed, e_undirected

def random_connected_graph(nodes_number):
    edges_number = int((np.random.random() * 0.3 + 1.40)*nodes_number)
    try_counter = 1
    graph_directed, graph_undirected = random_edges(nodes_number, edges_number)
    while not is_connected(nodes_number, graph_undirected):
        graph_directed, graph_undirected = random_edges(nodes_number, edges_number)
        try_counter += 1
        print("Try #" + str(try_counter))
    print("Try counter: " + str(try_counter) + " (nodes_number: " + str(nodes_number) + ", edges_number: " + str(edges_number) + ")")
    return graph_directed, graph_undirected

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

def edges_from_matrix(n, matrix):
        edges = []
        for i in range(n):
            for j in range(n):
                if matrix[i, j] != 0:
                    edges.append((i, j, matrix[i, j]))
        return edges

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