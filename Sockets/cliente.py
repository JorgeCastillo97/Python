import socket

def main():
    c = socket.socket()
    c.connect(("localhost", 8000))
    while True:
        mensaje = input("Envia un mensaje por el socket: ")
        c.send(bytearray(mensaje, "utf8"))
        recibido = c.recv(1024)
        if mensaje == "salir":
            break
    print("Servicio finalizado - CLIENTE.")
    c.close()

if __name__ == '__main__': main()