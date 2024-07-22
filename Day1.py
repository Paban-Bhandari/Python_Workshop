print ('hello Paban')

#Variables:
#1. string
#2. int
#3. float
#4. char
#5. boolean
#6. complex

#This is a string:
first_name = "Paban"
if first_name == "Paban":
    print("Yes you are Paban, Welcome to the hub")
else:
    print("You can't enter")

#This ia the integer:
number = 20

#This is float:
decimal_number = 30.55

#This is boolean:
is_this_Texas = True

num1 = 100
num2 = 500
print (num1 + num2)

print("This will print out the types")
print(type(first_name))
print(type(number))
print(type(decimal_number))
print(type(is_this_Texas))

# TO take user_input
user_name = input ("What is your name? : ")
user_age = input ("What is your age? : ")
print ("Your Name is " + str(user_name))
print("Your age is " ,(user_age))

# writing a program to create a app that can calculate user age by its date of birth
year_of_birth = input("Enter your year of birth: ")
current_year = 2024

current_age = current_year - int(year_of_birth)
print("Your current age is :",(current_age))

#conditions
if current_age < 18:
    print("Yor are not eligible to enter")
else:
    print("Yes, You can enter")

#loop
for i in range(0,20):
    print(i)

fruits = ('apple','banana','grapes','mango','strawberry')
for i in fruits:
    print(i)

if 'banana' in fruits:
    print("Yay, There is Banana")











    