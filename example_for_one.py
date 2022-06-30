from practical.data import *
import matplotlib

# MATPLOTLIB IS NOT THREAD SAFE

matplotlib.use("Agg")

data = getData("Anjou")

snow = process_undirected("Anjou", data)

#############################################################################################

name, totalweight, cycleData = process_directed("Anjou", data, snow)
snow_plows_count = 5
process_directed_data(name, *cycleData, snow_plows_count)