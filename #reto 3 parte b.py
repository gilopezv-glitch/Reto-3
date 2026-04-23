#reto 3 parte b
class MenuItem:
    def __init__(self,name: str, price: float):
        self.name = name
        self.price= price
    def calculate_price(self) -> float:
        return self.price
    
class bebida (MenuItem):
    def __init__(self, name: str, price: float, size:str):
        super().__init__(name,price)
        self.size=size
class aperitivo (MenuItem):
    def __init__(self, name: str, price: float, portion_size:str):
        super().__init__(name,price)
        self.portion_size=portion_size
class plato_fuerte (MenuItem):
    def __init__(self, name: str, price: float, calorias: int):
        super().__init__(name,price)
        self.calorias= calorias
class postre (MenuItem):
    def __init__(self, name: str, price: float, flavor:str):
        super().__init__(name,price)
        self.flavor= flavor

class order:
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)
    def calculate_total(self) -> float:
        return sum(item.calculate_price() for item in self.items)

    def apply_discount(self) -> float:
        total = self.calculate_total()
        if len(self.items) >= 5:
            return total * 0.9
        return total

#menu opciones
menu = [
    bebida("Gaseosa", 5.0, "Medium"),
    bebida("Cafe", 4.0, "Small"),
    bebida("Jugo", 6.0, "Large"),

    aperitivo("Nachos", 8.0, "Grande"),
    aperitivo("Pan", 7.0, "Personal"),
    aperitivo("Sopa", 6.5, "Personal"),

    plato_fuerte("Hamburguesa", 15.0, 800),
    plato_fuerte("Pizza", 20.0, 1200),
    plato_fuerte("Pasta", 18.0, 900),

    postre("Helado", 7.0, "Fresa"),
    postre("Pastel de Chocolate", 8.5, "Chocolate"),
    postre("Cheesecake", 6.0, "Vainilla"),
]