from item import Item
from phone import Phone

item_for_class_attribute = Item("Phone",100,5)
print(f"Default pay_rate is {item_for_class_attribute.pay_rate}")
print(f"Original price of phone {item_for_class_attribute.__price}")
item_for_class_attribute.apply_discount()
print(f"after applying the discount the price is {item_for_class_attribute.__price}")

item_for_updatating_class_attribute = Item("Laptop",1000,3)
item_for_updatating_class_attribute.pay_rate = 0.7
print(f"modified pay_rate is {item_for_updatating_class_attribute.pay_rate}")
print(f"Original Price of laptop {item_for_updatating_class_attribute.__price}")
item_for_updatating_class_attribute.apply_discount()
print(f"after overriding the discount rate to 0.3 for laptop {item_for_updatating_class_attribute.__price}")
print('-------------------------')


phone1 = Phone("Santhosh Phone",500,5,1)
print(phone1.claculate_total_price())
print(Item.all)
print(Phone.all)




