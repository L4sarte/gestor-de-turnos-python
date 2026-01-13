import funciones
    
# "Activar" el json para leer los turnos anteriormente guardados
funciones.cargar_turnos()
while True:
    # Para traer la variable opcion de la funcion
    opcion = funciones.mostrar_menu()
    if opcion == 1:
        nombre, fecha, hora = funciones.solicitar_datos_turno()
        funciones.agregar_turno(nombre, fecha, hora)
        print("--- Agregar turno ---")
    elif opcion == 2:
        funciones.ver_turnos()
    elif opcion == 3:
        funciones.cancelar_turno()
    elif opcion == 4:
        print("Gracias por usar mi sistema, hasta luego!")
        break
    else:
        print("Opcion no valida, ingrese una entre (1-4)")