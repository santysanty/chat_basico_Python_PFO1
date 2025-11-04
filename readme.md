📂 chat_basico_Python_PFO1
 ├── servidor.py          # Servidor concurrente que recibe y guarda mensajes
 ├── cliente.py           # Cliente que se conecta al servidor y envía mensajes
 ├── ver_mensajes.py      # Visualiza los registros almacenados en la base de datos
 ├── chat.db              # Base de datos SQLite generada automáticamente
 ├── README.md            # Documento descriptivo del proyecto
🚀 Funcionamiento
🧠 Servidor (servidor.py)
Inicializa la base de datos y crea la tabla mensajes si no existe.

Escucha en el puerto 5000 y acepta conexiones de varios clientes.

Cada cliente es manejado en un hilo independiente (thread).

Cada mensaje recibido se guarda con:

ID autoincremental

Contenido

Fecha y hora de envío

IP del cliente

Si el cliente envía "éxito", el servidor cierra su conexión.

💬 Cliente (cliente.py)
Se conecta al servidor en localhost:5000.

Permite enviar múltiples mensajes o salir con “éxito”.

Muestra la respuesta del servidor para cada mensaje.

📊 Visualización de Mensajes (ver_mensajes.py)
Permite listar los mensajes guardados en la base de datos chat.db:


ID: 1 | Mensaje: exito | Fecha: 2025-11-04 02:15:29 | IP: 127.0.0.1
ID: 2 | Mensaje: exito | Fecha: 2025-11-04 02:15:35 | IP: 127.0.0.1
ID: 3 | Mensaje: exito | Fecha: 2025-11-04 02:15:40 | IP: 127.0.0.1
ID: 4 | Mensaje: exito | Fecha: 2025-11-04 02:30:08 | IP: 127.0.0.1
ID: 5 | Mensaje: exito | Fecha: 2025-11-04 02:30:19 | IP: 127.0.0.1
ID: 6 | Mensaje: exito | Fecha: 2025-11-04 02:30:29 | IP: 127.0.0.1
🧪 Pruebas de Ejecución
🔹 Ejecución del Servidor

PS C:\Users\Usuario\Desktop\Redes\ProgramacionSobreRedes\PFO1> py servidor.py
Servidor escuchando en localhost:5000...
Nuevo cliente conectado: ('127.0.0.1', 56407)
[2025-11-04 02:30:08] 127.0.0.1 dijo: exito
Nuevo cliente conectado: ('127.0.0.1', 56408)
[2025-11-04 02:30:19] 127.0.0.1 dijo: exito
Nuevo cliente conectado: ('127.0.0.1', 56409)
[2025-11-04 02:30:29] 127.0.0.1 dijo: exito
🔹 Cliente 1 – juan

PS C:\Users\Usuario\Desktop\Redes\ProgramacionSobreRedes\PFO1> py cliente.py
Ingrese un nombre para este cliente: juan
juan conectado al servidor. Escribe 'éxito' para salir.

juan -> exito
Servidor -> Mensaje recibido (2025-11-04 02:30:08)
juan ->
🔹 Cliente 2 – mario

PS C:\Users\Usuario\Desktop\Redes\ProgramacionSobreRedes\PFO1> py cliente.py
Ingrese un nombre para este cliente: mario
mario conectado al servidor. Escribe 'éxito' para salir.

mario -> exito
Servidor -> Mensaje recibido (2025-11-04 02:30:19)
mario ->
🔹 Cliente 3 – lulu

PS C:\Users\Usuario\Desktop\Redes\ProgramacionSobreRedes\PFO1> py cliente.py
Ingrese un nombre para este cliente: lulu
lulu conectado al servidor. Escribe 'éxito' para salir.

lulu -> exito
Servidor -> Mensaje recibido (2025-11-04 02:30:29)
lulu ->
🔹 Visualización con ver_mensajes.py

PS C:\Users\Usuario\Desktop\Redes\ProgramacionSobreRedes\PFO1> py ver_mensajes.py

📋 Lista de mensajes guardados:

ID: 1 | Mensaje: exito | Fecha: 2025-11-04 02:15:29 | IP: 127.0.0.1
ID: 2 | Mensaje: exito | Fecha: 2025-11-04 02:15:35 | IP: 127.0.0.1
ID: 3 | Mensaje: exito | Fecha: 2025-11-04 02:15:40 | IP: 127.0.0.1
ID: 4 | Mensaje: exito | Fecha: 2025-11-04 02:30:08 | IP: 127.0.0.1
ID: 5 | Mensaje: exito | Fecha: 2025-11-04 02:30:19 | IP: 127.0.0.1
ID: 6 | Mensaje: exito | Fecha: 2025-11-04 02:30:29 | IP: 127.0.0.1
🧩 Concurrencia Implementada
El servidor utiliza threading.Thread para permitir que varios clientes se comuniquen simultáneamente.
Cada cliente se ejecuta en un hilo independiente y el acceso a la base de datos se sincroniza mediante threading.Lock(), evitando errores por escritura simultánea.

✅ Versión final funcional.  
⚙️ Servidor concurrente con base de datos integrada.  
💬 Clientes múltiples con identificación individual.
