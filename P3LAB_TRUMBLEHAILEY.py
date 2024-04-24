#Haile Trumble
#3/11/2024
#P3LAB -Branching

#Get info from user
change = int (input("enter amount of change"))

#This represents no change back
if change <= 0:
    print("No change")
num_dollars = change // 100
change = change - (num_dollars * 100)

#Caluculate how many quarters
num_quarters = change //25
change = change - (num_quarters *25)


#Caluculate how many dimes
num_dimes = change //10
change = change - (num_dimes *10)

#Caluculate how many nickels
num_nickels = change //5
change = change - (num_dimes *5)

#Caluculate how many pennies
num_pennies = change //1
#double check
change = change - (num_pennies *1)

#Display info to user
if num_dollars > 0:
    print(num_dollars, end = " ")
    if num_dollars == 1:
        print("dollar")
    else:
        print ("Dollars")

if num_quarters > 0:
    print(num_quarters, end = " ")
    if num_quarters == 1:
        print("quarter")
    else:
        print ("quarters")

