import socket
import time
import random

SOCK_BUFFER = 4


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("192.168.0.105", 5000)

    print(f"Conectando a {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)
    client_id = random.randint(0, 1000)
    for i in range(5):
        msg = f"Hola mundo {i} desde el cliente {client_id}"
        msg = msg.encode("utf-8")
        inicio_tx = time.perf_counter()
        sock.sendall(msg)
        fin_tx = time.perf_counter()
        print(f"Tiempo de transmisión: {fin_tx - inicio_tx} segundos")

        amnt_recvd = 0
        amnt_expected = len(msg)
        total_data = b""
        
        inicio_rx = time.perf_counter()
        while amnt_recvd < amnt_expected:
            data = sock.recv(SOCK_BUFFER)
            total_data += data
            amnt_recvd += len(data)
            # print(f"Recibido parcial: {data}")
        fin_rx = time.perf_counter()

        print(f"Tiempo de recepción: {fin_rx - inicio_rx} segundos")
        
        print(f"Recibido: {total_data}")
        time.sleep(1)
    
    sock.sendall("quit".encode("utf-8"))

    sock.close()