__author__ = 'Matt'

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











