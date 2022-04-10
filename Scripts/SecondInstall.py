import imp


import tqdm
import time
import os

Todo = [
    "pip install --upgrade pip",
    "pip install PySimpleGUI"
    ]
PBar = tqdm.tqdm(total=len(Todo))

for CurrentTodo in Todo:
    os.system(CurrentTodo)
    PBar.update(1)