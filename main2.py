from item import Item
from phone import Phone
from keyboard import Keyboard

item1 = Item("My Item",750)
item2 = Phone("IQOO07",1000,4,2)
item3 = Keyboard("SAMSUNG",300,4)

try:
    #print(item1.name)
    item1.name = "Hi"
    #print(item1.name)
except ValueError as e:
    print(e)

#print(item1.price)
#item1.apply_discount()
print(item1.price)
item1.apply_increment(0.2)
print(item1.price)


print(f"the price of {item2.name} is {item2.price}, we have {item2.broken_phone} broken phones")
item2.apply_discount()
print(f"after price discount it comes to be {item2.price}")

