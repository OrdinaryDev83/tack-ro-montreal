from utils import *
from theoric import *

import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

def show_path(graph):
    show_graph(graph, True)

def show_graph(graph, colors=False):
    if graph.directed:
        show_nxgraph(directed_graph_to_nxgraph(graph), colors)
    else:
        show_nxgraph(undirected_graph_to_nxgraph(graph), colors)

def show_nxgraph(graph, colors=False):
    options = {
        "with_labels": True,
        "edgecolors": "black",
        "node_color": "white"
    }
    
    if colors:
        clrs = []
        n = len(graph.edges)
        for i in range(n):
            f = i / n
            clrs.append((f, 0, 1 - f))

        options["edge_color"] = clrs
    
    nx.draw(graph, **options)
    plt.show()