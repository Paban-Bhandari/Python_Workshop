while True:
    Name = input("Enter your Name: ")
    Percentage= input("Enter your Marks in percentage: ")

    if float(Percentage) > 40:
        print("Congrats!!! " + str(Name) + " Yor are pass with percentage " + (Percentage))
    else:
        print("Sorry " + str(Name) + " You are fail with percentage " + (Percentage) + " Better luck next time!!.")
