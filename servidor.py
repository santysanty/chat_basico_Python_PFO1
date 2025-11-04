import socket
import sqlite3
import datetime
import threading

# Creamos un lock global para proteger el acceso a la base de datos
db_lock = threading.Lock()

# --------------------- FUNCIONES ---------------------

def inicializar_db():
    """Crea la base de datos y la tabla si no existen."""
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contenido TEXT NOT NULL,
            fecha_envio TEXT NOT NULL,
            ip_cliente TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def guardar_mensaje(contenido, ip_cliente):
    """Guarda un mensaje en la base de datos (con bloqueo de concurrencia)."""
    with db_lock:  # Solo un hilo puede escribir a la vez
        conn = sqlite3.connect("chat.db")
        cursor = conn.cursor()
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO mensajes (contenido, fecha_envio, ip_cliente) VALUES (?, ?, ?)",
                       (contenido, fecha, ip_cliente))
        conn.commit()
        conn.close()
        return fecha

def manejar_cliente(client_socket, client_address):
    """Recibe mensajes del cliente, los guarda y responde."""
    print(f"Nuevo cliente conectado: {client_address}")
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            mensaje = data.decode().strip()
            if mensaje.lower() == "éxito":
                print(f"Cliente {client_address} cerró la conexión.")
                break

            # Guarda mensaje de forma segura con Lock
            fecha = guardar_mensaje(mensaje, client_address[0])
            respuesta = f"Mensaje recibido ({fecha})"
            client_socket.send(respuesta.encode())
            print(f"[{fecha}] {client_address[0]} dijo: {mensaje}")

    except (ConnectionResetError, ConnectionAbortedError):
        print(f"Cliente {client_address} se desconectó abruptamente.")
    finally:
        client_socket.close()
        print(f"Conexión finalizada con {client_address}")

def inicializar_socket():
    """Configura el socket del servidor."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 5000))
    server_socket.listen(5)
    print("Servidor escuchando en localhost:5000...")
    return server_socket

# --------------------- MAIN ---------------------
if __name__ == "__main__":
    inicializar_db()
    server_socket = inicializar_socket()

    while True:
        client_socket, client_address = server_socket.accept()
        hilo_cliente = threading.Thread(target=manejar_cliente, args=(client_socket, client_address))
        hilo_cliente.start()
