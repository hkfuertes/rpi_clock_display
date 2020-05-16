#!/usr/bin/env python3

from tkinter import Tk, Label, StringVar, CENTER
from windows import MainWindow
from layouts.ClockLayout import *
import os, pyglet, signal

from config import Config

import locale

pid_file = os.path.join(os.path.dirname(__file__), './current.pid')

def receive_signal(signum, frame):
    # Stopping the app
    print("Closing the app!")
    w.destroy()
    os.remove(pid_file)

if __name__ == '__main__':

    config = Config.getInstance()
    print(config)
    locale.setlocale(locale.LC_ALL, config['locale'])

    # Saving the curren PID
    file = open(pid_file,'w') 
    file.write("{}".format(os.getpid())) 
    file.close() 

    # Prepare for good closing
    signal.signal(signal.SIGTERM, receive_signal)

    #Fontawesome
    pyglet.font.add_file(os.path.join(os.path.dirname(__file__), 'otfs/Font Awesome 5 Free-Solid-900.otf'))
    #OWF
    pyglet.font.add_file(os.path.join(os.path.dirname(__file__), 'otfs/owfont-regular.otf'))

    w = MainWindow()
    w.title("RPI Display")
    w.configure(background='black')

    gl = ClockLayout(w)
    gl.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    # GUI Main window
    w.mainloop()
