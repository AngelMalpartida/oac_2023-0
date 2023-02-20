from threading import Thread
import time

CUENTA = 50_000_000


def cuenta(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    inicio = time.perf_counter()
    t1 = Thread(target=cuenta, args=(CUENTA // 2,))
    t2 = Thread(target=cuenta, args=(CUENTA // 2,))
    t1.start()
    t2.start()
    #t1.join()
    #t2.join()  # Si se descomentan estas dos líneas, los tiempos de ejecucion se reducen
    
    fin = time.perf_counter()

    print(f"Tiempo de cuenta descendente multihilo: {fin - inicio:0.2f} segundos")
