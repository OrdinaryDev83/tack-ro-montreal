from practical.data import *
from practical.districts import *
import matplotlib

# MATPLOTLIB IS NOT THREAD SAFE

matplotlib.use("Agg")

snow_plows = 2200

dataCollect = []

def subprocess(district):
    data = getData(district)

    snow = process_undirected(district, data)
    dataCollect.append(process_directed(district, data, snow))

for dis in districts:
    subprocess(dis)

total = 0
for data in dataCollect:
    name, totalweight, cycleData = data
    total += totalweight

for data in dataCollect:
    name, totalweight, cycleData = data
    snow_plows_count = round((totalweight / total) * snow_plows)
    process_directed_data(name, *cycleData, snow_plows_count)

print("Finished")