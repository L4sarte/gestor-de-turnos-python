import funciones
    
# "Activar" el json para leer los turnos anteriormente guardados
funciones.cargar_turnos()
while True:
    # Para traer la variable opcion de la funcion
    opcion = funciones.mostrar_menu()
    if opcion == 1:
        print("--- Agregar turno ---")
        nombre, fecha, hora = funciones.solicitar_datos_turno()
        funciones.agregar_turno(nombre, fecha, hora)
    elif opcion == 2:
        funciones.ver_turnos()
    elif opcion == 3:
        id_borrar = funciones.solicitar_id() # 1. Pide el dato
        funciones.cancelar_turno(id_borrar)           # 2. Ejecuta la acción
    elif opcion == 4:
        id_actualizar = funciones.solicitar_id()
        funciones.marcar_turno_realizado(id_actualizar)
    elif opcion == 5:
        print("Gracias por usar mi sistema, hasta luego!")
        break
    else:
        print("Opcion no valida, ingrese una entre (1-5)")