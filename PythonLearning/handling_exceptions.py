#try:
#	num = int(input("Enter a number: "))
#	r = 10 / num
#	print("Result: ", r)
#except ZeroDivisionError:
#	print("Error: You cannot divide by zero")
#except ValueError:
#	print("Error: Please enter a valid number")
#except Exception as e:
#	print("An error occurred: ", e)
#else:
#	print("No exceptions occurred")
#finally:
#	print("Execution completed")

"""
def calculate_age(year_born):
	current_year = 2025
	if year_born > current_year:
		raise ValueError("Invalid birth year")
	return current_year - year_born

try:
	birth_year = int(input("Enter birth year: "))
	age = calculate_age(birth_year)
	print("Age: ", age)
except ValueError as ve:
	print("Error: ", ve)
"""

class InsufficientFundsError(Exception):
	pass

def withdraw(balance, amount):
	if amount > balance:
		raise InsufficientFundsError("Insufficient funds")
	return balance - amount

try:
	account_balance = 500
	withdrawal_amount = int(input("Enter an amount to withdraw: "))
	remaining_balance = withdraw(account_balance, withdrawal_amount)
	print("Remaining balance: ", remaining_balance)
except InsufficientFundsError as ife:
	print("Error: ", ife)
