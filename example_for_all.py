from practical.data import *
from practical.districts import *
import matplotlib

# MATPLOTLIB IS NOT THREAD SAFE

matplotlib.use("Agg")

snow_plows = 2200
snow_plow_per_district = round(np.floor(snow_plows / len(districts)))
print("We dispose of", snow_plow_per_district, "plows per district")

def subprocess(district):
    data = getData(district)

    snow = process_undirected(district, data)
    process_directed(district, data, snow, snow_plow_per_district)

for dis in districts:
    subprocess(dis)

print("Finished")