# Patrón Builder
# Daniel J Rozo R

from abc import ABC, abstractmethod

# Clase Director
class Director:
    def __init__(self, constructor):
        self.constructor = constructor
    
    def construir_casa(self, tipo_casa, opciones):
        if tipo_casa == 'moderna':
            self.constructor.construir_paredes(opciones.get('paredes', 'Ladrillo'))
            self.constructor.construir_techo(opciones.get('techo', 'Tejas'))
            self.constructor.construir_pisos(opciones.get('pisos', 'Madera'))
        elif tipo_casa == 'clasica':
            self.constructor.construir_paredes(opciones.get('paredes', 'Piedra'))
            self.constructor.construir_techo(opciones.get('techo', 'Tejas'))
            self.constructor.construir_pisos(opciones.get('pisos', 'Madera'))

# Clase Casa
class Casa:
    def __init__(self):
        self.paredes = None
        self.techo = None
        self.pisos = None

    def __str__(self):
        return f"Casa con paredes de {self.paredes}, techo de {self.techo} y pisos de {self.pisos}"

# Clase abs Constructor
class Constructor(ABC):
    @abstractmethod
    def construir_paredes(self, tipo_paredes: str):
        pass
    
    @abstractmethod
    def construir_techo(self, tipo_techo: str):
        pass
    
    @abstractmethod
    def construir_pisos(self, tipo_pisos: str):
        pass
    
    @abstractmethod
    def obtener_casa(self):
        pass

# ConstructorConcreto para Casa Moderna
class ConstructorCasaModerna(Constructor):
    def __init__(self):
        self.casa = Casa()
    
    def construir_paredes(self, tipo_paredes: str):
        self.casa.paredes = f"{tipo_paredes} modernas"
    
    def construir_techo(self, tipo_techo: str):
        self.casa.techo = f"{tipo_techo} moderno"
    
    def construir_pisos(self, tipo_pisos: str):
        self.casa.pisos = f"{tipo_pisos} modernos"
    
    def obtener_casa(self):
        return self.casa

# ConstructorConcreto para Casa Clásica
class ConstructorCasaClasica(Constructor):
    def __init__(self):
        self.casa = Casa()
    
    def construir_paredes(self, tipo_paredes: str):
        self.casa.paredes = f"{tipo_paredes} clásicas"
    
    def construir_techo(self, tipo_techo: str):
        self.casa.techo = f"{tipo_techo} clásico"
    
    def construir_pisos(self, tipo_pisos: str):
        self.casa.pisos = f"{tipo_pisos} clásicos"
    
    def obtener_casa(self):
        return self.casa


# Función para elegir opción
def elegir_opcion(tipo_opcion: str, opciones: list) -> str:
    print(f"Selecciona el tipo de {tipo_opcion}:")
    for i, opcion in enumerate(opciones):
        print(f"{i + 1}. {opcion}")
    while True:
        seleccion = input(f"Ingresa el número de opción (1-{len(opciones)}): ")
        try:
            seleccion_idx = int(seleccion) - 1
            if 0 <= seleccion_idx < len(opciones):
                return opciones[seleccion_idx]
            else:
                print("Selección inválida. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")

# Función principal
def main():
    print("--------------------------------------------------------------------------------------")
    print("------------------------------ CONSTRUCTOR DE CASAS ----------------------------------")
    print("Bienvenido a la fábrica de casas, por favor indique cómo quiere que sea ésta")
    print("--------------------------------------------------------------------------------------")

    tipo_casa = elegir_opcion('Tipo de Casa', ['moderna', 'clasica'])

    if tipo_casa == 'moderna':
        constructor = ConstructorCasaModerna()
    elif tipo_casa == 'clasica':
        constructor = ConstructorCasaClasica()

    director = Director(constructor)

    opciones = {
        'paredes': elegir_opcion('Paredes', ['Ladrillo', 'Piedra']),
        'techo': elegir_opcion('Techo', ['Tejas', 'Chapa']),
        'pisos': elegir_opcion('Pisos', ['Madera', 'Cerámica', 'Hormigón'])
    }

    director.construir_casa(tipo_casa, opciones)
    casa = constructor.obtener_casa()
    print(casa)

# Ejecución del programa
if __name__ == "__main__":
    main()
