import socket
import sqlite3
import datetime

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
    """Guarda un mensaje en la base de datos."""
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO mensajes (contenido, fecha_envio, ip_cliente) VALUES (?, ?, ?)",
                   (contenido, fecha, ip_cliente))
    conn.commit()
    conn.close()
    return fecha

def inicializar_socket():
    """Configura el socket del servidor."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 5000))
    server_socket.listen(5)
    print("Servidor escuchando en localhost:5000...")
    return server_socket

def manejar_cliente(client_socket, client_address):
    """Recibe mensajes del cliente y los guarda en la DB."""
    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        mensaje = data.decode().strip()
        if mensaje.lower() == "éxito":
            print(f"Cliente {client_address} finalizó la conexión.")
            break

        fecha = guardar_mensaje(mensaje, client_address[0])
        respuesta = f"Mensaje recibido: {fecha}"
        client_socket.send(respuesta.encode())
        print(f"[{fecha}] {client_address[0]} dijo: {mensaje}")

    client_socket.close()

# --------------------- MAIN ---------------------
if __name__ == "__main__":
    try:
        inicializar_db()
        server_socket = inicializar_socket()
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Conexión establecida con {client_address}")
            manejar_cliente(client_socket, client_address)
    except OSError as e:
        print(f"Error de socket: {e}")
    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")
