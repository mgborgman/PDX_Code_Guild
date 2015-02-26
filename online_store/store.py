__author__ = 'Matt Borgman'

import database


class Store(object):
    def __init__(self):
        self.list_of_customers = []
        self.available_items = []


class Customer(object):
    def __init__(self, name='none', email='none'):
        self.name = name
        self.email = email
        self.cart = Cart()


class Cart(object):
    def __init__(self):
        pass


class Menu(object):
    def __init__(self):
        pass


    def print_menu_main(self):
        print("BetterBuy.com")
        print("1. Log in")
        print("2. Sign up")
        print("3. Exit")
        menu_select = raw_input("Please Log in to shop with us! \n")
        return menu_select

    '''main menu'''
    def use_menu(self, select, store):
        try:
            if select == '1':
                self.log_in(store)
            elif select == '2':
                self.sign_up(store)
        except ValueError:
            print("Please enter a number")

    '''ask user for name and email and store in list'''
    def sign_up(self, store):
        name = raw_input("What is your name? ")
        email = raw_input("What is your email? ")
        store.list_of_customers.append([name, email])

    '''ask user for name and email and compare to database'''
    def log_in(self, store):
        name = raw_input("Name: ")
        email = raw_input("Email: ")
    '''compare entered log in name to name in database'''
        # if database.c.execute('SELECT name FROM TABLE WHERE name= ?, name)

'''TESTING'''
better_buy = Store()
main = Menu()
select = main.print_menu_main()
main.use_menu(select, better_buy)
print(better_buy.list_of_customers)
select = main.print_menu_main()
main.use_menu(select, better_buy)
print(better_buy.list_of_customers)