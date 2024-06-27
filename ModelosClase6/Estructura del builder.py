from typing import List

class Director:
    def __init__(self, constructor):
        self.constructor = constructor
    
    def construir(self, datos: str):
        tokens = datos.split()
        i = 0
        while i < len(tokens):
            if tokens[i] == "<CLIENTE>":
                dato_cliente = []
                i += 1
                while tokens[i] != "</CLIENTE>":
                    dato_cliente.append(tokens[i])
                    i += 1
                cliente = " ".join(dato_cliente)
                self.constructor.construir_cliente(cliente)
            elif tokens[i] == "<PRODUCTO>":
                dato_producto = []
                i += 1
                while tokens[i] != "</PRODUCTO>":
                    dato_producto.append(tokens[i])
                    i += 1
                producto = " ".join(dato_producto)
                self.constructor.construir_producto(producto)
            i += 1

class EjemploBuilder:
    @staticmethod
    def main():
        datos = "<CLIENTE> Jose Juncal </CLIENTE> <PRODUCTO> Miel </PRODUCTO> <PRODUCTO> Tomates </PRODUCTO>"
        constructor_concreto = ConstructorConcreto()
        director = Director(constructor_concreto)
        director.construir(datos)
        c = constructor_concreto.get_cliente()
        print(c)

class Constructor:
    def construir_cliente(self, cliente: str):
        pass
    
    def construir_producto(self, producto: str):
        pass

class ConstructorConcreto(Constructor):
    def __init__(self):
        self.cliente = None
    
    def construir_cliente(self, datos_cliente: str):
        self.cliente = Cliente(datos_cliente)
    
    def construir_producto(self, datos_producto: str):
        self.cliente.agregar_producto(datos_producto)
    
    def get_cliente(self):
        return self.cliente

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def __str__(self):
        return f"Cliente: {self.nombre}, Productos: {', '.join(self.productos)}"

# Ejecutar el método main para probar el código
EjemploBuilder.main()
