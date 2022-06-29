from practical.data import *
import matplotlib

# MATPLOTLIB IS NOT THREAD SAFE

matplotlib.use("Agg")
snow_plows = 2200
snow_plow_per_district = round(np.floor(snow_plows / 19))

data = getData("Anjou")

snow = process_undirected("Anjou", data)

#############################################################################################

process_directed("Anjou", data, snow, snow_plow_per_district)