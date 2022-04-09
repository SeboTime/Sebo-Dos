import time
import os

command = ["close", "installer", "sebo-dos"]

print("Commands:")
for commands in command:
    print(commands)

while True:
    print("")
    MainInput = str(input("Launcher: "))
    if MainInput == command[0]:
        break
    elif MainInput == command[1]:
        os.system("py Scripts/Install.py")
    elif MainInput == command[2]:
        print("")
        os.system("py Scripts/Sebo-Dos.py")
        if open("Data/Closed.sebodata", "r").read() == "True":
            if open("Data/Returned.sebodata", "r").read() == "True":
                open("Data/Closed.sebodata", "w").write("False")
                open("Data/Returned.sebodata", "w").write("False")
            elif open("Data/Returned.sebodata", "r").read() == "False":
                open("Data/Closed.sebodata", "w").write("False")
                break
            else:
                print("")
                print(open("Errors/Data", "r").read())
                time.sleep(10)
                break
        elif open("Data/Closed.sebodata", "r").read() == "False":
            print("")
            print("Sebo-Dos is crashed!")
        else:
            print("")
            print(open("Errors/Data", "r").read())
            time.sleep(10)
            break
    else:
        print("{" + MainInput + "}" + "is not a command!")
