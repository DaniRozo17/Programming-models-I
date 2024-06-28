# Patrón Prototype
# Daniel J Rozo R

import copy
import time
from datetime import datetime

# Clase Ticket
class Ticket:
    def __init__(self, evento, fecha, lugar, asiento=None, nombre=None, precio=0):
        self.evento = evento
        self.fecha = fecha
        self.lugar = lugar
        self.asiento = asiento
        self.nombre = nombre
        self.precio = precio
        self.timestamp = time.time()  # Agregar un timestamp para mostrar el tiempo actual
    
    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        formatted_time = datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')
        return (f"Evento: {self.evento}, Fecha: {self.fecha}, Lugar: {self.lugar}, "
                f"Asiento: {self.asiento}, Nombre: {self.nombre}, Precio: ${self.precio}, "
                f"Fecha de pago: {formatted_time}\n")

# otras funciones
def mostrar_opciones_asiento(asientos_disponibles):
    print("Opciones de asiento disponibles:")
    for idx, (asiento, precio) in enumerate(asientos_disponibles.items()):
        print(f"{idx + 1}. Asiento: {asiento}, Precio: ${precio}")

def elegir_asiento(asientos_disponibles):
    while True:
        try:
            opcion = int(input("Elige una opción de asiento (1-4): "))
            if 1 <= opcion <= len(asientos_disponibles):
                asiento = list(asientos_disponibles.keys())[opcion - 1]
                precio = asientos_disponibles.pop(asiento)  # Eliminar el asiento elegido de las opciones disponibles (en caso de que se genere más de un ticket)
                return asiento, precio
            else:
                print(f"Opción no válida, por favor elige un número entre 1 y {len(asientos_disponibles)}.")
        except ValueError:
            print("Entrada no válida, por favor ingresa un número.")

# Esta es la función principal
def generar_tickets():
    # Prototipo de ticket base
    ticket_base = Ticket(
        evento="Concierto de Jazz",
        fecha="2024-07-15",
        lugar="Estadio El Campín"
    )

    # Para pedir info del usuario del ticket
    print("--------------------------------------------------------------------------------------")
    print("------------------------------TIENDA DE TICKETS---------------------------------------")
    print("Bienvenido a la tienda de tickets, a continuación encontrará los asientos disponibles para el concierto de Jazz que se dara el 15 de Julio de este año")
    print("--------------------------------------------------------------------------------------")
    nombre = input("Ingresa tu nombre: ")

    # Solicitar la cantidad de tickets a generar
    while True:
        try:
            cantidad_tickets = int(input("¿Cuántos tickets deseas generar? "))
            if cantidad_tickets > 0:
                break
            else:
                print("Por favor, ingresa un número mayor a 0.")
        except ValueError:
            print("Entrada no válida, por favor ingresa un número.")

    # Opciones de asientos disponibles
    asientos_disponibles = {
        "A1": 80,
        "A2": 92,
        "B1": 40,
        "B2": 37
    }

    tickets_generados = []  #Lista de tickets, en caso de generar más de uno solo
    
    # Generar los tickets solicitados
    for i in range(cantidad_tickets):
        if not asientos_disponibles:
            print("No hay más asientos disponibles.")
            break
        
        print(f"\nGenerando ticket {i + 1} de {cantidad_tickets}:")

        # Mostrar opciones y elegir asiento
        mostrar_opciones_asiento(asientos_disponibles)
        asiento, precio = elegir_asiento(asientos_disponibles)
        
        # Crear el ticket personalizado clonando el prototipo base
        nuevo_ticket = ticket_base.clone()
        nuevo_ticket.nombre = nombre
        nuevo_ticket.asiento = asiento
        nuevo_ticket.precio = precio
        
        # Añadir el ticket a la lista de tickets generados
        tickets_generados.append(nuevo_ticket)
    
    # Mostrar las facturas de los tickets generados
    print("\nFacturas de los Tickets Generados:")
    for ticket in tickets_generados:
        print(ticket)

# Generar tickets 
generar_tickets()
