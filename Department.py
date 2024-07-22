print("\t\t\t\t\t\t Welcome to Fruit Department")

# Creating a empty list
fruits = []

while True:
    print("Add Fruits name to append in the data list or remove from the data list:")
    print("Press 1 to add item and 2 to delete item")
    choose = input("Choose the option: ")
    item = input("Enter fruit name: ")

    if int(choose) == 1:
        fruits.append(item)
    elif int(choose) == 2:
        fruits.remove(item)

    print(fruits)

#creating limit to manipulate data in the department
#The limit is user can only add or delete data from department 10 times
    limit = 5
    print("You have", limit , 'time limit')
    limit = limit - 1
    if limit == 0:
        print("Your limit for today have been completed. Please come back later.")
        break