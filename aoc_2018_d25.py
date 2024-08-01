import time

with open('inputd25.txt') as f:
    ls = f.read().strip().split('\n')

points = []
for l in ls:
    p = list(map(int, l.split(',')))
    points.append(p)

def get_dist(p1, p2):
    '''Given two four dimensional points, return the distance between them'''
    return(abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + \
           abs(p1[2]-p2[2]) + abs(p1[3]-p2[3]))

def distances(points):
    pd = dict()
    for p in points:
        cur_distances = []
        for p2 in points:
            cur_distances.append(get_dist(p, p2))
        pd[tuple(p)] = cur_distances
    return(pd)

T0 = time.perf_counter()
pd_dict = distances(points)
T1 = time.perf_counter()
print(f"It took {T1-T0} seconds to complete with only Python")


import numpy as np
ls = ','.join(ls)
points = np.array(list(map(int, ls.split(',')))).reshape(-1, 4)

def distances(points):
    # Need a list with a new axis to get the broadcasting to work correctly
    return(np.sum(np.abs(points[np.newaxis,:,:] - 
                         points[:,np.newaxis,:]), axis=-1))

T0 = time.perf_counter()
pds = distances(points)
T1 = time.perf_counter()
print(f"It took {T1-T0} seconds to complete with NumPy")
