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

if open("Data/AddonLaunch.sebodata", "r").read() == "False":
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
    print("Sebo-Dos Version: 1.7.1")
    print("")
    print("Hello " + str(open("Data/Username.sebodata", "r").read()) + "!")
    
elif open("Data/AddonLaunch.sebodata", "r").read() == "True":
    open("Data/AddonLaunch.sebodata", "w").write("False")
else:
    print("Your data is corrupted!")
    time.sleep(5)
    sys.exit()

def DosMain():
    command0 = "close"
    command1 = "return"
    command2 = "help"
    command3 = "system.command"
    command4 = "time"
    command5 = "date"
    command6 = "say"
    command7 = "old.paint"
    command8 = "update"
    addon0 = "addon1"
    addon1 = "addon2"
    addon2 = "addon3"
    secret0 = "old"

    print("")
    DosInput = str(input("Sebo-Dos:\ "))
    if DosInput == command0:
        open("Data/Closed.sebodata", "w").write("True")
        sys.exit()
    elif DosInput == command1:
        open("Data/Closed.sebodata", "w").write("True")
        open("Data/Returned.sebodata", "w").write("True")
    elif DosInput == command2:
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
        print(addon0)
        print(addon1)
        print(addon2)
        DosMain()
    elif DosInput == command3:
        print("")
        SystemCommandInput = str(input("System-Command: "))
        print("")
        os.system(SystemCommandInput)
        DosMain()
    elif DosInput == command4:
        print("")
        print(time.strftime("%H:%M:%S"))
        DosMain()
    elif DosInput == command5:
        print("")
        print(datetime.date.today())
        DosMain()
    elif DosInput == command6:
        print("")
        SayInput = str(input("Text: "))
        print("")
        print(SayInput)
        DosMain()
    elif DosInput == command7:
        os.system("py Scripts/OldPaint.py")
        DosMain()
    elif DosInput == command8:
        print("")
        webbrowser.open("https://github.com/SeboTime/Sebo-Dos/releases/latest")
        DosMain()
    elif DosInput == addon0:
        print("")
        open("Data/AddonLaunch.sebodata", "w").write("True")
        os.system("py Scripts/Addons/Addon1.py")
        DosMain()
    elif DosInput == addon1:
        print("")
        open("Data/AddonLaunch.sebodata", "w").write("True")
        os.system("py Scripts/Addons/Addon2.py")
        DosMain()
    elif DosInput == addon2:
        print("")
        open("Data/AddonLaunch.sebodata", "w").write("True")
        os.system("py Scripts/Addons/Addon3.py")
        DosMain()
    elif DosInput == secret0:
        os.system("ren old Sebo-Dos-OLD.py")
        os.system("start Sebo-Dos-OLD.py")
        DosMain()
    else:
        print("{" + DosInput + "} is not a command, try {help}.")
        DosMain()

DosMain()
