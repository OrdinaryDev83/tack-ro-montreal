from theoric.utils import *
from time import time
import threading


res_list = []

def execute():
    nodes_great_list = []
    undir_graph_great_list = []
    dir_graph_great_list = []
    undir_euler_time_great_list = []
    dir_euler_time_great_list = []
    undir_cycle_great_list = []
    dir_cycle_great_list = []
    undir_cycle_time_great_list = []
    dir_cycle_time_great_list = []

    great_list = []

    great_list.append([10])
    great_list.append([20])
    great_list.append([50])
    #great_list.append([100])
    #great_list.append([200])
    #great_list.append([300])
    #great_list.append([400])
    #great_list.append([500])
    #great_list.append([600])
    #great_list.append([700])
    #great_list.append([800])
    #great_list.append([900])
    #great_list.append([1000])
    #great_list.append([2000])
    #great_list.append([3000])
    #great_list.append([4000])
    #great_list.append([5000])
    #great_list.append([6000])
    #great_list.append([7000])
    #great_list.append([8000])
    #great_list.append([9000])


    for nodes_numbers_list in great_list:
        dir_graph_list = []
        undir_graph_list = []

        nodes_great_list.append(nodes_numbers_list[0])

        for i in nodes_numbers_list:
            edges_directed, edges_undirected = random_connected_graph(i)
            graph_u = Graph(i, edges_undirected, False)
            #print("undir edges: ", graph_u.edges)
            graph_d = Graph(i, edges_directed, True)
            #print("dir edges: ", graph_d.edges)
            dir_graph_list.append(graph_d)
            undir_graph_list.append(graph_u)
            undir_graph_great_list.append(graph_u)
            dir_graph_great_list.append(graph_d)
            g_u = undirected_graph_to_nxgraph(graph_u)
            g_d = directed_graph_to_nxgraph(graph_d)
            if (i < 100):
                show_graph(g_u)
                show_graph(g_d)

            
        eulerizing_time_list_directed = []
        eulerizing_time_list_undirected = []


        for i in range(len(undir_graph_list)):
            t0 = time()
            undir_graph_list[i].eulerize()
            t1 = time()
            #print ("undirected eulerizing time: " + str(int((t1 - t0) * 1000) / 1000) + " seconds" + " (nodes_number: " + str(nodes_numbers_list[i]) + ")")
            #print ("Successfully ? " + str(undir_graph_list[i].is_eulerian()))
            eulerizing_time_list_undirected.append(t1 - t0)
            undir_euler_time_great_list.append(t1 - t0)
            undir_graph_great_list.append(undir_graph_list[i])
            #print("undirected graph: ", undir_graph_list[i].edges)

        for i in range(len(dir_graph_list)):
            t0 = time()
            dir_graph_list[i].eulerize()
            t1 = time()
            #print ("directed eulerizing time: " + str(int((t1 - t0) * 1000) / 1000) + " seconds" + " (nodes_number: " + str(nodes_numbers_list[i]) + ")")
            #print ("Successfully ? " + str(dir_graph_list[i].is_eulerian()))
            eulerizing_time_list_directed.append(t1 - t0)
            dir_euler_time_great_list.append(t1 - t0)
            dir_graph_great_list.append(dir_graph_list[i])
            #print("directed graph: ", dir_graph_list[i].edges)


        eulerian_cycle_time_list_directed = []
        eulerian_cycle_time_list_undirected = []
        eulerian_cycle_list_undirected = []
        eulerian_cycle_list_directed = []


        for i in range(len(undir_graph_list)):
            t0 = time()
            eulerian_cycle_list_undirected.append(find_eulerian_cycle_undirected(undir_graph_list[i].n, undir_graph_list[i].edges, 0))
            t1 = time()
            #print ("undirected eulerian cycle time: " + str(int((t1 - t0) * 1000) / 1000) + " seconds" + " (nodes_number: " + str(nodes_numbers_list[i]) + ")")
            #print ("Succesfully ? ", (len(eulerian_cycle_list_undirected[i]) - len(undir_graph_list[i].edges)) == 0)
            eulerian_cycle_time_list_undirected.append(t1 - t0)
            undir_cycle_time_great_list.append(t1 - t0)
            undir_cycle_great_list.append(eulerian_cycle_list_undirected[i])
            #print("undirected cycle: ", eulerian_cycle_list_undirected[i])

        for i in range(len(dir_graph_list)):
            t0 = time()
            eulerian_cycle_list_directed.append(find_eulerian_cycle_directed(dir_graph_list[i].n, dir_graph_list[i].edges, 0))
            t1 = time()
            #print ("directed eulerian cycle time: " + str(int((t1 - t0) * 1000) / 1000) + " seconds" + " (nodes_number: " + str(nodes_numbers_list[i]) + ")")
            #print ("Succesfully ? ", (len(eulerian_cycle_list_directed[i]) - len(dir_graph_list[i].edges)) == 0)
            eulerian_cycle_time_list_directed.append(t1 - t0)
            dir_cycle_time_great_list.append(t1 - t0)
            dir_cycle_great_list.append(eulerian_cycle_list_directed[i])
            #print("directed cycle: ", eulerian_cycle_list_directed[i])

        #print (nodes_numbers_list)
        #print (eulerizing_time_list_undirected)
        #print (eulerizing_time_list_directed)
        #print (eulerian_cycle_time_list_undirected)
        #print (eulerian_cycle_time_list_directed)
        #print ("\n")
        #print ("\n")

        #il faut plot/show les time_great_list en fonction de nodes_great_list

    #print(nodes_great_list)
    #print(undir_euler_time_great_list)
    #print(dir_euler_time_great_list)
    #print(undir_cycle_time_great_list)
    #print(dir_cycle_time_great_list)
    res_list.append([nodes_great_list, undir_euler_time_great_list, dir_euler_time_great_list, undir_cycle_time_great_list, dir_cycle_time_great_list])
    #print(res_list)


thread_list = []
for i in range(1):
    t = threading.Thread(target=execute)
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()


res_array = np.array(res_list)

print('\n')
print('\n')
print('\n')
print('results:')

print(res_array)

# mean on dimension 0 in res_array :
mean_res_array = np.mean(res_array, axis=0)

print ('mean results:')
print (mean_res_array)



print("done")
'''
plt.plot(nodes_great_list, eulerizing_time_list_undirected, 'b-', label='undirected')
plt.plot(nodes_great_list, eulerizing_time_list_directed, 'r-', label='directed')
plt.legend(loc='upper left')
plt.xlabel('nodes number')
plt.ylabel('eulerizing time')
plt.title('eulerizing time')
plt.show()

plt.plot(nodes_great_list, eulerian_cycle_time_list_undirected, 'b-', label='undirected')
plt.plot(nodes_great_list, eulerian_cycle_time_list_directed, 'r-', label='directed')
plt.legend(loc='upper left')
plt.xlabel('nodes number')
plt.ylabel('eulerian cycle time')
plt.title('eulerian cycle time')
plt.show()
'''