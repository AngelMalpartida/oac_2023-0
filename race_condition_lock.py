import concurrent.futures
from threading import Lock
import time
class FakeDatabase:

    def __init__(self):
        self.value = 0
        self.lock = Lock()

    def update(self,name):
        print(f"Thread {name}: Buscando actualizacion")
        print(f"Thread {name}: apunto de iniciar el candado")
        self.lock.acquire()#se crea el locker para que no se pueda acceder
        #por otros hilos mientras se esta ejecutando
        print(f"Thread {name}: tiene el candado")
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        print(f"Thread {name}: liberando el candado")
        self.lock.release()
        print(f"Thread {name}: candado liberado")
        print(f"Thread {name}: actualizacion completa")

if __name__=="__main__":
    workers=5

    db=FakeDatabase()
    print(f"Valor inicial de la base de datos: {db.value}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(workers):
            executor.submit(db.update,(index))
    print(f"Valor final: {db.value}")