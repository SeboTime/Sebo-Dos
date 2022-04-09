from genericpath import exists
import os

command = ["return", "help"]

while True:
    print("")
    MainInput = str(input("Sebo-Dos:\Games\ "))
    if MainInput == command[0]:
        break
    elif MainInput == command[1]:
        print("Commands:")
        for commands in command:
            print(commands)
        print("")
        print("Games:")
        for games in os.listdir("Scripts/Games/"):
            if os.path.isfile("Scripts/Games/" + games) == True:
                print(games[:-3])
    elif exists("Scripts/Games/" + MainInput + ".py") == True:
        os.system("py Scripts/Games/" + MainInput + ".py")
