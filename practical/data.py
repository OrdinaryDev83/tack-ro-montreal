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
    plt.figure()
    path = "imgs/" + name + "/" + name + "_view.png"
    # fig, ax = ox.plot_graph(data, save=True, filepath=path, show=False, dpi=1000)

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

    fig = plt.figure()
    nx.draw(graph, **options, width=0.2)
    fig.set_facecolor("#FFFFFF")
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
def plot_cycle(name, subName, originalNxGraph, euleurizedG, G_cycle, G_nodes):
    options = {
    "node_size": 2,
    "arrowsize": 3,
    "min_source_margin": 1,
    }

    positionsx = nx.get_node_attributes(originalNxGraph, "x")
    positionsy = nx.get_node_attributes(originalNxGraph, "y")
    position = {}
    org_position = {}
    for pos in positionsx:
        a = G_nodes[pos]
        position[a] = (positionsx[pos], positionsy[pos])
        org_position[pos] = (positionsx[pos], positionsy[pos])

    labels = {}

    """for i in range(1, len(cycle)):
    a = cycle[i - 1]
    b = cycle[i]
    labels[(a, b)] = str(i)"""

    plt.figure()
    nx.draw(originalNxGraph, pos=org_position, **options, width=0.2)

    edge_color = []
    i = 0
    for edge in G_cycle.edges:
        edge_clr = i / (len(G_cycle.edges) - 1)
        edge_color.append((edge_clr, 0, 1 - edge_clr))
        i += 1
    options["edge_color"] = edge_color

    X = directed_graph_to_nxgraph(G_cycle)

    nx.draw(X, pos=position, **options, width=0.2)
    nx.draw_networkx_labels(euleurizedG, pos=position, labels=labels)
    plt.savefig("imgs/" + name + "/" + name + "_" + subName + ".png", dpi=1000)

def hours_to_HMS(h):
    hours = math.floor(h)
    minutes = math.floor((h * 60.0) % 60.0)
    secondes = math.floor((((h * 60.0) % 60.0) * 60.0) % 60.0)

    return str(hours) + ":" + str(minutes) + ":" + str(secondes)

def find_key(d, value):
    for (a, b, c) in d.keys():
        if a == value[0] and b == value[1]:
            return (a, b, c)
    for (a, b, c) in d.keys():
        if b == value[0] and a == value[1]:
            return (-1, -1, c)
    return None

# save the calculated data in a file
def save_data(name, cycle, snow):
    total_snow_volume = 0
    total_distance_km = 0

    # avg size of the roads
    avg_road_width = 5.0
    # avg fuel consumption per km in L for deneigeuses
    avg_fuel_consumption_per_km = 30.0
    # avg fuel cost in $
    avg_fuel_cost = 0.9
    # avg deneigeuse speed in km/h
    avg_speed = 5.0

    for i in range(1, len(cycle)):
        a = cycle[i - 1]
        b = cycle[i]
        key = (a, b)
        n_key = find_key(snow, key)
        weight = 0
        s = 0
        if n_key != None:
            weight = n_key[2]
            if n_key[0] != -1:
                s = snow[n_key]
        total_snow_volume += weight * (s / 100) * avg_road_width
        total_distance_km += (weight / 1000)

    total_snow_volume /= 100

    lines = [
        "distance : " + str(round(total_distance_km, 2)) + "km\n",
        "snow : " + str(round(total_snow_volume, 2)) + "m3\n",
        "fuel spent : " + str(round(total_distance_km * avg_fuel_consumption_per_km, 2)) + "L\n"
        "fuel cost : " + str(round(total_distance_km * avg_fuel_consumption_per_km * avg_fuel_cost, 2)) + "$\n"
        "time : " + hours_to_HMS(total_distance_km / avg_speed)
        ]
    with open("imgs/" + name + "/" + name + "_data.txt", 'w') as f:
        f.writelines(lines)

# plot and process the data in a directed way
def process_directed(name, data):
    if not(os.path.isdir("imgs")):
        os.mkdir("imgs")
    if not(os.path.isdir("imgs/" + name)):
        os.mkdir("imgs/" + name)
    print("Processing " + name + " (directed)")
    
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
    cycle_directed = find_eulerian_cycle_directed(G.n, G.edges, 0)

    # convert the node list to a directed graph (cycle graph)
    print("Finding a cycle")
    G_cycle_directed = directed_graph_from_cycle(G.n, cycle_directed)

    # convert it back to a nxgraph to plot it
    E = directed_graph_to_nxgraph(G)

    # plot the cycle graph
    plot_cycle(name, "directed_cycle", directedNxGraph, E, G_cycle_directed, G_nodes)
    save_data(name, cycle_directed, G.snow)

# plot and process the data in a undirected way
def process_undirected(name, data):
    if not(os.path.isdir("imgs")):
        os.mkdir("imgs")
    if not(os.path.isdir("imgs/" + name)):
        os.mkdir("imgs/" + name)
    print("Processing " + name + " (undirected)")

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

    weight = 0
    for edge in G.edges:
        weight += edge[2]
    print("Total street length", str(round(weight / 1000.0, 2)) + "km")

    print("Is the graph Eulerian:", G.is_eulerian(), "/", "Edges count:", len(G.edges))

    # find an eulerian cycle in a directed graph
    print("Finding a cycle")
    cycle_directed = find_eulerian_cycle_undirected(G.n, G.edges, 0)

    # convert the node list to a directed graph (cycle graph)
    G_cycle_directed = directed_graph_from_cycle(G.n, cycle_directed)

    # convert it back to a nxgraph to plot it
    E = directed_graph_to_nxgraph(G)

    # plot the cycle graph
    plot_cycle(name, "undirected_cycle", undirectedNxGraph, E, G_cycle_directed, G_nodes)