#Hailey Trumble
#3/27/2024
#P4LAB2
#Use a a wild loop

var1 = int (input("Enter the smaller integer: "))
var2 = int (input("Enter the larger integer: "))

#While var1 us larger, allow the user to re-enter
while var1 >= var2:
    print("First number must be smaller. Try again")
    var1 = int(input("Enter the smaller integer: "))
    var2 = int(input("Enter the larger integer: "))
#The while loop has broken. Values entered correct
for num in range(var1, var2+1, 5):
    print(num, end =" ")
