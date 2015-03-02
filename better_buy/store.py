__author__ = 'Matt'
import database

'''first attempt @ store. No persistence.'''


# store class
# list_of_customers take str and int data
# available_inventory take str, int, and float data
class Store(object):
    def __init__(self):
        self.list_of_customers = []
        self.available_inventory = []


class Customer(object):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.cart = Cart()

    def __repr__(self):
        return "{}".format(self.name)

    def view_cart(self):
        for item in self.cart.items:
            print("you have a {} in your cart").format(item)


class InventoryItem(object):
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

    def __repr__(self):
        return "{} {} {}".format(self.item_id, self.name, self.price)

    def __str__(self):
        return self.name

class Cart(object):
    def __init__(self):
        self.items = []

    def buy(self, item):
        self.items.append(item)


class Menu(object):
    customer = None
    def sign_up(self):
        name = raw_input("Name: ")
        email = raw_input("Email: ")
        password = raw_input("Password: ")
        self.customer = database.Customer(name=name, email=email, password=password)
        self.customer.save()
        return [name, email, password]

    def show_customers(self):
        for name in database.Customer:
            print name.name, name.email, name.password











