from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    La interfaz Handler declara un método para construir la cadena de manejadores.
    También declara un método para ejecutar una solicitud.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    El comportamiento predeterminado de encadenamiento se puede implementar dentro de una clase base de manejador.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Devolver un manejador desde aquí nos permitirá enlazar los manejadores de una
        # manera conveniente como esta:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


"""
Todos los Concrete Handlers manejan una solicitud o la pasan al siguiente manejador en la cadena.
"""


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "Plátano":
            return f"Mono: Yo comeré el {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "Nuez":
            return f"Ardilla: Yo comeré la {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "Albóndiga":
            return f"Perro: Yo comeré la {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    El código del cliente suele estar diseñado para trabajar con un solo manejador.
    En la mayoría de los casos, ni siquiera sabe que el manejador es parte de una cadena.
    """

    for comida in ["Nuez", "Plátano", "Taza de café"]:
        print(f"\nCliente: ¿Quién quiere un(a) {comida}?")
        resultado = handler.handle(comida)
        if resultado:
            print(f"  {resultado}")
        else:
            print(f"  {comida} quedó sin tocar.")


if __name__ == "__main__":
    mono = MonkeyHandler()
    ardilla = SquirrelHandler()
    perro = DogHandler()

    mono.set_next(ardilla).set_next(perro)

    # El cliente debería poder enviar una solicitud a cualquier manejador, no solo al primero en la cadena.
    print("Cadena: Mono > Ardilla > Perro")
    client_code(mono)
    print("\n")
