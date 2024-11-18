from item import Item

class Phone(Item):
    '''
    This is the class we inherited from Item class.
    '''
    def __init__(self, name: str, price: float, quantity=1,broken_phone=0) -> None:
        super().__init__(name, price, quantity)
        assert broken_phone >= 0, f"Brokecn Phones {broken_phone} is not greater than or equal 0"
        self.broken_phone = broken_phone