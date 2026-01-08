import funciones
    
funciones.cargar_turnos()
while True:
    opcion = funciones.mostrar_menu()
    if opcion == 1:
        print("--- Agregar turno ---")
        funciones.agregar_turno()
    elif opcion == 2:
        funciones.ver_turnos()
    elif opcion == 3:
        funciones.cancelar_turno()
    elif opcion == 4:
        print("Gracias por usar mi sistema, hasta luego!")
        break
    else:
        print("Opcion no valida, ingrese una entre (1-4)")