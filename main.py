import sys

class Item:
    """Class representing a item"""
    def __init__(self, name, price=1, quantity=1) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def claculate_total_price(self):
        """method representing the price calulcation"""
        return self.price * self.quantity


item1 = Item("Phone",100,5)
item2 = Item("Computer",1000,5)
item3 = Item("Charger",5)
print(item1.claculate_total_price())
print(item2.claculate_total_price())
print(item3.claculate_total_price())



