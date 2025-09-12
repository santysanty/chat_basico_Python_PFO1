# Propuesta Formativa Obligatoria

## TP: Chat Básico Cliente-Servidor con Sockets y Base de Datos

### Objetivo
Configurar un **servidor de sockets en Python** que reciba mensajes de clientes, los guarde en una base de datos SQLite y envíe confirmaciones.  
Se busca aplicar buenas prácticas de **modularización**, **manejo de errores** y documentación del código.

---

### Servidor
- Escucha en `localhost:5000`.
- Funciones principales:
  - Inicializar el socket.
  - Aceptar conexiones y recibir mensajes.
  - Guardar mensajes en la base de datos (`id`, `contenido`, `fecha_envio`, `ip_cliente`).
  - Manejar errores (puerto ocupado, DB no accesible).
  - Responder al cliente con:  
    ```
    Mensaje recibido: <timestamp>
    ```

---

### Cliente
- Se conecta al servidor en `localhost:5000`.
- Permite enviar múltiples mensajes hasta que el usuario escriba `éxito`.
- Muestra la respuesta del servidor para cada mensaje.

---

### Base de Datos
- Usar **SQLite** (`sqlite3`).
- Tabla `mensajes` con los campos:
  - `id` (INTEGER, PRIMARY KEY AUTOINCREMENT)
  - `contenido` (TEXT)
  - `fecha_envio` (TEXT)
  - `ip_cliente` (TEXT)

---

### Recomendaciones
- Comentar cada sección clave del código, por ejemplo:
  ```python
  # Configuración del socket TCP/IP
