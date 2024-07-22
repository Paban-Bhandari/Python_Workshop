######################
#1. variable
#2. data type
#3. conditions
#4. Loop
#5. list
#6. dictionary
#7. tuple
#8. set
#9. function
########################

########################
#name = "Paban Bhandari"
#print (type(name))
#########################

####################################################
#how to identify the given number is odd or even
# while True:
number = input("Enter a number: ")
if int(number)%2 == 0:
    if int(number)<100:
        print((number)," is less than 100")
    print(str(number) + " is even.")
else:
    print(str(number) + " is odd.")
#####################################################

#####################################################
#loop
for i in range(1,5):
    if i == 3:
        print("I have got 3 in the loop")
        break #to break the loop
    print(i)
#####################################################

###################################################
num = 5
for i in range(1,num+1):
    for j in range(i):
        print("*", end="")
    print()
###################################################

###########################################################################
#list in Python
number_list = [3,4,5,10,20,30] #number in list
fruit_list = ['Apple','Banana','Mango','Orange','Grapes','Watermelon','Cherry']  #string in list



#To read the item from the list:
# print(number_list [0])
# print(fruit_list [3])

#To check the item in the list:
# if 'Mango' in fruit_list:
#     print("Yes, We have Mangoes. You want to buy it?")
# else:
#     print("Sorry! We don't have Mangoes")

#To add new items in the list:
# while True:
#     new_fruits = input("Enter new fruits brought in department: ")
#     fruit_list.append(new_fruits)
#     print("Fruit list after adding new item: ")
#     print(fruit_list)

#To remove the item from the list:
# while True:
#     buyed_fruits = input("Enter fruit you buy from the department: ")
#     fruit_list.remove(buyed_fruits)
#     print("Fruit list after removing existing fruit: ")
#     print(fruit_list)

#To remove the item from the list:
for i in range(1,5):
    buyed_fruits = input("Enter fruit you buy from the department: ")
    if buyed_fruits == 'exit':
        break
    fruit_list.remove(buyed_fruits)
    print("Fruit list after removing existing fruit: ")
    print(fruit_list)
###########################################################################
