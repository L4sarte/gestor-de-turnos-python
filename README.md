Gestor de Turnos (Turnero)
Un sistema de gestión de turnos desarrollado en Python. Este proyecto busca replicar la lógica de un sistema de reservas escalable, comenzando desde un MVP (Producto Mínimo Viable) en consola y evolucionando hacia una aplicación robusta con persistencia de datos.

📋 Características Actuales
Alta de turnos: Registro de cliente, fecha, hora y estado.

Listado de turnos: Visualización completa de las reservas actuales.

Cancelación: Eliminación de turnos mediante ID único.

Interfaz de Consola: Menú interactivo y navegación sencilla.

Validación de Entradas: Manejo de errores para evitar cierres inesperados en el menú principal.

🛠️ Tecnologías
Python 3.x

Lógica estructurada (en proceso de migración a modular/POO)

🚀 Hoja de Ruta (Roadmap)
El desarrollo del proyecto sigue una estrategia incremental:

[x] MVP Básico (CRUD en memoria).

[x] Robustez en el menú principal (Manejo de errores).

[x] Robustez en la entrada de datos (IDs y Fechas).

[x] Refactorización: Eliminar variables globales y dependencias.

[x] Persistencia de datos: Guardado y cargado mediante archivos JSON.

[ ] Manejo avanzado de fechas (Librería datetime).

[ ] Interfaz Gráfica (Futuro).

📝 Historial de Cambios (Changelog)

v0.3 (Persistencia y Estructura)
Persistencia de Datos: Implementación de sistema de guardado y carga automática mediante archivos JSON (turnos.json). Los datos ya no se pierden al cerrar el programa.

Modularización: Refactorización del código en dos módulos: main.py (controlador principal) y funciones.py (lógica de negocio), mejorando la escalabilidad.

Lógica Autónoma: Eliminación de variables globales para el contador de IDs; ahora el sistema calcula el siguiente ID automáticamente basado en los registros existentes.

Robustez: Implementación de manejo de errores (try-except) en todas las entradas numéricas críticas para evitar cierres inesperados.

v0.2
Se implementó un sistema de try-except en el menú principal y en la seccion "Cancelar turno" para evitar que el programa se cierre al ingresar texto en lugar de números.

Mejoras en la legibilidad del código.

v0.1
Lanzamiento inicial del MVP.

Funciones básicas: Agregar, Ver y Cancelar turnos.

Almacenamiento temporal en listas (RAM).

👤 Autor
L4sarte - Desarrollador Junior / Trainee