import json

lista_turnos = [

]

def guardar_turnos():
    with open('turnos.json', 'w', encoding='utf-8') as archivo:
        json.dump(lista_turnos, archivo, indent=4)

def cargar_turnos():
    global lista_turnos
    try:
        with open('turnos.json', 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            lista_turnos = datos
    except:
        lista_turnos = []

def mostrar_menu():
    print("\n--- Menu Gestor de tareas by L4sarte ---")
    print("1. Agregar turno \n2. Ver turnos \n3. Cancelar un turno \n4. Salir")
    while True:
        try:
            opcion = int(input("Seleccione una opcion: "))
            break
        except:
            print("Debes ingresar una opcion valida del menu (1-4)")
    return opcion

def agregar_turno():
    if len(lista_turnos) == 0:
        identificador = 1
    else:
        ultimo_id = lista_turnos[-1]
        identificador =  ultimo_id['id'] + 1
    cliente = input("Ingrese el nombre de quien reserva el turno: ")
    fecha = input("Ingrese fecha del turno (dd/mm/aaaa): ")
    hora = input("Ingrese la hora del turno (hh:mm): ")
    estado = "pendiente"
    nuevo_turno = {'id': identificador, 'cliente': cliente, 'fecha': fecha, 'hora': hora, 'estado': estado}
    lista_turnos.append(nuevo_turno)
    print("Turno agregado correctamente!")
    guardar_turnos()

def ver_turnos():
    print("\n--- Turnos actuales ---")
    for turno in lista_turnos:
        print(f"\tID: {turno['id']} \nCliente: {turno['cliente']} \nFecha: {turno['fecha']} \nHora: {turno['hora']} \nEstado: {turno['estado']}")
        print("------------------------------")

def cancelar_turno():
    print("\n--- Eliminar turno ---")
    while True:
        try:
            id_eliminar = int(input("Ingrese el ID del turno que desea eliminar: "))
            break
        except:
            print("Debe ingresar un ID valido (numerico entero)")
    turno_encontrado = None
    for turno in lista_turnos:
        if turno['id'] == id_eliminar:
            turno_encontrado = turno
            break
    if turno_encontrado:
        lista_turnos.remove(turno_encontrado)
        print("Turno cancelado correctamente")
        guardar_turnos()
    else:
        print("El ID ingresado no se encuentra")