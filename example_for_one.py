from practical.data import *
import matplotlib

# MATPLOTLIB IS NOT THREAD SAFE

matplotlib.use("Agg")

data = getData("Anjou")

snow = process_undirected("Anjou", data)

#############################################################################################

process_directed("Anjou", data, snow)