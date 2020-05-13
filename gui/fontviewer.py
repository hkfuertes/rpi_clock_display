from tkinter import Tk, LEFT, Listbox, Label, StringVar
from FullScreenWindow import *
import pyglet
import fontawesome as fa
import os
import json

def setText(event):
    selected.set("{}".format(color_box.curselection()))

if __name__ == '__main__':
    w = FullscreenWindow()
    w.title("Display")

    font_path = os.path.join(os.path.dirname(__file__), 'otfs\owfont-regular.ttf')
    pyglet.font.add_file(font_path)
    font_name = "owf-regular"


    json_path = os.path.join(os.path.dirname(__file__), 'owfont-regular.maping.json')
    json1_file = open(json_path)
    json1_str = json1_file.read()
    json1_data = json.loads(json1_str)

    #print(json1_data)

    color_box = Listbox(w, font=(font_name, 16))
    color_box.bind('<Double-1>', setText)
    for i in json1_data:
        int_val = int(json1_data[i],0)
        color_box.insert(int_val,"{}".format(chr(int_val)))

    color_box.pack()

    selected=StringVar()
    selected.set("test")
    label = Label(w, textvariable=selected)
    label.pack()

    # GUI Main window
    w.mainloop()
