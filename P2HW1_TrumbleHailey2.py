#Hailey Trumble
#3/8/2024
#P1HW2
#Travel expenses
Budget = int(input("What is your intial budget? "))
Destination = input("Enter your travel destination: ")
Gas = int(input("How much will you spend on gas: "))
Accomodation = int(input("How much will you spend on the hotel: "))
Food = int(input("How much will you spend on food: "))
Remaining = Budget - Gas - Accomodation - Food 
print()
print("------------Travel Expenses------------")
print ("Intial Budget:         $",Budget )
print ("Location:              ",Destination )
print ("Gas:                   $",Gas )
print ("Accomodation:          $",Accomodation )
print ("Food:                  $",Food )
print ("---------------------------------------")
print ()
print ("Remaining Balance:     $",Remaining)
