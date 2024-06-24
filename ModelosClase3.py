from abc import ABC, abstractmethod

# FACTORY METHOD 

# Clase abstracta del producto llamada videojuego
class Videojuego(ABC):
    @abstractmethod
    def nombre_juego(self):
        pass


# Clase del producto 1
class VideojuegoRPG(Videojuego):
    def nombre_juego(self):
        return "Juego de Rol (RPG)"

# Clase del producto 2
class VideojuegoFPS(Videojuego):
    def nombre_juego(self):
        return "Juego de Disparos en Primera Persona (FPS)"

# Clase del producto 3
class VideojuegoEstrategia(Videojuego):
    def nombre_juego(self):
        return "Juego de Estrategia"


# Creador de los productos videojuegos 
class CreadorJuegos(ABC):
    @abstractmethod
    def factory_method(self):
        pass
    
    def crear_juego(self):
        juego = self.factory_method()
        return juego
    

# Creador de producto videojuego en concreto 1
class CreadorJuegosRPG(CreadorJuegos):
    def factory_method(self):
        return VideojuegoRPG()

# Creador de producto videojuego en concreto 1
class CreadorJuegosFPS(CreadorJuegos):
    def factory_method(self):
        return VideojuegoFPS()

# Creador de producto videojuego en concreto 1
class CreadorJuegosEstrategia(CreadorJuegos):
    def factory_method(self):
        return VideojuegoEstrategia()


# Todo lo del main
def main():
    print("----------BIENVENIDO---------------")
    print("-----------------------------------")
    print("Acorde a la categoria que elijas podras tener un descuento en los juegos de la misma")
    print("Elige una categoría de videojuego: ")
    print("1. RPG (50%)")
    print("2. FPS (20%)")
    print("3. Estrategia (32%)")
    print("-----------------------------------")
    
    opcion = input("Ingresa el número de la categoría deseada: ")
    
    if opcion == "1":
        creador = CreadorJuegosRPG()
        descuento = 50
    elif opcion == "2":
        creador = CreadorJuegosFPS()
        descuento = 20
    elif opcion == "3":
        creador = CreadorJuegosEstrategia()
        descuento = 32
    else:
        print("Opción no válida.")
        return
    
    juego = creador.crear_juego()
    print(f"Categoria seleccionada: {juego.nombre_juego()}")
    print(f"FELICIDADES, por tu elección tendras un descuento del ",descuento,"%")

if __name__ == "__main__":
    main()
