from pprint import pprint
import sys

def main_menu():
	print "============================="
	print "1. List phonebook entries"
	print "2. Add an entry"
	print "3. Edit entry"
	print "4. Remove entry"
	print "5. Search for number"
	print "6. Exit"
	selection = raw_input("What would you like to do? ")
	print "============================="

	if selection == '1':
		pprint(phonebook)
		main_menu()
	elif selection == '2':
		add()
		pprint(phonebook)
		main_menu()
	elif selection == '3':
		edit()
		main_menu()
	elif selection == '4':
		remove()
		main_menu()
	elif selection == '5':
		search()
		main_menu()
	elif selection == '6':
		sys.exit()


def add():
	name = raw_input("Name: ")
	number = raw_input("Number: ")
	phonebook[name] = {'name': name, 'number': number}

def edit():
	name = raw_input("which entry would you like to edit? ")
	print phonebook[name]
	phonebook_name = raw_input("Enter name for entry: ")
	phonebook_number = raw_input("Enter number for entry: ")
	phonebook[phonebook_name] = phonebook.pop(name)
	phonebook[phonebook_name] = {'name': phonebook_name, 'number':phonebook_number}
	print phonebook[phonebook_name]

def remove():
	pprint(phonebook)		
	remove = raw_input("Who would you like to remove? ")
	if remove in phonebook:
		phonebook.pop(remove)

def search():
	name = raw_input("Name: ")
	if name in phonebook:
		print phonebook[name]


phonebook = {
			"Matt" : {'name':'Matt','number':"360-521-1315"},
			"Mike" : {'name':'Mike','number':'360-555-1234'},
			"Chris": {'name':'Chris','number':'503-277-9710'},
			}

main_menu()



