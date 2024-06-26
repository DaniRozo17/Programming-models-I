# Patrón Prototype
# Daniel J Rozo R

import copy

class Ticket:
    def __init__(self, evento, fecha, lugar, asiento=None, nombre=None, precio=0):
        self.evento = evento
        self.fecha = fecha
        self.lugar = lugar
        self.asiento = asiento
        self.nombre = nombre
        self.precio = precio

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return (f'Evento: {self.evento}, Fecha: {self.fecha}, Lugar: {self.lugar}, '
                f'Asiento: {self.asiento}, Nombre: {self.nombre}, Precio: ${self.precio}')

def mostrar_opciones_asiento(asientos_disponibles):
    print("Opciones de asiento disponibles:")
    for idx, (asiento, precio) in enumerate(asientos_disponibles.items()):
        print(f"{idx + 1}. Asiento: {asiento}, Precio: ${precio}")

def elegir_asiento(asientos_disponibles):
    while True:
        try:
            opcion = int(input("Elige una opción de asiento (1-4): "))
            if 1 <= opcion <= 4:
                asiento = list(asientos_disponibles.keys())[opcion - 1]
                precio = asientos_disponibles[asiento]
                return asiento, precio
            else:
                print("Opción no válida, por favor elige un número entre 1 y 4.")
        except ValueError:
            print("Entrada no válida, por favor ingresa un número.")

def generar_ticket():
    # Prototipo de ticket base
    ticket_base = Ticket(evento="Concierto de Jazz", fecha="2024-07-15", lugar="Estadio Nacional")

    # Para pedir info del usuario del ticket
    print("--------------------------------------------------------------------------------------")
    print("------------------------------TIENDO DE TIKCETS---------------------------------------")
    print("Bienvenido a la tienda tickets, a continuación encontrará los asientos disponibles para el concierto de Jazz que se dara el 15 de Julio de este año")
    print("--------------------------------------------------------------------------------------")
    nombre = input("Ingresa tu nombre: ")

    # Opciones de asientos disponibles
    asientos_disponibles = {
        "A1": 80,
        "A2": 92,
        "B1": 40,
        "B2": 37
    }
    
    # Mostrar opciones y elegir asiento
    mostrar_opciones_asiento(asientos_disponibles)
    asiento, precio = elegir_asiento(asientos_disponibles)
    
    # Crear el ticket personalizado clonando el prototipo base
    nuevo_ticket = ticket_base.clone()
    nuevo_ticket.nombre = nombre
    nuevo_ticket.asiento = asiento
    nuevo_ticket.precio = precio
    
    # Mostrar la factura
    print("\nFactura del Ticket:")
    print(nuevo_ticket)

# Generar un ticket interactivo
generar_ticket()
