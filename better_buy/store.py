__author__ = 'Matt'

'''first attempt @ store. No persistence.'''


# store class
# list_of_customers take str and int data
# available_inventory take str, int, and float data
class Store(object):
    def __init__(self):
        self.list_of_customers = []
        self.available_inventory = []

    def buy(self, customer, item):
        customer.cart = [item]


class Customer(object):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.cart = Cart()

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class InventoryItem(object):
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

    def __repr__(self):
        return"{}, {}, {}".format (self.name, self.item_id, self.price)


class Cart(object):
    def __init__(self):
        self.items = []






