from utils import *
from theoric import *

import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

import random
import os

def convert_to_nx(graph):
    if graph.directed:
        return directed_graph_to_nxgraph(graph)
    else:
        return undirected_graph_to_nxgraph(graph)

def show_path(name, graph, path):
    show_graph_with_path(name, convert_to_nx(graph), path)

def show_graph(name, graph, colors=False):
    g = convert_to_nx(graph)
    if graph.directed:
        show_nxgraph(name, g, colors)
    else:
        show_nxgraph(name, g, colors)

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
    nx.draw(graph, pos=nx.spring_layout(graph), **options)

    if not os.path.exists("images"):
        os.mkdir("images")

    plt.savefig("images/" + name + ".png")
    plt.show()

def show_graph_with_path(name, graph, path):
    options = {
        "with_labels": True,
        "edgecolors": "black",
        "node_color": "white"
    }

    lbls = {}
    colors = [(0, 0, 0)] * len(graph.edges)
    for i in range(1, len(path)):
        lbls[path[i - 1], path[i]] = str(i)

        f = (i - 1) / (len(path) - 1)

        j = 0
        x, y = path[i - 1], path[i]
        for a, b in graph.edges:
            if graph.is_directed() and a == x and b == y:
                break
            elif (a == x and b == y) or (a == y and b == x):
                break
            j += 1
        colors[j] = (f, 0, 1 - f)
    print(graph.edges)
    print(lbls)

    options["edge_color"] = colors
    
    print("Plotting graph with path")
    nx.draw(graph, nx.spring_layout(graph), **options)

    if not os.path.exists("images"):
        os.mkdir("images")

    plt.savefig("images/" + name + ".png")
    plt.show()