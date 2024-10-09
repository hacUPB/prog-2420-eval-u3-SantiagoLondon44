# Sistema de Renta de Vehiculos

# Listas para almacenar datos de Vehiculos y clientes
Vehiculos = []
clientes = []

# Diccionario para almacenar las reservas: clave = cliente, valor = vehiculo
reservas = {}

# Función para agregar un vehiculo al inventario
def agregar_vehiculo():
    vehiculo = input("Ingrese el modelo del vehiculo: ")
    Vehiculos.append(vehiculo)
    print(f"vehiculo '{vehiculo}' agregado al inventario.\n")

# Función para agregar un cliente
def agregar_cliente():
    cliente = input("Ingrese el nombre del cliente: ")
    clientes.append(cliente)
    print(f"Cliente '{cliente}' agregado al sistema.\n")

# Función para realizar una reserva
def realizar_reserva():
    cliente = input("Ingrese el nombre del cliente que realiza la reserva: ")
    if cliente not in clientes:
        print("Cliente no encontrado. Por favor, regístrelo primero.\n")
        return

    vehiculo = input("Ingrese el modelo del vehiculo a reservar: ")
    if vehiculo not in Vehiculos:
        print("vehiculo no disponible en el inventario.\n")
        return

    reservas[cliente] = vehiculo
    Vehiculos.remove(vehiculo)
    print(f"Reserva realizada con éxito. {cliente} ha rentado el vehiculo '{vehiculo}'.\n")

# Función para mostrar el estado de los Vehiculos
def mostrar_estado_Vehiculos():
    print("Vehiculos disponibles para renta:")
    for vehiculo in Vehiculos:
        print(f"- {vehiculo}")
    
    print("\nVehiculos rentados:")
    for cliente, vehiculo in reservas.items():
        print(f"{cliente} ha rentado el vehiculo '{vehiculo}'")
    print("\n")

# Función principal del programa para interactuar con el usuario
def menu_principal():
    while True:
        print("Sistema de Renta de Vehiculos")
        print("1. Agregar vehiculo")
        print("2. Agregar cliente")
        print("3. Realizar reserva")
        print("4. Mostrar estado de Vehiculos")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_vehiculo()
        elif opcion == '2':
            agregar_cliente()
        elif opcion == '3':
            realizar_reserva()
        elif opcion == '4':
            mostrar_estado_Vehiculos()
        elif opcion == '5':
            print("Saliendo del sistema de renta de Vehiculos.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.\n")

# Ejecucion del software
if __name__ == "__main__":
    menu_principal()

