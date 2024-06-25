# Patrón Astract Factory
# Daniel J Rozo R

from abc import ABC, abstractmethod

# Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_engine(self):  #El motor
        pass
    
    @abstractmethod
    def create_chassis(self):  #El chasis
        pass
    
    @abstractmethod
    def create_interior(self):  #El interior
        pass

# El factory para los modelos Sedan (CONCRETE FACTORY)
class SedanFactory(AbstractFactory):
    def create_engine(self):
        return SedanEngine()
    
    def create_chassis(self):
        return SedanChassis()
    
    def create_interior(self):
        return SedanInterior()

# El factory para los modelos SUV (CONCRETE FACTORY)
class SUVFactory(AbstractFactory):
    def create_engine(self):
        return SUVEngine()
    
    def create_chassis(self):
        return SUVChassis()
    
    def create_interior(self):
        return SUVInterior()

#---------------------------------------------------

# Abstract Product: Motor (Padre)
class Engine(ABC):
    @abstractmethod
    def specs(self):
        pass

# Concrete Products: Motor Sedan (Hijo motor)
class SedanEngine(Engine):
    def specs(self):
        return "Motor type: 4-cilindros"

# Concrete Products: SUV Sedan (Hijo motor)
class SUVEngine(Engine):
    def specs(self):
        return "Motor type: 6-cilindros"
    
#---------------------------------------------------

# Abstract Product: Chasis (Padre)
class Chassis(ABC):
    @abstractmethod
    def specs(self):
        pass

# Concrete Products: Chasis Sedan (Hijo chasis)
class SedanChassis(Chassis):
    def specs(self):
        return "Chassis type: Chasis independiente"

# Concrete Products: Chasis SUV (Hijo chasis)
class SUVChassis(Chassis):
    def specs(self):
        return "Chassis type: Chasis autoportante"
    
#----------------------------------------------------

# Abstract Product: Interior
class Interior(ABC):
    @abstractmethod
    def specs(self):
        pass

# Concrete Products: Sedan Interior
class SedanInterior(Interior):
    def specs(self):
        return "Interior type: Asientos de cuero"

# Concrete Products: SUV Interior
class SUVInterior(Interior):
    def specs(self):
        return "Interior type: Asientos de tela"

#---------------------------------------------------

# Aqui va el Singleton
class CarFactoryManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.factory = None
        return cls._instance
    
    def set_factory(self, factory):
        self.factory = factory
    
    def get_factory(self):
        return self.factory

if __name__ == "__main__":
    print("---------------------------------------------------------------------------------------------")
    print("------------------------------TIENDA AUTOMOTRIZ DANIEL---------------------------------------")
    print("Bienvenido a la fabrica de automoviles, contamos con convienios de fabricación con dos marcas")
    print("¿Qué tipo de vehículo deseas adquirir (se creara acorde al modelo que elija)?")
    print("1. Sedán")
    print("2. SUV")
    print("---------------------------------------------------------------------------------------------")
    choice = input("Ingresa el número correspondiente a tu elección: ")
    
    factory_manager = CarFactoryManager()
    
    if choice == '1':
        factory_manager.set_factory(SedanFactory())
    elif choice == '2':
        factory_manager.set_factory(SUVFactory())
    else:
        print("Opción no válida. Saliendo del programa.")
        exit()
    
    engine = factory_manager.get_factory().create_engine()
    chassis = factory_manager.get_factory().create_chassis()
    interior = factory_manager.get_factory().create_interior()
    
    print("---------------------------------------------------------------------------------------------")
    print("Creando el vehículo:")
    print(engine.specs())
    print(chassis.specs())
    print(interior.specs())
    print("---------------------------------------------------------------------------------------------")
    print("GRACIAS POR VENIR")

