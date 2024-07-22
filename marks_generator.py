print("This is Mark Generator")
#Showing user other information about marks generator
#To show anything in written form we use print()
#print("\t \t \t Marks Generator created by TEXAS Student.")
while True:
    #to take the user name
    Name = input("Enter your Name: ")
    #To create it we need to take user marks in each subject
    DBMS = input("Enter your marks in DBMS: ")
    Technopreneurship = input("Enter your marks in Technopreneurship: ")
    SAD = input("Enter your marks in SAD: ")
    AI = input("Enter your marks in AI: ")
    CDC = input("Enter your marks in CDC: ")
    #Getting total marks by adding marks of each subject
    Total_Obtained_Mark = float(DBMS) + float(Technopreneurship) + float(SAD) + float(AI) + float(CDC)
    print("Your Marks In Total: " + str(Total_Obtained_Mark))
    #to get the percentage of a student we calculate like this:
    #total obtained marks divided by total marks of all the subject multiple by 100
    Total_Mark = 500

    Percentage = (float(Total_Obtained_Mark)/int(Total_Mark))*100

    if Percentage >= 80 and Percentage <= 100:
        print("Congratulations!!! " + str(Name) + " You have got Distinction with " + str(Percentage) + " Percentage")
    elif Percentage >= 60 and Percentage <= 79:
        print("Congratulations!!! " + str(Name) + " You have got First Division with " + str(Percentage) + " Percentage")
    elif Percentage >= 40 and Percentage <= 59:
        print("Congratulations!!! " + str(Name) + " You have got Second Division with " + str(Percentage) + " Percentage")
    else:
        print("Sorry " + str(Name) + " you are fail with " + str(Percentage) + " Percentage. Better luck next time." )
    