from practical.data import *
from practical.districts import *
import matplotlib

# MATPLOTLIB IS NOT THREAD SAFE

matplotlib.use("Agg")

def subprocess(district):
    data = getData(district)

    snow = process_undirected(district, data)
    process_directed(district, data, snow)

for dis in districts:
    subprocess(dis)

print("Finished")