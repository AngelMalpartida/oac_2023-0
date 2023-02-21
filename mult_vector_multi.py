import time
import numpy as np
from itertools import repeat
from multiprocessing import Pool, cpu_count

M=5000
N=5000

def mult_vec_sincrono(X,Y):
    suma=0
    for j in range(len(Y)):
        suma+=X[j]*Y[j]
    return suma

if __name__=="__main__":
    resultados=list()
    mat_M=np.random.randint(100,size=(M,N))
    vector_N=np.random.randint(100,size=(M,))

    inicio = time.perf_counter()
    with Pool(processes=cpu_count()) as pool:
        a=1