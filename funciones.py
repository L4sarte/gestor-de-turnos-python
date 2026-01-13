import json, datetime
from datetime import datetime

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
    # Validacion de formato input
    while True:
        try:
            opcion = int(input("Seleccione una opcion: "))
            break
        except:
            print("Debes ingresar una opcion valida del menu (1-4)")
    return opcion

def solicitar_datos_turno():
    
    cliente = input("Ingrese el nombre de quien reserva el turno: ")
    # Validacion de formato
    while True: 
        try:
            fecha = input("Ingrese fecha del turno (DD/MM/AAAA): ")
            fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
            if fecha_obj < datetime.now():
                print("No puede ser una fecha pasada")
            else:
                break
        except:
            print("El formato de la fecha debe ser el correcto (DD/MM/AAAA) y no puede ser una fecha pasada")
    # Validacion de formato
    while True:
        try: 
            hora = input("Ingrese la hora del turno (HH:MM): ")
            hora_obj = datetime.strptime(hora, "%H:%M")
            break
        except:
            print("El formato de la hora debe ser (HH:MM)")
    return cliente, fecha, hora

def solicitar_id_eliminar():
    while True:
        try:
            id_eliminar = int(input("Ingrese el ID del turno que desea eliminar: "))
            return id_eliminar # Devuelve el dato limpio
        except:
            print("Debe ingresar un ID valido (numerico entero)")

def agregar_turno(cliente, fecha, hora):
    # generacion de ID
    if len(lista_turnos) == 0:
        identificador = 1
    else:
        ultimo_id = lista_turnos[-1]
        identificador =  ultimo_id['id'] + 1
    estado = "Pendiente"
    nuevo_turno = {'id': identificador, 'cliente': cliente, 'fecha': fecha, 'hora': hora, 'estado': estado}
    lista_turnos.append(nuevo_turno)
    print("Turno agregado correctamente!")
    guardar_turnos()

def ver_turnos():
    print("\n--- Turnos actuales ---")
    # Recorre turno por turno y va mostrandolo
    for turno in lista_turnos:
        print(f"\tID: {turno['id']} \nCliente: {turno['cliente']} \nFecha: {turno['fecha']} \nHora: {turno['hora']} \nEstado: {turno['estado']}")
        print("------------------------------")

def cancelar_turno(id_eliminar): # <--- Ahora recibe el ID desde afuera
    print("\n--- Eliminar turno ---")
    
    turno_encontrado = None
    # Logica para buscar el turno
    for turno in lista_turnos:
        if turno['id'] == id_eliminar:
            turno_encontrado = turno
            break
            
    # Eliminacion de turno o retorno de no encontrado
    if turno_encontrado:
        lista_turnos.remove(turno_encontrado)
        print("Turno cancelado correctamente")
        guardar_turnos()
    else:
        print("El ID ingresado no se encuentra")