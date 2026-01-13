# Gestor de Turnos (Turnero)

Un sistema de gestión de turnos desarrollado en Python. Este proyecto busca replicar la lógica de un sistema de reservas escalable, comenzando desde un MVP en consola y evolucionando hacia una aplicación robusta con persistencia de datos y arquitectura profesional.

## 📋 Características Actuales
* **Alta de turnos (Create):** Registro de cliente, fecha y hora con validaciones robustas (no permite fechas pasadas ni formatos inválidos).
* **Listado de turnos (Read):** Visualización completa de las reservas. Mensajes inteligentes cuando no hay datos.
* **Actualización de Estado (Update):** Posibilidad de marcar turnos como "Completado" reutilizando la lógica de búsqueda.
* **Cancelación (Delete):** Eliminación de turnos mediante ID único.
* **Persistencia de Datos:** Guardado automático en `JSON` para mantener la información entre sesiones.
* **Arquitectura MVC:** Separación clara entre la Interfaz (inputs/menú) y la Lógica de Negocio.

## 🛠️ Tecnologías
* **Lenguaje:** Python 3.x
* **Manejo de Datos:** JSON (Persistencia), Datetime (Validación temporal).
* **Arquitectura:** Modular (Separación de responsabilidades: Interfaz vs Lógica).
* **Control de Versiones:** Git & GitHub.

## 🚀 Hoja de Ruta (Roadmap)
El desarrollo del proyecto sigue una estrategia incremental. Actualmente se ha alcanzado el hito de la **v1.0**.

- [x] MVP Básico (CRUD en memoria).
- [x] Robustez en el menú principal (Manejo de errores).
- [x] Persistencia de datos (JSON).
- [x] Refactorización: Arquitectura MVC (Separación Mozo/Cocinero).
- [x] Manejo avanzado de fechas (Librería `datetime`).
- [x] Funcionalidad completa CRUD (Create, Read, Update, Delete).
- [ ] Filtros de búsqueda (por fecha o cliente).
- [ ] Interfaz Gráfica (Futuro).

## 📝 Historial de Cambios (Changelog)

### v1.0 (Official Release - CRUD Completo)
* **Funcionalidad Completa:** Se agregó la opción de "Cambiar estado del turno" (de Pendiente a Completado), cerrando el ciclo CRUD.
* **Manejo de Fechas:** Implementación de la librería `datetime`. Ahora el sistema valida que las fechas sean reales y futuras.
* **Arquitectura MVC Finalizada:** Se completó la separación de responsabilidades. Las funciones lógicas (`agregar`, `cancelar`, `modificar`) ya no contienen `inputs` ni interacciones directas con el usuario, recibiendo todo por parámetros.
* **Mejoras de UX:** Mensajes más claros, feedback cuando las listas están vacías y validación de formatos de hora (HH:MM).

### v0.3 (Persistencia y Estructura)
* **Persistencia de Datos:** Implementación de sistema de guardado y carga automática mediante archivos JSON (`turnos.json`).
* **Modularización:** Refactorización del código en dos módulos: `main.py` y `funciones.py`.
* **Lógica Autónoma:** Generación automática de IDs basada en los registros existentes.

### v0.2
* Implementación de `try-except` generalizados para evitar cierres por errores de tipo de dato (str vs int).

### v0.1
* Lanzamiento inicial del MVP.
* Funciones básicas: Agregar, Ver y Cancelar.
* Almacenamiento temporal en RAM.

---
👤 **Autor**
**L4sarte** - Desarrollador de Software