#Hailey Trumble
#4/22/2024
#P5HW
#Math quiz



def main():
    print("Welcome to the Math Quiz!")
    print()
    print()
    print("Main Menu")
    print("1.Adding Random Numbers")
    print("2.Subtracting Random Numbers")
    print("3.Exit")
    option = int(input("Please choose one of these options:"))
    while option != 3:
        if option == 1:
            print("add")
        if option ==2:

            print("subtract")
        option = int(input("Please choose one of these options:"))

    print("Program is ending")
            
            
    #Call all other functions from here

import random

number = random.randint(1,10)

print(f"The random number is {number}")
#Call the main
main()



"""
def is_num_in_list(num_list):
    num= int(input("Gimme a number: "))
    while num not in num_list:
        print("The number you gave is not in
        num = int(input("Gimme a number:  "))
 """  


