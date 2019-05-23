import socket

def main():
    s = socket.socket()
    s.bind(("localhost", 8000))
    print("Servidor iniciado. Esperando clientes...")
    s.listen()
    while True:
        cliente, addr = s.accept()
        print("Cliente conectado desde:", addr)
        while True:
            recibido = cliente.recv(1024)
            if str(recibido, "utf-8") == "salir":
                break
            else:
                print("Mensaje recibido por parte del cliente:", str(recibido, "utf-8"))
                cliente.send(recibido)
        print("Servicio finalizado - SERVIDOR")
        cliente.close()


if __name__ == '__main__': main()