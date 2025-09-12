import socket

# Conectar al servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 5000))
print("Conectado al servidor. Escribe 'éxito' para salir.\n")

while True:
    mensaje = input("Escribe un mensaje: ")
    client_socket.send(mensaje.encode())

    if mensaje.lower() == "exito":
        print("Cerrando conexión...")
        break

    respuesta = client_socket.recv(1024)
    print(f"Servidor -> {respuesta.decode()}")

client_socket.close()
