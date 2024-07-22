################################################################
#Making simple Calculator using class
class calculator:
    def __init__(self, num):
        self.number = num
        self.splited_data = None
        self.total_amt = 0
        print(self.number)
    
    def sumFunction(self):
        self.total_amt = int(self.splited_data[0]) + int(self.splited_data[1])
        print(self.total_amt)

    def subFunction(self):
        self.total_amt = int(self.splited_data[0]) - int(self.splited_data[1])
        print(self.total_amt)

    def multiplyFunction(self):
        self.total_amt = int(self.splited_data[0]) * int(self.splited_data[1])
        print(self.total_amt)

    def divideFunction(self):
        self.total_amt = int(self.splited_data[0]) / int(self.splited_data[1])
        print(self.total_amt)

    def splitFunction(self):
        if '+' in self.number:
            #print(self.number.split("+"))
            self.splited_data = self.number.split("+")
            #print(self.splited_data)
            self.sumFunction()
        elif '-' in self.number:
            self.splited_data = self.number.split("-")
            self.subFunction()
        elif '*' in self.number:
            self.splited_data = self.number.split("*")
            self.multiplyFunction()
        elif '/' in self.number:
            self.splited_data = self.number.split("/")
            self.divideFunction()
        
while True:
    print("\t\t\t\t\t\tPlease enter exit to quit if you want")
    user_input = input("Enter a number to calculate: ")
    if user_input == "exit":
        break
    else:
        obj4 = calculator(user_input)
        print(obj4.splitFunction())
################################################################

# import math

# class Calculator:
#     def __init__(self, num):
#         self.number = num
#         self.splited_data = None
#         self.total_amt = 0
#         print(self.number)
    
#     def sumFunction(self):
#         self.total_amt = int(self.splited_data[0]) + int(self.splited_data[1])
#         print(self.total_amt)

#     def subFunction(self):
#         self.total_amt = int(self.splited_data[0]) - int(self.splited_data[1])
#         print(self.total_amt)

#     def multiplyFunction(self):
#         self.total_amt = int(self.splited_data[0]) * int(self.splited_data[1])
#         print(self.total_amt)

#     def divideFunction(self):
#         self.total_amt = int(self.splited_data[0]) / int(self.splited_data[1])
#         print(self.total_amt)

#     def sqrtFunction(self):
#         self.total_amt = math.sqrt(float(self.number.split("^")[1]))
#         print(self.total_amt)

#     def splitFunction(self):
#         if '+' in self.number:
#             self.splited_data = self.number.split("+")
#             self.sumFunction()
#         elif '-' in self.number:
#             self.splited_data = self.number.split("-")
#             self.subFunction()
#         elif '*' in self.number:
#             self.splited_data = self.number.split("*")
#             self.multiplyFunction()
#         elif '/' in self.number:
#             self.splited_data = self.number.split("/")
#             self.divideFunction()
#         elif '^' in self.number:
#             self.sqrtFunction()
        
# while True:
#     print("\t\t\t\t\t\tPlease enter 'exit' to quit if you want")
#     user_input = input("Enter an expression to calculate: ")
#     if user_input.lower() == "exit":
#         break
#     else:
#         obj4 = Calculator(user_input)
#         obj4.splitFunction()
