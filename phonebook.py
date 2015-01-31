def search(ask):
	if ask in phonebook:
		print phonebook[ask]
	else:
		print "Name not found"
		add = raw_input("Would you like to make an entry? ")

		if add.lower() == 'yes' or add.lower() == 'y':
			name = raw_input("what is entries name? ")
			number = raw_input("what is entries number? ")
			phonebook[name] = {'name': name, 'number':number}			
			print phonebook

def remove(ask2):
	if ask2.lower() == 'yes' or ask2.lower() == 'y':
		print phonebook		
		remove = raw_input("Who would you like to remove? ")
		if remove in phonebook:
			phonebook.pop(remove)


def edit(ask3):
	if ask3.lower() == 'yes' or ask3.lower() =='y':
		name = raw_input("which entry would you like to edit? ")
		print phonebook[name]
		phonebook_name = raw_input("Enter name for entry: ")
		phonebook_number = raw_input("Enter number for entry: ")
		phonebook[phonebook_name] = phonebook.pop(name)
		phonebook[phonebook_name] = {'name': phonebook_name, 'number':phonebook_number}
		print phonebook[phonebook_name]

phonebook = {
			"Matt" : {'name':'Matt','number':"360-521-1315"},
			"Mike" : {'name':'Mike','number':'360-555-1234'},
			"Chris": {'name':'Chris','number':'503-277-9710'},
			}

while True:
	ask = raw_input("Who would you like to call? ")
	search(ask)

	ask2 = raw_input("would you like to remove any entries? ")
	remove(ask2)
	print phonebook

	ask3 = raw_input("Would you like to edit any entires? ")
	edit(ask3)
	



	# end = raw_input("would you like to do more? ")
	# if end.lower() == 'yes' or end.lower() == 'y':
	# 	return True
	# else: 
	# 	return False



#print phonebook
#name = raw_input("Name: ") figure out  new way to add name
#number = raw_input("phone number: ") "" add number
#phonebook['new_name'] = name
#phonebook['new_number'] = number
#print phonebook



