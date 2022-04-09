import random
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
        open("Data/Username.sebodata", "w").write(" ")
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
        open("Data/Closed.sebodata", "w").write("True")
        os.system("py Launcher.py")

if open("Data/FirstStart.sebodata", "r").read() == "True":
    open("Data/FirstStart.sebodata", "w").write("False")
if open("Data/Username.sebodata", "r").read() == " ":
    print("")
    NewName = input("Name: ")
    open("Data/Username.sebodata", "w").write(NewName)
    
print("")
print("Sebo-Dos Version: 1.8")
print("")
print("Hello " + str(open("Data/Username.sebodata", "r").read()) + "!")

def DosMain():
    command = ["close", "return", "help", "time", "date", "say", "old.paint"]
    addon = ["addon1", "addon2", "addon3"]
    secret = ["old"]

    print("")
    DosInput = str(input("Sebo-Dos:\ "))
    if DosInput == command[0]:
        open("Data/Closed.sebodata", "w").write("True")
    elif DosInput == command[1]:
        open("Data/Closed.sebodata", "w").write("True")
        open("Data/Returned.sebodata", "w").write("True")
    elif DosInput == command[2]:
        print("Commands:")
        print(command[0])
        print(command[1])
        print(command[2])
        print(command[3])
        print(command[4])
        print(command[5])
        print(command[6])
        print(addon[0])
        print(addon[1])
        print(addon[2])
        DosMain()
    elif DosInput == command[3]:
        os.system("py Scripts/Commands/time.py")
        DosMain()
    elif DosInput == command[4]:
        os.system("py Scripts/Commands/date.py")
        DosMain()
    elif DosInput == command[5]:
        os.system("py Scripts/Commands/say.py")
        DosMain()
    elif DosInput == command[6]:
        os.system("py Scripts/OldPaint.py")
        DosMain()
    elif DosInput == addon[0]:
        print("")
        open("Data/AddonLaunch.sebodata", "w").write("True")
        os.system("py Scripts/Addons/Addon1.py")
        DosMain()
    elif DosInput == addon[1]:
        print("")
        os.system("py Scripts/Addons/Addon2.py")
        DosMain()
    elif DosInput == addon[2]:
        print("")
        os.system("py Scripts/Addons/Addon3.py")
        DosMain()
    elif DosInput == secret[0]:
        os.system("py Scripts/old")
        DosMain()
    else:
        print("{" + DosInput + "} is not a command, try {help}.")
        DosMain()

DosMain()
