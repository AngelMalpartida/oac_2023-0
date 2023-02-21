import time
from multiprocessing import Pool

CUENTA = 50_000_000

num_proc=16

def cuenta(n:int)-> None:
    while n > 0:
        n -= 1

if __name__=="__main__":
    inicio = time.perf_counter()
    with Pool(processes=num_proc) as pool:
        pool.map(cuenta, [CUENTA//num_proc]*num_proc)
    fin = time.perf_counter()
    print(f"Tiempo de cuenta descendente multiproceso : {fin - inicio:0.2f} segundos")