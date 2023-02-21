import numpy as np
import time



M=5000
N=5000


def mult_vec_sincrono(X,Y):
    Z=0
    for j in range(len(Y)):
        Z+=X[i,j]*Y[j]
    return Z

if __name__=="__main__":
    
    mat_M=np.random.randint(100,size=(M,N))

    vector_N=np.random.randint(100,size=(M,))
    inicio = time.perf_counter()
    for i in range(M):
        Z=mult_vec_sincrono(mat_M,vector_N)
    fin = time.perf_counter()
    print(f"Tiempo de cuenta descendente multiproceso: {fin - inicio:0.2f} segundos")