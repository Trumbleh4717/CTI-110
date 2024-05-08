import turtle
win = turtle.Screen()
hailey = turtle.Turtle()

#add some display options
hailey.pensize(4)      #increase pensize (takes intege)
hailey.pencolor("purple")   #set pencolor (takes string)
#Draw square
for item in range(4):
    #Actions to happen
    hailey.forward(100)
    hailey.left(90)
    
#Draw triangle
for item in range(3):
    #Actions to happen
    hailey.forward(100)
    hailey.left(120)
