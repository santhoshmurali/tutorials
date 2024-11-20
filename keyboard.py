from item import Item

class Keyboard(Item):
    '''
    This is the class we inherited from Item class.
    '''
    pay_rate = 0.7
    def __init__(self, name: str, price: float, quantity=1) -> None:
        super().__init__(name, price, quantity)