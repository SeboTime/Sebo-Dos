import imp
from os import system
import platform
import os

print("")
if platform.system() == "Windows":
    os.system("py Scripts/Games/FirstPersonWalker/Install.py")
else:
    print("Your system doesn't support this game!")