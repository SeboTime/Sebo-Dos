import turtle

while True:
    print("")
    turtle.bgcolor("black")
    turtle.color("lightblue")
    turtle.forward(0)
    PaintInput = str(input("Sebo-Dos:\paint\ "))
    if PaintInput == "return":
        break
    elif PaintInput == "help":
        print("Commands:")
        print("return")
        print("help")
        print("forward")
        print("backward")
        print("left")
        print("right")
        print("circle")
        print("show")
        print("hide")
        print("on")
        print("off")
        print("speed")
        print("")
    elif PaintInput == "forward":
        turtle.forward(25)
        print("")
    elif PaintInput == "backward":
        turtle.backward(25)
        print("")
    elif PaintInput == "left":
        turtle.left(22.5)
        print("")
    elif PaintInput == "right":
        turtle.right(22.5)
        print("")
    elif PaintInput == "circle":
        print("")
        PaintCircleSize = int(input("Sebo-Dos:\paint\circle\size\ "))
        print("")
        turtle.circle(PaintCircleSize)
    elif PaintInput == "show":
        turtle.showturtle()
        print("")
    elif PaintInput == "hide":
        turtle.hideturtle()
        print("")
    elif PaintInput == "on":
        turtle.pendown()
        print("")
    elif PaintInput == "off":
        turtle.penup()
        print("")
    elif PaintInput == "speed":
        print("")
        PaintSpeed = int(input("Sebo-Dos:\paint\speed\ "))
        print("")
        turtle.speed(PaintSpeed)
    else:
        print("Diesen Command gibt es nicht, porbier mal {help} aus.")
        print("")