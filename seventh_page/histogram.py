import multiprocessing as mp
import numpy as np
from matplotlib import pyplot as plt
import time

a = np.random.randint(0, 10, size=[2000, 2000])

def countHistogram(data):
    result = {}
    for i in data:
        result[i] = result.get(i, 0) + 1
    return result


def compareThreads():
    pool = mp.Pool(mp.cpu_count())
    print(mp.cpu_count())
    data = a.tolist()
    t = time.time()
    result = [pool.apply_async(countHistogram, args=(row,1)) for row in data]
    print("Time multicore: "+str(time.time() - t))
    pool.close()

    t = time.time()
    result = []
    for row in data:
        result.append(countHistogram(row))
    print("Time single: " + str(time.time() - t))

if __name__ == '__main__':
    compareThreads()

#12
#Time multicore: 0.09110021591186523
#Time single: 1.3453929424285889