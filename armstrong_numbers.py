def is_armstrong_number(number):
	holder = str(number)
	holder2 = 0
	for i in holder:
		holder2 += int(i) ** len(holder)
	if holder2 == number:
		return True
	else:
		return False

