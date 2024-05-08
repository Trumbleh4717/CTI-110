#Hailey Trumble
#3/8/2024
#P1HW2
#Travel expenses
Budget = int (input("What is your intial budget"))
Destantion = (input("enter your travel destantion"))
Gas = int (input("How much will you spend on gas"))
Accomodation = int (input("How much will you spend on the hotel"))
Food = int (input("How much will you spend on food"))
Remaining = Budget - Gas - Accomodation - Food
print ("Intial Budget:", Budget )
print ("Location:", Destantion )
print ("Gas:", Gas )
print ("Food:", Food)
print ("Hotel:", Accomodation)
print ("Remaining Balance:", Remaining)
