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
    # method to allow customers to purchase items. ex: user.cart.buy(laptop)
    # @item = InventoryItem object
    def buy(self, item):
        self.items.append(item)


class Menu(object):
    # empty list customer is created, this is where database objects will be stored
    customer = None
    # allows users to register with site and later login, allows cart and purchases to be tracked
    def sign_up(self):
        name = raw_input("Name: ")
        email = raw_input("Email: ")
        password = raw_input("Password: ")
        self.customer = database.Customer(name=name, email=email, password=password)
        self.customer.save()
        return [name, email, password]

    # lists all customers in Customer database
    def show_customers(self):
        for name in database.Customer:
            print name.name, name.email, name.password

    # User login which checks customer database to see if user has registered with site
    def login(self):
        email = raw_input("Email: ")
        password = raw_input("Password: ")

        for customer in database.Customer:
            if email == customer.email and password == customer.password:
                print("Welcome back {}".format(customer.name))











