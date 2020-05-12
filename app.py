from tkinter import Tk, Label, StringVar, CENTER
from FullScreenWindow import *
from panels.ClockLayout import *


if __name__ == '__main__':
    w = FullscreenWindow()
    w.title("RPI Display")
    w.configure(background='black')

    gl = ClockLayout(w)
    gl.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    # GUI Main window
    w.mainloop()
