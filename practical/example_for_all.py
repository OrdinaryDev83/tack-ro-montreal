from data import *
from districts import *
import threading

def process(district):
    data = getData(district)

    process_directed(district, data)
    process_undirected(district, data)

threads = []
for district in districts:
    threads.append(threading.Thread(target=process, args=(district,)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Finished")