from genericpath import exists
import random
import time
import os

import PySimpleGUI as sg
import tqdm

import Data

StartWindow = sg.Window(title="Sebo-Dos", icon="Icons/Sebo-Dos.ico", background_color="blue", keep_on_top=True, disable_minimize=True, margins=(50,0), layout=[
    [sg.Button("Start Sebo-Dos")],
    [sg.Button("Reset Data")]
    ])

FirstStartBarTime = random.randint(25, 100)
StartBarTime = random.randint(10, 25)
WinClosed = False

while True:
    event, values = StartWindow.read()
    if event == "Reset Data":
        Data.User.FirstLaunch = True
        Data.User.Username = ""
    if Data.User.FirstLaunch == True:
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
        open("Data/Closed.data", "w").write("True")
        open("Data/Returned.data", "w").write("True")
        WinClosed = True
        break

if WinClosed == False:
    if Data.User.Username == "":
        print("")
        NewName = input("Name: ")
        Data.User.Username = NewName
    if Data.User.Username == True:
        Data.User.FirstLaunch = False
        
    print("")
    print("Sebo-Dos Version: 1.8")
    print("")
    print("Hello " + Data.User.Username + "!")

def DosMain():
    Icommand = ["close", "return", "help"]

    print("")
    MainInput = str(input("Sebo-Dos:\ "))
    if MainInput == Icommand[0]:
        open("Data/Closed.data", "w").write("True")
    elif MainInput == Icommand[1]:
        open("Data/Closed.data", "w").write("True")
        open("Data/Returned.data", "w").write("True")
    elif MainInput == Icommand[2]:
        print("Commands:")
        for Icommands in Icommand:
            print(Icommands)
        for commands in os.listdir("Scripts/Commands/"):
            print(commands[:-3])
        print("")
        print("Programs:")
        for commands in os.listdir("Scripts/Programs/"):
            print(commands[:-3])
        DosMain()
    elif exists("Scripts/Commands/" + MainInput + ".py") == True:
        os.system("py Scripts/Commands/" + MainInput + ".py")
        DosMain()
    elif exists("Scripts/Programs/" + MainInput + ".py") == True:
        os.system("py Scripts/Programs/" + MainInput + ".py")
        DosMain()
    else:
        print("{" + MainInput + "} is not a command, try {help}.")
        DosMain()

if WinClosed == False:
    DosMain()