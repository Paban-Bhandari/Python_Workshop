class Number:
    def __init__(self):
        pass
    
    def check_odd_even(self, number):
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"
        
checker = Number()

# Get user input
user_input = input("Enter a number: ")

# Convert user input to integer (assuming the input is numeric)
try:
    number = int(user_input)
    result = checker.check_odd_even(number)
    print(f"The number {number} is {result}.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
