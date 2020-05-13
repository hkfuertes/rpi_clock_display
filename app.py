from tkinter import Tk, Label, StringVar, CENTER
from FullScreenWindow import *
from layouts.ClockLayout import *
import os, pyglet


if __name__ == '__main__':
    #Fontawesome
    pyglet.font.add_file(os.path.join(os.path.dirname(__file__), 'otfs/Font Awesome 5 Free-Solid-900.otf'))
    #OWF
    pyglet.font.add_file(os.path.join(os.path.dirname(__file__), 'otfs/owfont-regular.otf'))

    w = FullscreenWindow()
    w.title("RPI Display")
    w.configure(background='black')

    gl = ClockLayout(w)
    gl.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    # GUI Main window
    w.mainloop()
