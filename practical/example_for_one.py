from data import *

data = getData("Anjou")

snow = process_undirected("Anjou", data)

#############################################################################################

process_directed("Anjou", data, snow)