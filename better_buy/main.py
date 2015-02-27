__author__ = 'Matt'


import store

# create store and add customers to list
better_buy = store.Store()
name1 = raw_input("what is your name? ")
customer1 = store.Customer(11, name1)
customer2 = store.Customer(22, 'Ashley')
better_buy.list_of_customers.append(customer1)
better_buy.list_of_customers.append(customer2)
print(better_buy.list_of_customers)

# create list of inventory
laptop = store.InventoryItem(111, 'Laptop', 699.99)
tv = store.InventoryItem(222, 'TV', 1499.99)
xbox = store.InventoryItem(333, 'Xbox One', 349.99)
better_buy.available_inventory = [laptop, tv, xbox]
print(better_buy.available_inventory)

# grab customer1 and add laptop to his cart
better_buy.buy(customer1, laptop)
print(customer1.cart)
