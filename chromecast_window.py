#!/usr/bin/env python3

from tkinter import *
from windows import MainWindow
from layouts import ChromecastLayout
import os, pyglet, signal

from config import Config

import locale

if __name__ == '__main__':
    config = Config.getInstance()
    print(config)

    w = MainWindow()
    w.title("RPI Display Chromecast")
    w.configure(background='black')

    gl = ChromecastLayout(w)
    gl.pack(fill=BOTH)
    
    # GUI Main window
    w.mainloop()
