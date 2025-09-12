import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect("chat.db")
cursor = conn.cursor()

# Consulta de los mensajes
cursor.execute("SELECT * FROM mensajes")
mensajes = cursor.fetchall()

# Mostrar los resultados
print("\n📋 Lista de mensajes guardados:\n")
for fila in mensajes:
    print(f"ID: {fila[0]} | Mensaje: {fila[1]} | Fecha: {fila[2]} | IP: {fila[3]}")

conn.close()