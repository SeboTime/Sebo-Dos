import time
import os

command = ["close", "help", "install", "sebo-dos"]
Start = True

while True:
    if Start == True:
        Start = False
    elif Start == False:
        print("")
    else:
        print("")
        print(open("Errors/Unknown.error", "r").read())
        time.sleep(10)
        break
    MainInput = str(input("Launcher: "))
    if MainInput == command[0]:
        break
    if MainInput == command[1]:
        print("Commands:")
        for commands in command:
            print(commands)
    elif MainInput == command[2]:
        os.system("py Scripts/Install.py")
    elif MainInput == command[3]:
        print("")
        os.system("py Scripts/Sebo-Dos.py")
        if open("Data/Closed.data", "r").read() == "True":
            if open("Data/Returned.data", "r").read() == "True":
                open("Data/Closed.data", "w").write("False")
                open("Data/Returned.data", "w").write("False")
            elif open("Data/Returned.data", "r").read() == "False":
                open("Data/Closed.data", "w").write("False")
                break
            else:
                print("")
                print(open("Errors/Data.error", "r").read())
                time.sleep(10)
                break
        elif open("Data/Closed.data", "r").read() == "False":
            print("")
            print("Sebo-Dos is crashed!")
        else:
            print("")
            print(open("Errors/Data.error", "r").read())
            time.sleep(10)
            break
    else:
        print("{" + MainInput + "}" + "is not a command!")
