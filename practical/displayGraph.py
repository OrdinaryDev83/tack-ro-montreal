from utils import *
from theoric import *

import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

import random
import os

def show_path(name, graph):
    show_graph(graph, True)

def show_graph(name, graph, colors=False):
    if graph.directed:
        show_nxgraph(name, directed_graph_to_nxgraph(graph), colors)
    else:
        show_nxgraph(name, undirected_graph_to_nxgraph(graph), colors)

def show_nxgraph(name, graph, colors=False):
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
    
    print("Plotting graph")
    nx.draw(graph, **options)

    if not os.path.exists("images"):
        os.mkdir("images")

    plt.savefig("images/" + name + ".png")
    plt.show()