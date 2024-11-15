import sys

class Item:
    """Class representing a item"""
    def __init__(self, name:str, price:float, quantity=1) -> None:
        # run validation to the received arguments
        assert price >= 0, f"price {price} is not greater than or equal to 0!"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal 0!"


        # assign to self object
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



