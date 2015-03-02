__author__ = 'Matt'


import store
import database

# create store and add customers to list
better_buy = store.Store()
menu = store.Menu()
# name = menu.sign_up()
# print (name)
# # name1 = raw_input("what is your name? ")
# # # customer1 = store.Customer(11, name1)
# matt = database.Customer(name=name[0], email=name[1], password=name[2])
# matt.save()

# for customer in database.Customer:
#     print customer.name, customer.email
# customer2 = store.Customer(22, 'Ashley')
# better_buy.list_of_customers.append(customer1)
menu.sign_up()
print menu.customer
menu.show_customers()

# create list of inventory
laptop = store.InventoryItem(111, 'Laptop', 699.99)
tv = store.InventoryItem(222, 'TV', 1499.99)
xbox = store.InventoryItem(333, 'Xbox One', 349.99)
better_buy.available_inventory = [laptop, tv, xbox]
print(better_buy.available_inventory)

# grab customer1 and add laptop to his cart
# customer1.cart.buy(laptop)
# customer1.view_cart()
