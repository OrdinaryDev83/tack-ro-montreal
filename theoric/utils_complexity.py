from theoric.utils import *
from time import time

nodes_numbers_list = [10, 20, 50, 100, 200, 500, 1000]

dir_graph_list = []
undir_graph_list = []

for i in nodes_numbers_list:
    edges_directed, edges_undirected = random_connected_graph(i)
    graph_u = Graph(10, edges_undirected, False)
    graph_d = Graph(10, edges_directed, True)
    dir_graph_list.append(graph_d)
    undir_graph_list.append(graph_u)
    g_u = undirected_graph_to_nxgraph(graph_u)
    g_d = directed_graph_to_nxgraph(graph_d)
    if (i < 100):
        show_graph(g_u)
        show_graph(g_d)

    
eulerizing_time_list_directed = []
eulerizing_time_list_undirected = []

for i in range(len(undir_graph_list)):
    t0 = time()
    print(undir_graph_list[i].edges)
    undir_graph_list[i].eulerize()
    t1 = time()
    print ("undirected eulerizing time: " + str(int(t1 - t0)) + " seconds" + " (nodes_number: " + str(nodes_numbers_list[i]) + ")")
    eulerizing_time_list_undirected.append(t1 - t0)

for i in range(len(dir_graph_list)):
    t0 = time()
    dir_graph_list[i].eulerize()
    t1 = time()
    print ("directed eulerizing time: " + str(int(t1 - t0)) + " seconds" + " (nodes_number: " + str(nodes_numbers_list[i]) + ")")
    eulerizing_time_list_directed.append(t1 - t0)
