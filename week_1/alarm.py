def sleep_in(weekday, vacation):
	if weekday == True and vacation == True:
		return True
	elif weekday == True and vacation == False:
		return False
	elif weekday == False and vacation == True:
		return True
	elif weekday == False and vacation == False:
		return True

# weekday = raw_input("is it a weekday? ")
# vacation = raw_input("are you on vacation? ")


print sleep_in(True, True)
print sleep_in(True, False) 
print sleep_in(False, True) 