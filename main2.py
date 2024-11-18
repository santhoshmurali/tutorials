from item import Item

item1 = Item("My Item",750)

try:
    #print(item1.name)
    item1.name = "Hi"
    #print(item1.name)
except ValueError as e:
    print(e)

print(item1.price)

