[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PehQeuqy)
# Unidad 3
---
## Documentación del proyecto
Nombre: Santiago Londoño Salazar 
ID:  000540651
---
# STAR CAR REN-A-CAR

## DESCRIPCION A DETALLE

Este sistema de gestion basicamente funciona como una rentadora de carros,
permitiendo asi la gestion de datos importantes para la empresa tales como
clientes, vehiculos o reservas de venta. El usuario podra agregar clientes nuevos,
registrar vehiculos disponibles y realizar reserevas de los autos en servicio. 
El programa está diseñado para manejar estos datos utilizando listas y diccionarios.

### IMPORTANCIA

El sistema de STAR CAR REN-A-CAR es muy productivo y eficaz para cualquier negocio que
 necesite gestionar inventarios de vehículos y su disponibilidad, asegurando un proceso organizado y eficiente.

 ### ALCANCE

 Eras son algunas de las funciones y facilidades de STAR CAR REN-A-CAR: - Registrar y gestionar la información de los clientes.
- Añadir y gestionar la lista de autos disponibles.
- Realizar y gestionar reservas de autos.
- Consultar el estado de los autos (disponibles o rentados).

### ESTRUCTURAS DE DATOS USADAS

- **Listas:** Para almacenar la lista de vehículos y la lista de clientes.
- **Diccionarios:** Para gestionar las reservas, enlazando clientes con los autos que han rentado.

## PSEUDO CÓDIGO

INICIO del programa

DEFINIR lista vehiculoss
DEFINIR lista clientes
DEFINIR diccionario reservas

FUNCIÓN agregar_vehiculos()
    PEDIR al usuario que ingrese el modelo del vehiculos
    AÑADIR el vehiculos a la lista de vehiculoss
    MOSTRAR mensaje confirmando que el vehiculos fue agregado

FUNCIÓN agregar_cliente()
    PEDIR al usuario que ingrese el nombre del cliente
    AÑADIR el cliente a la lista de clientes
    MOSTRAR mensaje confirmando que el cliente fue agregado

FUNCIÓN realizar_reserva()
    PEDIR al usuario que ingrese el nombre del cliente
    SI el cliente no está en la lista de clientes
        MOSTRAR mensaje de error y pedir que lo registre primero
        SALIR de la función
    FIN SI

    PEDIR al usuario que ingrese el modelo del vehiculos a reservar
    SI el vehiculos no está en la lista de vehiculoss
        MOSTRAR mensaje de error y que el vehiculos no está disponible
        SALIR de la función
    FIN SI

    ASIGNAR el vehiculos al cliente en el diccionario reservas
    ELIMINAR el vehiculos de la lista de vehiculoss disponibles
    MOSTRAR mensaje confirmando que la reserva se ha realizado con éxito

FUNCIÓN mostrar_estado_vehiculoss()
    MOSTRAR todos los vehiculoss disponibles en la lista de vehiculoss
    MOSTRAR todos los vehiculoss rentados y sus respectivos clientes del diccionario reservas

FUNCIÓN menu_principal()
    MIENTRAS el programa esté en ejecución
        MOSTRAR el menú de opciones:
            1. Agregar vehiculos
            2. Agregar cliente
            3. Realizar reserva
            4. Mostrar estado de vehiculoss
            5. Salir
        LEER opción seleccionada por el usuario

        SI la opción es '1'
            LLAMAR a la función agregar_vehiculos()
        SINO SI la opción es '2'
            LLAMAR a la función agregar_cliente()
        SINO SI la opción es '3'
            LLAMAR a la función realizar_reserva()
        SINO SI la opción es '4'
            LLAMAR a la función mostrar_estado_vehiculoss()
        SINO SI la opción es '5'
            MOSTRAR mensaje de salida
            TERMINAR el bucle
        SINO
            MOSTRAR mensaje de opción no válida
        FIN SI
    FIN MIENTRAS

LLAMAR a la función menu_principal()

FIN del programa



   
