import csv

class Item:
    """Class representing a item"""
    pay_rate = 0.8
    all = []

    def __init__(self, name:str, price:float, quantity=1) -> None:
        # run validation to the received arguments
        assert price >= 0, f"price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal 0"

        # assign to self object
        self._name = name
        self.__price = price
        self.quantity = quantity

        # append all instances
        Item.all.append(self)

    def claculate_total_price(self):
        """method representing the price calulcation"""
        return self.__price * self.quantity


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}',{self.__price},{self.quantity})"
    

    @classmethod
    def instantiate_from_class(cls):
        with open("Items.csv","r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
    
    @staticmethod
    def num_is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
    
    @property # we call it as a getter
    def name(self):
        '''name attribute'''
        print(f"you are trying to get {self._name}")
        return self._name
    
    @name.setter # we will call it as a setter
    def name(self, value):
        print(f"you are trying to set {value}")
        if isinstance(value,str) and len(value)>0:
            self._name = value
        else:
            raise ValueError("Value needs to be non-Null string value")

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        """ Apply discounts"""
        self.__price = self.__price * self.pay_rate

    def apply_increment(self,increment_value):
        '''  increment the product price'''
        self.__price = self.__price + (self.__price*increment_value)
        
            
