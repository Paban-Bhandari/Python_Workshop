# ####################################################
# #classes_example
# #to define class we use class and its name:

# class MyCollege:
#     x = "Ram"

# obj = MyCollege()
# print(obj.x)
# ####################################################

# ####################################################
# #This is how we create class with constructor:
# class ClassWithCons:
#     def __init__(self) -> None:
#         print("This is being called when initiazating object")

# obj1 = ClassWithCons()
# ####################################################

# ####################################################
# #This is how we passs parameter(data) to class
# class ClassWithData:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address

#         print(self.name)
#         print(self.address)

# obj2 = ClassWithData ('Paban',"Changathali")     
# ####################################################

# ####################################################
# #This is how we add multiple function in a class:
# class multipleFunctionClass:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

#     def printName(self):
#         print(self.name)
#     def printAge(self):
#         print(self.age)    
#     def printAdress(self):
#         print(self.address)

# obj3 = multipleFunctionClass('Paban',20, 'Bhaktapur')
# obj3.printName()
# obj3.printAge()
# obj3.printAdress()
# ####################################################

#######################################################
#making calculator:
#######################################################

# #######################################################
# #inheritance in class
# class ParentClass:
#     def __init__(self, name):
#         self.name = name
#         self.class_type = "BIT"
#         print("This is Parent Class")

#     def printName(self):
#         print(self.name)

# #Here we are inherting the parent class
# class ChildClass(ParentClass):
#     pass
# obj1 = ChildClass("Paban")
# print(obj1.class_type)
# obj1.printName()
# #######################################################

# ##################################################################
# # Class parent2
# class parent2:
#     def __init__(self, name, address) -> None:
#          self.name = name
#          self.address = address

#          print("This is being called from parent class")
#          print(f"{self.name} {self.address}")

# class child2(parent2):
#      def printnumber(self):
#           print("This is number")

# obj3 = child2("Kushal", "chakrapad")
# obj4 = child2("Pawan", "bouddha")
# obj5 = child2("Ram", "bouddha")
# #obj3.printnumber()
# ##################################################################

#################################################################
import math
print(math.sqrt(4))
#################################################################