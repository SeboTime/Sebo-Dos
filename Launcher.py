import time
import os

command = ["close", "installer", "sebo-dos"]

print("Commands:")
print(command[0])
print(command[1])
print(command[2])

while True:
    print("")
    DosInput = str(input("Launcher: "))
    if DosInput == command[0]:
        break
    elif DosInput == command[1]:
        os.system("py Scripts/Install.py")
    elif DosInput == command[2]:
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
                print("Your data is corrupted!")
                time.sleep(10)
                break
        elif open("Data/Closed.sebodata", "r").read() == "False":
            print("")
            print("Sebo-Dos is crashed!")
        else:
            print("")
            print("Your data is corrupted!")
            time.sleep(10)
            break
    else:
        print("{" + DosInput + "}" + "is not a command!")
