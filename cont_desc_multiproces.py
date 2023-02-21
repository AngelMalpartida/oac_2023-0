import time
import multiprocessing as mp
CUENTA = 50_000_000


def cuenta(n:int)-> None:
    while n > 0:
        n -= 1

if __name__=="__main__":
    inicio = time.perf_counter()
    p1 = mp.Process(target=cuenta, args=(CUENTA // 2,))
    p2 = mp.Process(target=cuenta, args=(CUENTA // 2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    fin = time.perf_counter()
    print(f"Tiempo de cuenta descendente multiproceso: {fin - inicio:0.2f} segundos")