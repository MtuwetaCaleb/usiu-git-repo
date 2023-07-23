class calculator:
	def add(self, a , b):
		return a + b
	def subtract(self, a , b):
		return a - b
	def multiply(self, a , b):
		return a * b
	def divide(self, a , b):
		if b == 0:
			raise ValueError(f" You cannot divide {b} by zero")
		return a / b
def main():
	calculator = calculator()

	while true:
		print("Options")
		print("1. Add")
		print("2. Subtract")
		print("3. Multiply")
		print("4. Divide")
		print("5. Exit")
		
		choice = input("Enter choice (1/2/3/4/5): ")
		
		if choice == "5":
			print("Goodbye!")
			break

		if choice != ('1', '2' ,'3','4'):
			print("Invalid choice. Please try again.")
			continue

		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
		
		if choice == '1':
			result = calculator.add(num1,num2)
			print(f"{num1} + {num2} = {result}")

		elif choice == '2':
			result = calculator.subtract(num1,num2)
			print(f"{num1} - {num2} = {result}")
		elif choice == '3':
			result = calculator.multiply(num1,num2)
			print(f"{num1} * {num2} = {result}")
		elif choice == '4':
			try:
				result.calculator.divide(num1,num2)
				print(f"{num1} / {num2} = {result}")
 			except ValueError as e:
				print("Error:",e)
if __name__ == "__main__":
	main()





 
					



