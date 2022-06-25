from turtle import pos
from utils import *
import matplotlib.pyplot as plt
import osmnx.distance as distance
from theoric import *
import os.path

# comparer random temps + n + point de départ + calculer complexite des algo + chercher des temps 
# notebook, push cele, refaire la partie théorique, faire plein de tests 

# get the data from the district (arrondissement)
def getData(district):
    data = ox.graph_from_place(district + ", Montréal, Canada", network_type="drive")
    data = distance.add_edge_lengths(data)
    return data

# show the data (not a graph)
def plot_data(name, data):
    plt.clf()
    path = "imgs/" + name + "/" + name + "_view.png"
    fig, ax = ox.plot_graph(data, save=True, filepath=path, show=False, dpi=1000)

# extract the directed nxgraph from the data
def extract_directed_graph(data):
    directedNxGraph = ox.utils_graph.get_digraph(data)
    return directedNxGraph

# extract the undirected nxgraph from the data
def extract_undirected_graph(data):
    undirectedNxGraph = ox.utils_graph.get_undirected(data)
    return undirectedNxGraph

# get the position dictionary from the graph and store them to plot them afterwards
def get_position(graph):
    positionsx = nx.get_node_attributes(graph, "x")
    positionsy = nx.get_node_attributes(graph, "y")
    position = {}
    for pos in positionsx:
        position[pos] = (positionsx[pos], positionsy[pos])
    return position

# plot a nxgraph
def plot_graph(name, subname, graph, position):
    options = {
    "node_size": 2,
    "arrowsize": 3,
    "min_source_margin": 1,
    "pos": position
    }

    nx.draw(graph, **options, width=0.2)
    plt.savefig("imgs/" + name + "/" + name + "_" + subname + ".png", dpi=1000)

# plot a nxgraph containing snow heights
def plot_snow(name, subname, G, graph, position):
    options = {
    "node_size": 2,
    "arrowsize": 3,
    "min_source_margin": 1,
    "pos": position
    }

    edge_color = []
    i = 0
    for edge in G.edges:
        snow = G.snow[edge]
        edge_clr = snow / 15
        if edge_clr > 1.0:
            edge_clr = 1.0
        edge_color.append((edge_clr, edge_clr, edge_clr))
        i += 1

    fig = plt.figure()
    nx.draw(graph, edge_color=edge_color, width=1, **options)
    fig.set_facecolor("#00000F")
    plt.savefig("imgs/" + name + "/" + name + "_" + subname + "_snow.png", dpi=1000)

# plot a cycle graph (directed graph with edges contained in the original graph, directed or not)
def plot_cycle(name, subName, originalNxGraph, G_cycle, E, G_nodes):
    options = {
    "node_size": 2,
    "arrowsize": 3,
    "min_source_margin": 1,
    }

    positionsx = nx.get_node_attributes(originalNxGraph, "x")
    positionsy = nx.get_node_attributes(originalNxGraph, "y")
    position = {}
    for pos in positionsx:
        a = G_nodes[pos]
        position[a] = (positionsx[pos], positionsy[pos])

    labels = {}

    """for i in range(1, len(cycle)):
    a = cycle[i - 1]
    b = cycle[i]
    labels[(a, b)] = str(i)"""

    nx.draw(E, pos=position, **options, width=0.2)

    edge_color = []
    i = 0
    for edge in G_cycle.edges:
        edge_clr = i / (len(G_cycle.edges) - 1)
        edge_color.append((edge_clr, 0, 1 - edge_clr))
        i += 1
    options["edge_color"] = edge_color

    X = directed_graph_to_nxgraph(G_cycle)

    nx.draw(X, pos=position, **options, width=0.2)
    nx.draw_networkx_labels(E, pos=position, labels=labels)
    plt.savefig("imgs/" + name + "/" + name + "_" + subName + ".png", dpi=1000)

# save the calculated data in a file
def save_data(name, weights, snow):
    total_snow_height = 0
    total_distance = 0
    avg_road_width = 5.0
    for key in weights:
        s = 0
        if key in snow:
            s = snow[key]
        elif ((key[1], key[0]) in snow):
            s = snow[(key[0], key[1])]
        total_snow_height += weights[key] * (s / 100) * avg_road_width
        total_distance += weights[key]

    total_snow_height /= 100

    lines = ["distance : " + str(round(total_distance / 100, 2)) + "km\n", "snow : " + str(round(total_snow_height, 2)) + "m3"]
    with open("imgs/" + name + "/" + name + "_data.txt", 'w') as f:
        f.writelines(lines)

# plot and process the data in a directed way
def process_directed(name):
    if not(os.path.isdir("imgs")):
        os.mkdir("imgs")
    if not(os.path.isdir("imgs/" + name)):
        os.mkdir("imgs/" + name)
    print("Processing " + name + " (directed)")
    data = getData(name)
    plot_data(name, data)

    # convert it to a nxgraph
    directedNxGraph = extract_directed_graph(data)

    # get the points' positions
    position = get_position(directedNxGraph)

    # plot the nx graph
    plot_graph(name, "raw_directed", directedNxGraph, position)

    # convert it to our graph class, keeping the old node IDs
    G, G_nodes = directed_nxgraph_to_graph(directedNxGraph)

    # snow height system

    print("Adding snow")
    G.add_random_snow() # according to a gaussian curve distribution of the snow height
    plot_snow(name, "directed", G, directedNxGraph, position)
    print("Removing unsnowy non bridges roads")
    G.remove_unsnowy() # remove unsnowy and not "bridges" roads

    # end snow
    print("Is the graph Eulerian:", G.is_eulerian(), "/", "Edges count:", len(G.edges))
    # eulerize the graph
    G.eulerize()


    print("Is the graph Eulerian:", G.is_eulerian(), "/", "Edges count:", len(G.edges))

    # find an eulerian cycle in a directed graph
    cycle_directed, weight_directed = find_eulerian_cycle_directed(G.n, G.edges, 0)

    # convert the node list to a directed graph (cycle graph)
    print("Finding a cycle")
    G_cycle_directed = directed_graph_from_cycle(G.n, cycle_directed)

    # convert it back to a nxgraph to plot it
    E = directed_graph_to_nxgraph(G)

    # plot the cycle graph
    plot_cycle(name, "directed_cycle", directedNxGraph, G_cycle_directed, E, G_nodes)
    save_data(name, weight_directed, G.snow)

# plot and process the data in a undirected way
def process_undirected(name):
    if not(os.path.isdir("imgs")):
        os.mkdir("imgs")
    if not(os.path.isdir("imgs/" + name)):
        os.mkdir("imgs/" + name)
    print("Processing " + name + " (undirected)")
    data = getData(name)
    plot_data(name, data)

    # convert it to a nxgraph
    undirectedNxGraph = extract_undirected_graph(data)

    # get the points' positions
    position = get_position(undirectedNxGraph)

    # plot the nx graph
    plot_graph(name, "raw_undirected", undirectedNxGraph, position)

    # convert it to our graph class, keeping the old node IDs
    G, G_nodes = undirected_nxgraph_to_graph(undirectedNxGraph)

    # snow height system

    print("Adding snow")
    G.add_random_snow() # according to a gaussian curve distribution of the snow height
    plot_snow(name, "undirected", G, undirectedNxGraph, position)
    print("Removing unsnowy non bridges roads")
    G.remove_unsnowy() # remove unsnowy and not "bridges" roads

    # end snow
    print("Is the graph Eulerian:", G.is_eulerian(), "/", "Edges count:", len(G.edges))
    # eulerize the graph
    G.eulerize()


    print("Is the graph Eulerian:", G.is_eulerian(), "/", "Edges count:", len(G.edges))

    # find an eulerian cycle in a directed graph
    print("Finding a cycle")
    cycle_directed = find_eulerian_cycle_undirected(G.n, G.edges, 0)

    # convert the node list to a directed graph (cycle graph)
    G_cycle_directed = directed_graph_from_cycle(G.n, cycle_directed)

    # convert it back to a nxgraph to plot it
    E = undirected_graph_to_nxgraph(G)

    # plot the cycle graph
    plot_cycle(name, "undirected_cycle", undirectedNxGraph, G_cycle_directed, E, G_nodes)