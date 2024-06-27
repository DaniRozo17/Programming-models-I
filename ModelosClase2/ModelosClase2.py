from typing import List, Dict

# Clase papá
class Product:
    def __init__(self, name: str, price: float, discount: float = 0):
        self.name = name
        self.price = price
        self.discount = discount

    def get_product_details(self) -> Dict:
        discounted_price = self.price * (1 - self.discount / 100)
        return {"name": self.name, "price": discounted_price, "discount(%)": self.discount}

# Clase usuario
class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.cart: List[Product] = []
        self.game_descriptions = GameDescriptions()  # Instancia única de GameDescriptions

    def add_to_cart(self, product: Product):
        self.cart.append(product)

    def get_cart_details(self) -> List[Dict]:
        cart_details = []
        for product in self.cart:
            description = self.game_descriptions.get_description(product.name)
            cart_details.append({"name": product.name, "price": product.price, "discount": product.discount, "description": description})
        return cart_details

    def clear_cart(self):
        self.cart = []


# Clase Tienda
class Store:
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)

    def list_products(self) -> List[Dict]:
        return [product.get_product_details() for product in self.products]

    def get_product(self, index: int) -> Product:
        return self.products[index]

# Clase papá (métodos de pago)
class Payment:
    def pay(self, amount: float):
        pass

# Clase hija (pago con tarjeta de crédito)
class CreditCardPayment(Payment):
    def pay(self, amount: float):
        print(f"Pagado {amount} con tarjeta de crédito.")

# Clase (pago con PayPal)
class PayPalPayment(Payment):
    def pay(self, amount: float):
        print(f"Pagado {amount} con PayPal.")


# Clase de descripciones (cada descripción de juego va a ser unica) Aqui aplica el método Singleton
class GameDescriptions:
    _instance = None

    def __new__(cls): # Método para obtener la instancia única de GameDescriptions
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.descriptions = {
                "The Legend of Zelda": "Aqui un valiente guerrero se encuentra con múltiples dificultades, puzzles y desafios para conseguir increibles premios",
                "Super Mario Odyssey": "Un pequeño heroe busca salvar a su princesa, para ello tendra que enfrentar hongos, trampas  demas desafios. ¿Podra lograrlo?",
                "Minecraft": "Un juego de construcción para todo público",
                "Fortnite": "Juego de disparos de manera online",
                "Among Us": "Juego de espionaje y crimen, ¿Podrás encontrar al impostor?",
                "Cyberpunk 2077": "Juego futurista y sobre su realidad despues del gran avance de la tecnología",
                "Stardew Valley": "Aqui podras cuidar una granja y divertirte con todas las tareas que esta tiene para tí",
                "The Witcher 3": "Un brujo que caza bestias se encuentra con dificultades aun mayores, ayudale a completar su desafio",
                "Hades": "Juego sobre el hades",
                "Celeste": "Juego rpg donde podras guiar a tu personaje por multiples retos que pondran a prueba tu destreza"
            }
        return cls._instance

    def get_description(self, game_name): # Método para obtener la descripción de un juego dado su nombre
        return self.descriptions.get(game_name, "Descripción no encontrada")


# Main de la aplicación
def main():
    store = Store()

    # Crear catálogo de juegos
    catalog = [
        Product("The Legend of Zelda", 59.99, 10),
        Product("Super Mario Odyssey", 49.99, 5),
        Product("Minecraft", 26.95, 15),
        Product("Fortnite", 0.00, 0),
        Product("Among Us", 5.00, 20),
        Product("Cyberpunk 2077", 59.99, 25),
        Product("Stardew Valley", 14.99, 10),
        Product("The Witcher 3", 39.99, 50),
        Product("Hades", 24.99, 5),
        Product("Celeste", 19.99, 15)
    ]

    for game in catalog:
        store.add_product(game)

    # Mostrar la tienda 
    print ("---------------------------------------")
    print ("BIENVENIDO A LA TIENDA DE VIDEOJUEGOS")
    print ("---------------------------------------")
    print("Catálogo de juegos:")
    print ("---------------------------------------")

    for idx, product in enumerate(store.list_products()):
        print(f"{idx + 1}. {product}")

    # Selección que va a hacer el usuario
    user = User(1, "gamer123")
    while True:
        choice = int(input("Ingrese el número del juego que desea agregar al carrito (0 para finalizar): "))
        if choice == 0:
            break
        elif 1 <= choice <= len(catalog):
            user.add_to_cart(store.get_product(choice - 1))
        else:
            print("Selección inválida. Por favor, intente nuevamente.")

    # Mostrar lo que el usuario va a comprar (carrito de compras)
    print("\nCarrito de compras:")
    total = 0
    for item in user.get_cart_details():
        print(item)
        total += item["price"]

    print(f"Total a pagar: {total}")

    # Selección de Métodos de pago
    payment_method = input("Seleccione método de pago (credit_card o paypal): ")
    if payment_method == "credit_card":
        payment = CreditCardPayment()
    elif payment_method == "paypal":
        payment = PayPalPayment()
    else:
        print("Método de pago inválido.")
        return

    payment.pay(total)
    user.clear_cart()

if __name__ == "__main__":
    main()


# Añadir un contador para saber cuantas instancias hace, osea que si compro el mismo juego dos veces pueda solo dar una vez la descripción
