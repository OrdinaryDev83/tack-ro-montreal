from data import *
from districts import *

for district in districts:
    process_directed(district)
    process_undirected(district)