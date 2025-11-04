import socket
import threading

def cliente_chat(nombre_cliente):
    """Función principal del cliente."""
    try:
        # Crear el socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 5000))
        print(f"{nombre_cliente} conectado al servidor. Escribe 'éxito' para salir.\n")

        while True:
            mensaje = input(f"{nombre_cliente} -> ")

            # Enviar mensaje
            client_socket.send(mensaje.encode())

            # Si el usuario escribe 'éxito', se cierra la conexión
            if mensaje.lower() == "éxito":
                print(f"{nombre_cliente} cerró la conexión.")
                break

            # Esperar respuesta del servidor
            respuesta = client_socket.recv(1024)
            if not respuesta:
                print("El servidor cerró la conexión.")
                break

            print(f"Servidor -> {respuesta.decode()}")

    except ConnectionRefusedError:
        print("No se pudo conectar con el servidor. Asegúrate de que esté ejecutándose.")
    except KeyboardInterrupt:
        print("\nConexión interrumpida manualmente.")
    finally:
        client_socket.close()
        print(f"Conexión finalizada para {nombre_cliente}.\n")

# --------------------- MAIN ---------------------
if __name__ == "__main__":
    # Identificación del cliente (automática o manual)
    nombre = input("Ingrese un nombre para este cliente: ").strip()
    if not nombre:
        nombre = f"Cliente-{threading.get_ident()}"  # Asigna un ID si no se escribe nombre

    cliente_chat(nombre)
