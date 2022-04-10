import tqdm
import os

Todo = [
    "pip install --upgrade pip",
    "pip install ursina"
    ]
PBar = tqdm.tqdm(total=len(Todo))

for CurrentTodo in Todo:
    os.system(CurrentTodo)
    PBar.update(1)

os.system("py Scripts/Games/FirstPersonWalker/Main.py")
