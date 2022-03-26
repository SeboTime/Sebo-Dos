import webbrowser
import datetime
import random
import turtle
import time
import sys
import os

import PySimpleGUI as sg
import tqdm

StartWindow = sg.Window(title="Sebo-Dos", icon="Icons/Sebo-Dos.ico", background_color="blue", keep_on_top=True, disable_minimize=True, margins=(50,0), layout=[
    [sg.Button("Start Sebo-Dos")],
    [sg.Button("Reset Data")]
    ])

FirstStartBarTime = random.randint(25, 100)
StartBarTime = random.randint(10, 25)

while True:
    event, values = StartWindow.read()

    if event == "Reset Data":
        open("Data/FirstStart.sebodata", "w").write("True")
        open("Data/Username.sebodata", "w").write("")

        if open("Data/FirstStart.sebodata", "r").read() == "True":
            StartBarTime = FirstStartBarTime

    if event == "Start Sebo-Dos":
        with tqdm.tqdm(total=StartBarTime, desc="Starting", colour="blue") as StartBar:
            StartWindow.close()
            for i in range(StartBarTime):
                time.sleep(0.1)
                StartBar.update(1)
            StartBar.close()
            break

    if event == sg.WIN_CLOSED:
        sys.exit()

os.system("cls")

if open("Data/FirstStart.sebodata", "r").read() == "True":
    open("Data/FirstStart.sebodata", "w").write("False")

if open("Data/Username.sebodata", "r").read() == "":
    NewName = input("Name: ")
    open("Data/Username.sebodata", "w").write(NewName)


os.system("cls")

print("Sebo-Dos Version: 1.6")
print("")
print("Hello " + str(open("Data/Username.sebodata", "r").read()) + "!")
print("")

def DosMain():

    command0 = "shutdown"
    command1 = "help"
    command2 = "system.command"
    command3 = "time"
    command4 = "date"
    command5 = "say"
    command6 = "old.paint"
    command7 = "update"
    command8 = "start"
    secret0 = "old"

    DosInput = str(input("Sebo-Dos:\ "))
    if DosInput == command0:
        print("")
        print("Shutdown...")
        print("")
        time.sleep(1)
        sys.exit()
    elif DosInput == command1:
        print("Commands:")
        print(command0)
        print(command1)
        print(command2)
        print(command3)
        print(command4)
        print(command5)
        print(command6)
        print(command7)
        print(command8)
        print("")
        DosMain()
    elif DosInput == command2:
        print("")
        SystemCommandInput = str(input("System-Command: "))
        print("")
        os.system(SystemCommandInput)
        print("")
        DosMain()
    elif DosInput == command3:
        print("")
        print(time.strftime("%H:%M:%S"))
        print("")
        DosMain()
    elif DosInput == command4:
        print("")
        print(datetime.date.today())
        print("")
        DosMain()
    elif DosInput == command5:
        print("")
        SayInput = str(input("Text: "))
        print("")
        print(SayInput)
        print("")
        DosMain()
    elif DosInput == command6:
        OldPaintMain()
    elif DosInput == command7:
        print("")
        webbrowser.open("https://github.com/SeboTime/Sebo-Dos/releases")
        DosMain()
    elif DosInput == command8:
        print("")
        StartInput = str(input("Start: "))
        os.system("start " + StartInput)
        print("")
        DosMain()
    elif DosInput == secret0:
        os.system("ren old Sebo-Dos-OLD.py")
        os.system("start Sebo-Dos-OLD.py")
        DosMain( )
    else:
        print("{" + DosInput + "} is not a command, try {help}.")
        print("")
        DosMain()

def OldPaintMain():
        print("")
        turtle.bgcolor("black")
        turtle.color("lightblue")
        turtle.forward(0)
        PaintInput = str(input("Sebo-Dos:\paint\ "))
        if PaintInput == "close":
            print("")
            turtle.bye()
            DosMain()
        elif PaintInput == "help":
            print("Commands:")
            print("close")
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
            OldPaintMain()
        elif PaintInput == "forward":
            turtle.forward(25)
            print("")
            OldPaintMain()
        elif PaintInput == "backward":
            turtle.backward(25)
            print("")
            OldPaintMain()
        elif PaintInput == "left":
            turtle.left(22.5)
            print("")
            OldPaintMain()
        elif PaintInput == "right":
            turtle.right(22.5)
            print("")
            OldPaintMain()
        elif PaintInput == "circle":
            print("")
            PaintCircleSize = int(input("Sebo-Dos:\paint\circle\size\ "))
            print("")
            turtle.circle(PaintCircleSize)
            OldPaintMain()
        elif PaintInput == "show":
            turtle.showturtle()
            print("")
            OldPaintMain()
        elif PaintInput == "hide":
            turtle.hideturtle()
            print("")
            OldPaintMain()
        elif PaintInput == "on":
            turtle.pendown()
            print("")
            OldPaintMain()
        elif PaintInput == "off":
            turtle.penup()
            print("")
            OldPaintMain()
        elif PaintInput == "speed":
            print("")
            PaintSpeed = int(input("Sebo-Dos:\paint\speed\ "))
            print("")
            turtle.speed(PaintSpeed)
            OldPaintMain()
        else:
            print("Diesen Command gibt es nicht, porbier mal {help} aus.")
            print("")
            OldPaintMain()

DosMain()
