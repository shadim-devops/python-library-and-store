class Product:
    def __init__(self, name, price, code):
        self.name = name
        self.price = price
        self.code = code

    def final_price(self):
        return self.price


class Electronics(Product):
    def __init__(self, name, price, code, warranty):
        super().__init__(name, price, code)
        self.warranty = warranty

    def final_price(self):
        return self.price * 1.23


class Clothing(Product):
    def __init__(self, name, price, code, size):
        super().__init__(name, price, code)
        self.size = size

    def final_price(self):
        return self.price * 1.1


class Book(Product):
    def __init__(self, name, price, code, author):
        super().__init__(name, price, code)
        self.author = author

    def final_price(self):
        return self.price


class ShoppingCart:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)
        print("Added to cart:", product.name)

    def remove_product(self, code):
        for p in self.__products:
            if p.code == code:
                self.__products.remove(p)
                print("Removed product:", p.name)
                return

    def total(self):
        total = 0
        for p in self.__products:
            total += p.final_price()
        return total


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Customer(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.order_history = []


class Administrator(User):
    def __init__(self, name, email):
        super().__init__(name, email)

    def add_product(self, store, product):
        store.append(product)
        print("Administrator added product:", product.name)


class Order:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer
        self.status = "new"

    def pay(self):
        self.status = "paid"
        print("Order paid. Amount:", self.cart.total())


p1 = Electronics("Laptop", 5000, "E1", "24 miesiace")
p2 = Clothing("T-shirt", 100, "U1", "L")
p3 = Book("Python for Beginners", 100, "K1", "Example Author")

cart = ShoppingCart()
cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

print("Cart total:", cart.total())

customer = Customer("Adam", "customer@example.com")

zam = Order(cart, customer)
zam.pay()
